"""Preenche os campos dos itens de um ou mais Projects (v2) a partir das issues. Idempotente.

Só grava o que falta; Resultado, Depende de, Pontos e Evidência acompanham o estado real da issue.
Também põe responsável (o usuário autenticado), um rótulo de tipo e a milestone, quando faltam.
Nunca apaga item, campo, rótulo ou issue.

Por padrão SÓ SIMULA: mostra quantas gravações faria. Use --gravar para aplicar.

Uso:
  python scripts/preencher-project.py --dono <dono> --projects 2[,1] [--excluir x,y]
         [--niveis niveis.json] [--fim AAAA-MM-DD] [--milestone-padrao "MVP"] [--gravar]

niveis.json (opcional) mapeia repositório para Frente: {"aircnc": "Estudo", "components": "Produto"}.
Sem o arquivo, a Frente padrão é "Vitrine".
"Depende de" = "Responsável" quando a issue tem o rótulo `depende-do-responsavel`.

Requer o GitHub CLI autenticado com escopo `project`. Caminho do gh: --gh, variável GH ou PATH.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("--dono", required=True)
ap.add_argument("--projects", default="2", help="números dos Projects, separados por vírgula")
ap.add_argument("--excluir", default="", help="repositórios fora do escopo")
ap.add_argument("--niveis", default="", help="JSON repositório -> Frente (Estudo, Vitrine, Produto, Piloto)")
ap.add_argument("--fim", default="", help="data de Fim para issues abertas (AAAA-MM-DD); vazio = não preenche")
ap.add_argument("--milestone-padrao", default="", help="milestone a criar quando o repositório não tem nenhuma; vazio = não cria")
ap.add_argument("--rotulo-responsavel", default="depende-do-responsavel")
ap.add_argument("--gravar", action="store_true", help="aplica as mudanças (sem isso, só simula)")
ap.add_argument("--gh", default=os.environ.get("GH") or shutil.which("gh") or "gh")
A = ap.parse_args()

EX = {r for r in A.excluir.split(",") if r}
FRENTE = json.load(open(A.niveis, encoding="utf-8")) if A.niveis else {}
PONTOS = {"XS": 1, "S": 2, "M": 3, "L": 5, "XL": 8}
CAMPOS_NOVOS = [
    ("Tipo", "SINGLE_SELECT", "Funcionalidade,Correção,Documentação,Qualidade,Infraestrutura,Conteúdo,Ideia"),
    ("Frente", "SINGLE_SELECT", "Piloto,Vitrine,Estudo,Produto"),
    ("Resultado", "SINGLE_SELECT", "Concluída,Não planejada,Aberta"),
    ("Depende de", "SINGLE_SELECT", "Ninguém,Responsável,Claude"),
    ("Pontos", "NUMBER", None), ("Objetivo", "TEXT", None), ("Evidência", "TEXT", None),
]


def run(*args, escrita=False):
    if escrita and not A.gravar:
        return ""
    for _ in range(8):
        r = subprocess.run([A.gh, *args], capture_output=True, text=True, encoding="utf-8", errors="replace")
        if r.returncode == 0:
            return r.stdout
        if re.search("rate limit|abuse|secondary|timeout|502|504", r.stderr, re.I):
            time.sleep(120)
            continue
        print("ERRO", args[:3], r.stderr[-220:], flush=True)
        return ""
    return ""


Q = """query($c:String){user(login:"%s"){projectV2(number:%d){id items(first:100,after:$c){pageInfo{hasNextPage endCursor} nodes{id
 content{... on Issue{id number title body state stateReason url createdAt closedAt repository{name} assignees(first:1){totalCount}
 labels(first:20){totalCount nodes{name}} milestone{title}
 closedByPullRequestsReferences(first:1,includeClosedPrs:true){nodes{url}} comments(last:1){nodes{url}}}}
 fieldValues(first:30){nodes{... on ProjectV2ItemFieldTextValue{text field{... on ProjectV2FieldCommon{name}}}
 ... on ProjectV2ItemFieldNumberValue{number field{... on ProjectV2FieldCommon{name}}}
 ... on ProjectV2ItemFieldDateValue{date field{... on ProjectV2FieldCommon{name}}}
 ... on ProjectV2ItemFieldSingleSelectValue{name field{... on ProjectV2FieldCommon{name}}}}}}}}}}"""


def itens(n):
    out, cur = [], None
    while True:
        args = ["api", "graphql", "-f", "query=" + Q % (A.dono, n)]
        if cur:
            args += ["-f", "c=" + cur]
        d = json.loads(run(*args))["data"]["user"]["projectV2"]
        out += d["items"]["nodes"]
        if not d["items"]["pageInfo"]["hasNextPage"]:
            return d["id"], out
        cur = d["items"]["pageInfo"]["endCursor"]


def tipo(titulo):
    t = titulo.lower()
    for pat, v in (("fix|bug|corrig|quebrad|falha", "Correção"),
                   ("ci|deploy|publicar|hospedar|render|pages|devops|vite|node", "Infraestrutura"),
                   ("test|qa|lint|lcp|acessib|cobertura|perform", "Qualidade"),
                   ("doc|readme|plano|licen", "Documentação"),
                   ("ideia|site institucional|anúncio", "Ideia")):
        if re.search(rf"\b({pat})", t):
            return v
    return "Funcionalidade"


def objetivo(c):
    m = re.search(r"##\s*OBJETIVO[^\n]*\n+([^\n#][^\n]*)", c.get("body") or "", re.I)
    txt = m.group(1).strip() if m else "Resolver: " + " ".join(c["title"].split())
    return re.sub(r"https?://\S+", "", txt)[:240]


eu = json.loads(run("api", "graphql", "-f", "query={viewer{id}}"))["data"]["viewer"]["id"]
milestones, stats = {}, {}
for n in (int(x) for x in A.projects.split(",")):
    tem = {f["name"] for f in json.loads(run("project", "field-list", str(n), "--owner", A.dono, "--limit", "60", "--format", "json"))["fields"]}
    for nome, tipo_campo, opcoes in CAMPOS_NOVOS:
        if nome not in tem:
            cmd = ["project", "field-create", str(n), "--owner", A.dono, "--name", nome, "--data-type", tipo_campo]
            if opcoes:
                cmd += ["--single-select-options", opcoes]
            run(*cmd, escrita=True)
    campos = {f["name"]: f for f in json.loads(run("project", "field-list", str(n), "--owner", A.dono, "--limit", "60", "--format", "json"))["fields"]}
    pid, its = itens(n)
    muts, escopo = [], 0

    def setv(item, nome, kind, val):
        if nome not in campos:
            return  # campo ainda não existe (simulação)
        f = campos[nome]["id"]
        if kind == "sel":
            oid = next((o["id"] for o in campos[nome].get("options", []) if o["name"] == val), None)
            if not oid:
                return
            v = '{singleSelectOptionId:"%s"}' % oid
        elif kind == "num":
            v = "{number:%s}" % val
        elif kind == "date":
            v = '{date:"%s"}' % val
        else:
            v = "{text:%s}" % json.dumps(val, ensure_ascii=False)
        muts.append('updateProjectV2ItemFieldValue(input:{projectId:"%s",itemId:"%s",fieldId:"%s",value:%s}){clientMutationId}' % (pid, item, f, v))

    for it in its:
        c = it.get("content") or {}
        repo = (c.get("repository") or {}).get("name")
        if not repo or repo in EX:
            continue
        escopo += 1
        vals = {fv["field"]["name"]: fv.get("name") or fv.get("text") or fv.get("date") or fv.get("number")
                for fv in it["fieldValues"]["nodes"] if fv.get("field")}
        fechada = c["state"] == "CLOSED"
        rotulos = {l["name"] for l in c["labels"]["nodes"]}
        quer = {
            "Tipo": ("sel", tipo(c["title"])),
            "Frente": ("sel", FRENTE.get(repo, "Vitrine")),
            "Prioridade": ("sel", "P3" if fechada else "P2"),
            "Tamanho": ("sel", "S"),
            "Início": ("date", c["createdAt"][:10]),
            "Objetivo": ("txt", objetivo(c)),
        }
        if fechada:
            quer["Fim"] = ("date", c["closedAt"][:10])
        elif A.fim:
            quer["Fim"] = ("date", A.fim)
        forca = {
            "Resultado": ("sel", "Não planejada" if fechada and c.get("stateReason") == "NOT_PLANNED" else "Concluída" if fechada else "Aberta"),
            "Depende de": ("sel", "Ninguém" if fechada else "Responsável" if A.rotulo_responsavel in rotulos else "Claude"),
            "Pontos": ("num", PONTOS.get(vals.get("Tamanho") or "S", 2)),
        }
        prs, coms = c["closedByPullRequestsReferences"]["nodes"], c["comments"]["nodes"]
        ev = prs[0]["url"] if prs else coms[0]["url"] if coms else c["url"] if fechada else None
        if ev:
            forca["Evidência"] = ("txt", ev)
        for k, (kd, v) in quer.items():
            if k not in vals:
                setv(it["id"], k, kd, v)
        for k, (kd, v) in forca.items():
            if vals.get(k) != v and not (kd == "num" and vals.get(k) == float(v)):
                setv(it["id"], k, kd, v)
        if c["assignees"]["totalCount"] == 0:
            muts.append('addAssigneesToAssignable(input:{assignableId:"%s",assigneeIds:["%s"]}){clientMutationId}' % (c["id"], eu))
        if c["labels"]["totalCount"] == 0:
            rot = "tipo:" + re.sub(r"[^a-z]", "", tipo(c["title"]).lower().translate(str.maketrans("çãáéíó", "caaeio")))
            run("label", "create", rot, "--repo", f"{A.dono}/{repo}", "--force", "--color", "5319e7", escrita=True)
            run("issue", "edit", str(c["number"]), "--repo", f"{A.dono}/{repo}", "--add-label", rot, escrita=True)
        if not c.get("milestone"):
            if repo not in milestones:
                ms = json.loads(run("api", f"repos/{A.dono}/{repo}/milestones?state=all&per_page=100") or "[]")
                pick = next((m["title"] for m in ms), None)
                if not pick and A.milestone_padrao:
                    pick = A.milestone_padrao
                    run("api", f"repos/{A.dono}/{repo}/milestones", "-f", f"title={pick}", escrita=True)
                milestones[repo] = pick
            if milestones[repo]:
                run("issue", "edit", str(c["number"]), "--repo", f"{A.dono}/{repo}", "--milestone", milestones[repo], escrita=True)

    if A.gravar:
        for i in range(0, len(muts), 30):
            run("api", "graphql", "-f", "query=mutation{" + " ".join(f"m{j}:{m}" for j, m in enumerate(muts[i:i + 30])) + "}")
            time.sleep(3)
            print("Project", n, min(i + 30, len(muts)), "/", len(muts), flush=True)
    stats[n] = {"itens_no_escopo": escopo, "gravacoes": len(muts), "aplicado": A.gravar}

print(json.dumps(stats, ensure_ascii=False))
if not A.gravar:
    print("Simulação: nada foi gravado. Rode de novo com --gravar para aplicar.")
