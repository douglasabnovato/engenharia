"""Gera um relatório HTML do portfólio a partir do JSON do estado.py. Só lê arquivos locais.

Uso:
  python scripts/relatorio.py --estado estado.json --saida relatorio.html [--notas notas.json] [--titulo "..."]

notas.json (opcional): {"<repo>": {"feito": "o que entrou", "falta": "o que falta e de quem"}}

Índice do ciclo (0 a 100): 60% critérios aplicáveis atendidos, 20% repositórios com 5+ issues
abertas de 3+ critérios, 20% repositórios com a seção do ciclo no plano.
"""
import argparse
import datetime
import html
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("--estado", required=True)
ap.add_argument("--saida", required=True)
ap.add_argument("--notas", default="")
ap.add_argument("--titulo", default="Relatório do portfólio · " + datetime.date.today().strftime("%d/%m/%Y"))
A = ap.parse_args()

D = {d["repo"]: d for d in json.load(open(A.estado, encoding="utf-8"))}
N = json.load(open(A.notas, encoding="utf-8")) if A.notas else {}
e = lambda s: html.escape(str(s))  # noqa: E731

CSS = """<style>
:root{--bg:#f6f7f8;--paper:#fff;--ink:#17202a;--muted:#56626e;--rule:#d9dee3;--ok:#1e6b3a;--warn:#8a5a12;--no:#9b2c2c}
@media (prefers-color-scheme:dark){:root{--bg:#12171c;--paper:#192027;--ink:#e5e9ed;--muted:#9aa6b1;--rule:#2d3740;--ok:#7fd19b;--warn:#e2b260;--no:#f19a9a}}
body{background:var(--bg);color:var(--ink);font:15px/1.55 system-ui,sans-serif;margin:0}
.wrap{max-width:1100px;margin:0 auto;padding:32px 16px;display:grid;gap:28px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px}
.stat{background:var(--paper);border:1px solid var(--rule);border-radius:6px;padding:12px}.stat b{font-size:1.6rem;display:block}
.table{overflow-x:auto;border:1px solid var(--rule);border-radius:6px;background:var(--paper)}
table{border-collapse:collapse;width:100%}th,td{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:1px solid var(--rule)}
th{font-size:.75rem;text-transform:uppercase;color:var(--muted)}a{color:inherit}
.ok{color:var(--ok)}.warn{color:var(--warn)}.no{color:var(--no)}td.num{font-variant-numeric:tabular-nums;white-space:nowrap}
</style>"""


def linha(r):
    d, n = D[r], N.get(r, {})
    a, t = d["resumo"] or (0, 0)
    fin = '<span class="ok">sim</span>' if d["finalizado"] == "sim" else '<span class="warn">não</span>'
    site = f'<a href="{e(d["home"] or d["pages"])}">no ar</a>' if d["http"] == "200" else e(d["http"])
    prs = ", ".join(f'#{p["n"]} ({e(p["ci"])})' for p in d["prs"]) or "-"
    return (f'<tr><td><a href="https://github.com/{e(r)}">{e(r)}</a></td><td>{e(n.get("feito", ""))}</td>'
            f'<td class="num">{a} de {t}</td><td>{fin}</td><td class="num">{d["com3"]}</td><td>{site}</td>'
            f'<td>{prs}</td><td>{e(n.get("falta", ""))}</td></tr>')


rs = sorted(D)
fin = [r for r in rs if D[r]["finalizado"] == "sim"]
nfin = [r for r in rs if r not in fin]
a = sum((D[r]["resumo"] or (0, 0))[0] for r in rs)
t = sum((D[r]["resumo"] or (0, 0))[1] for r in rs) or 1
idx = round(100 * (0.6 * a / t + 0.2 * sum(D[r]["com3"] >= 5 for r in rs) / len(rs)
                   + 0.2 * sum(D[r]["ciclo"] for r in rs) / len(rs)), 1)
TH = ("<thead><tr><th>Projeto</th><th>O que entrou</th><th>Critérios</th><th>Finalizado</th>"
      "<th>Issues 3+</th><th>Site</th><th>PRs abertos</th><th>O que falta e de quem</th></tr></thead>")

page = f"""<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(A.titulo)}</title>{CSS}<div class="wrap">
<header><h1>{e(A.titulo)}</h1><p>Lido pela API do GitHub. "No ar" = o endereço respondeu HTTP 200; isso não prova que é a versão atual.</p></header>
<div class="stats">
 <div class="stat"><b>{len(fin)}</b>finalizados de {len(rs)}</div>
 <div class="stat"><b>{a} de {t}</b>critérios aplicáveis</div>
 <div class="stat"><b>{sum(D[r]['com3'] for r in rs)}</b>issues abertas com 3+ critérios</div>
 <div class="stat"><b>{sum(D[r]['http'] == '200' for r in rs)}</b>sites no ar</div>
 <div class="stat"><b>{idx}</b>índice do ciclo (0 a 100)</div>
</div>
<section><h2>Finalizados ({len(fin)})</h2><div class="table"><table>{TH}<tbody>{''.join(linha(r) for r in fin)}</tbody></table></div></section>
<section><h2>Não finalizados ({len(nfin)})</h2><div class="table"><table>{TH}<tbody>{''.join(linha(r) for r in nfin)}</tbody></table></div></section>
</div></html>"""

with open(A.saida, "w", encoding="utf-8") as f:
    f.write(page)
print(f"{len(fin)} finalizados, {len(nfin)} não, índice {idx} -> {A.saida}")
