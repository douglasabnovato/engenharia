"""Estado dos repositórios de um dono, só leitura.

Para cada repositório: critérios e "Finalizado" lidos do MVP.md, seção do ciclo no plano,
PRs abertos (com o CI de cada um), CI da branch, issues abertas com 3+ critérios e se o site responde.

Uso:
  python scripts/estado.py --dono <dono> [--repos a,b,c] [--excluir x,y] [--branch principal|<nome>]
                           [--ciclo "Ciclo de 09/11/2026"] [--saida estado.json]

Requer o GitHub CLI autenticado (`gh auth status`). O caminho do gh vem de --gh, da variável GH
ou do PATH. Nada é gravado no GitHub.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding="utf-8")

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("--dono", required=True, help="usuário ou organização no GitHub")
ap.add_argument("--repos", default="", help="lista separada por vírgula (padrão: todos os não arquivados)")
ap.add_argument("--excluir", default="", help="repositórios fora do escopo, separados por vírgula")
ap.add_argument("--branch", default="principal", help="'principal' (padrão) ou o nome de uma branch, ex.: developer/sprint-2026-11-12")
ap.add_argument("--ciclo", default="", help="texto da seção do ciclo a procurar no PLANO-DE-ACAO.md")
ap.add_argument("--saida", default="estado.json", help="arquivo JSON de saída")
ap.add_argument("--gh", default=os.environ.get("GH") or shutil.which("gh") or "gh", help="caminho do GitHub CLI")
A = ap.parse_args()


def gh(*args):
    r = subprocess.run([A.gh, *args], capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.stdout if r.returncode == 0 else ""


def http(url):
    if not url:
        return "-"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            return str(r.status)
    except urllib.error.HTTPError as e:
        return str(e.code)
    except Exception as e:  # rede, DNS, tempo esgotado
        return type(e).__name__


def raw(full, path, ref):
    return gh("api", f"repos/{full}/contents/{path}?ref={ref}", "-H", "Accept: application/vnd.github.raw")


def ci_do_pr(rollup):
    cs = [c for c in rollup if c.get("__typename") == "CheckRun"]
    if not cs:
        return "sem-checks"
    if any(c.get("status") != "COMPLETED" for c in cs):
        return "rodando"
    return "verde" if all(c.get("conclusion") in ("SUCCESS", "SKIPPED", "NEUTRAL") for c in cs) else "vermelho"


def um(x):
    nome = x["name"]
    full = f"{A.dono}/{nome}"
    principal = (x.get("defaultBranchRef") or {}).get("name") or "main"
    ref = principal if A.branch == "principal" else A.branch
    arvore = json.loads(gh("api", f"repos/{full}/git/trees/{ref}?recursive=1") or '{"tree":[]}').get("tree", [])
    paths = [p["path"] for p in arvore]

    plano = next((p for p in paths if re.search(r"PLANO-DE-ACAO\.md$", p)), None)
    ciclo = bool(plano and A.ciclo and A.ciclo in raw(full, plano, ref))

    mvp = next((p for p in paths if re.search(r"(^|/)MVP\.md$", p)), None)
    fin, resumo = "-", None
    if mvp:
        t = raw(full, mvp, ref)
        m = re.search(r"Finalizado:?\**\s*:?\s*\**(sim|não)", t, re.I)
        fin = m.group(1).lower() if m else "?"
        m = re.search(r"Resumo:?\**:?\s*\**\s*(\d+) de (\d+)", t)
        resumo = [int(m.group(1)), int(m.group(2))] if m else None

    prs = json.loads(gh("pr", "list", "--repo", full, "--state", "open", "--json",
                        "number,headRefName,baseRefName,author,labels,statusCheckRollup") or "[]")
    meus = [dict(n=p["number"], de=p["headRefName"], para=p["baseRefName"], ci=ci_do_pr(p["statusCheckRollup"]),
                 rotulos=[r["name"] for r in p["labels"]])
            for p in prs if "dependabot" not in p["author"]["login"]]
    dependabot = sum("dependabot" in p["author"]["login"] for p in prs)

    run = json.loads(gh("run", "list", "--repo", full, "--branch", ref, "--limit", "1", "--json", "conclusion,status") or "[]")
    ci = (run[0]["conclusion"] or run[0]["status"]) if run else "sem CI"

    iss = json.loads(gh("issue", "list", "--repo", full, "--state", "open", "--limit", "300", "--json", "number,body,labels") or "[]")
    com3 = sum(len(re.findall(r"- \[ \]", i["body"] or "")) >= 3 for i in iss)
    resp = sum(any(l["name"] == "depende-do-responsavel" for l in i["labels"]) for i in iss)

    home = x.get("homepageUrl") or ""
    pages = json.loads(gh("api", f"repos/{full}/pages") or "{}").get("html_url", "")
    return dict(repo=nome, principal=principal, ref=ref, resumo=resumo, finalizado=fin, ciclo=ciclo, ci=ci,
                prs=meus, dependabot=dependabot, abertas=len(iss), com3=com3, depende_responsavel=resp,
                home=home, http=http(home or pages), pages=pages)


fora = {r for r in A.excluir.split(",") if r}
lista = json.loads(gh("repo", "list", A.dono, "--limit", "300", "--json", "name,defaultBranchRef,homepageUrl,isArchived") or "[]")
if A.repos:
    quero = set(A.repos.split(","))
    lista = [x for x in lista if x["name"] in quero]
lista = [x for x in lista if x["name"] not in fora and not x["isArchived"]]
if not lista:
    sys.exit("Nenhum repositório. Confira --dono, --repos e se o gh está autenticado.")

with ThreadPoolExecutor(8) as ex:
    out = list(ex.map(um, sorted(lista, key=lambda z: z["name"])))

with open(A.saida, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

for d in out:
    r = f"{d['resumo'][0]}/{d['resumo'][1]}" if d["resumo"] else "-"
    prs = " ".join(f"#{p['n']}:{p['de']}->{p['para']}({p['ci']})" for p in d["prs"]) or "-"
    print(f"{d['repo']:26} crit={r:6} fin={d['finalizado']:3} ciclo={'S' if d['ciclo'] else 'n'} ci={d['ci']:9} "
          f"issues={d['abertas']}/{d['com3']}(resp {d['depende_responsavel']}) dep={d['dependabot']} http={d['http']} prs={prs}")
print(f"\n{len(out)} repositórios -> {A.saida}")
