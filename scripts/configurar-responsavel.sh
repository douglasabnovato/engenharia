#!/usr/bin/env bash
# Configurações que só o responsável faz. Leia antes e rode você mesmo, no Git Bash ou num terminal Unix:
#   DONO=<dono> bash scripts/configurar-responsavel.sh pages    <repo> [<repo>...]
#   DONO=<dono> bash scripts/configurar-responsavel.sh proteger <repo> [<repo>...]
#
#   pages    -> liga o GitHub Pages com fonte "GitHub Actions" e roda de novo o último workflow da principal
#   proteger -> cria o ruleset "principal-protegida": proíbe apagar e force push na branch padrão e exige PR
#               (0 aprovações: você continua mesclando os próprios PRs)
#
# Os agentes escrevem este script, mas não o executam: mudar configuração do repositório é do responsável.
# Nada aqui apaga: se o Pages ou o ruleset já existir, a chamada falha e o script segue.
# Caminho do gh: variável GH ou o gh do PATH.
set -euo pipefail
GH="${GH:-gh}"
DONO="${DONO:?defina DONO=<usuario ou organizacao>}"
ACAO="${1:-}"; shift || true
[ "$#" -gt 0 ] || { echo "uso: DONO=<dono> bash $0 pages|proteger <repo> [<repo>...]"; exit 1; }

case "$ACAO" in
  pages)
    for r in "$@"; do
      echo "== $r"
      "$GH" api -X POST "repos/$DONO/$r/pages" -f build_type=workflow >/dev/null && echo "Pages ligado" || echo "falhou (talvez já ligado)"
      b=$("$GH" repo view "$DONO/$r" --json defaultBranchRef --jq .defaultBranchRef.name)
      id=$("$GH" run list --repo "$DONO/$r" --branch "$b" --limit 1 --json databaseId --jq '.[0].databaseId')
      [ -n "$id" ] && "$GH" run rerun "$id" --repo "$DONO/$r" || echo "sem workflow para rodar de novo"
    done ;;
  proteger)
    for r in "$@"; do
      echo "== $r"
      "$GH" api -X POST "repos/$DONO/$r/rulesets" --input - >/dev/null <<'JSON' && echo "protegida" || echo "falhou (talvez já exista)"
{
  "name": "principal-protegida",
  "target": "branch",
  "enforcement": "active",
  "conditions": { "ref_name": { "include": ["~DEFAULT_BRANCH"], "exclude": [] } },
  "rules": [
    { "type": "deletion" },
    { "type": "non_fast_forward" },
    { "type": "pull_request", "parameters": {
        "required_approving_review_count": 0, "dismiss_stale_reviews_on_push": false,
        "require_code_owner_review": false, "require_last_push_approval": false,
        "required_review_thread_resolution": false } }
  ]
}
JSON
    done
    echo "Para exigir o CI verde, acrescente no painel (Rulesets -> principal-protegida) a regra"
    echo "'Require status checks to pass' com os nomes dos jobs do workflow de cada repositório." ;;
  *) echo "uso: DONO=<dono> bash $0 pages|proteger <repo> [<repo>...]"; exit 1 ;;
esac
