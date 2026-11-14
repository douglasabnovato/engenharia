# Fluxo Git

```
feature/AAAA-MM-DD  →  developer/sprint-<próxima quinta>  →  principal (main ou master)
   (um dia de trabalho)      (uma semana)                    (produção)
```

## Branches

| Branch | Nasce de | Nome | Vida |
|---|---|---|---|
| Feature | a sprint | `feature/` + data de hoje (`feature/2026-11-09`) | Um dia ou um ciclo de agente |
| Sprint | a principal | `developer/sprint-` + data da próxima quinta-feira (`developer/sprint-2026-11-12`) | Até o merge na principal |
| Principal | — | a do repositório (`main` ou `master`) | Permanente, protegida |

- Se a sprint não existir, criar a partir da principal. Se estiver atrás da principal, atualizar por PR ou avanço simples (fast-forward), nunca com force.
- Exceção de nome: num repositório cujas regras não aceitam `/`, usar hífen (`developer-sprint-2026-11-12`). Registrar a exceção no brief.
- Ciclo curto sobre trabalho que ainda não foi para a principal: a feature nasce da sprint, e o trabalho entra no PR sprint → principal que já está aberto.

## Commits

- Pequenos, em português, no padrão do repositório (`feat:`, `fix:`, `docs:`, `test:`, `ci:`...).
- Push a cada commit.
- Lint, testes e build antes do push.
- Commits feitos com IA terminam com a linha `Co-Authored-By` do agente.
- Nunca: force push (nem `--force-with-lease`), reescrever histórico, `--no-verify`.

## Quem pode mesclar o quê

| PR | Quem mescla | Condição |
|---|---|---|
| feature → sprint | O agente, uma tentativa | CI verde. Se a permissão negar, o PR fica aberto com `revisao-responsavel` |
| Dependabot (patch ou minor) → principal | O responsável (o merge pelo agente foi negado) | CI verde |
| Dependabot (major) | O responsável | Depois de revisar a migração |
| sprint → principal | **Só o responsável** | CI verde e revisão. O agente abre com `revisao-responsavel` e deixa aberto |

CI vermelho ou ausente bloqueia o merge pelo agente. Num repositório sem CI, o agente cola no PR a saída do build e dos testes, deixa o PR aberto com `revisao-responsavel` e abre a issue para criar o CI. (Regra esclarecida em 13/11/2026, engenharia#21.)

## Principal protegida

Sem proteção, um push direto publica sem CI; por isso o critério 10 fica "Parcial" até a principal ter um ruleset. Criar o ruleset é do responsável (Settings → Rules → Rulesets, ou o script [`scripts/configurar-responsavel.sh`](../scripts/configurar-responsavel.sh)).

Exemplo: o ruleset `principal-protegida` do `aircnc` (lido pela API em 09/11/2026):

```json
{
  "name": "principal-protegida",
  "target": "branch",
  "enforcement": "active",
  "conditions": { "ref_name": { "include": ["~DEFAULT_BRANCH"], "exclude": [] } },
  "rules": [
    { "type": "deletion" },
    { "type": "non_fast_forward" },
    { "type": "pull_request", "parameters": {
        "required_approving_review_count": 0,
        "dismiss_stale_reviews_on_push": false,
        "require_code_owner_review": false,
        "require_last_push_approval": false,
        "required_review_thread_resolution": false } },
    { "type": "required_status_checks", "parameters": {
        "strict_required_status_checks_policy": false,
        "required_status_checks": [
          { "context": "backend" }, { "context": "frontend" },
          { "context": "mobile" }, { "context": "e2e" } ] } }
  ]
}
```

O que cada regra faz:
- `deletion`: ninguém apaga a principal.
- `non_fast_forward`: ninguém faz force push.
- `pull_request` com 0 aprovações: tudo entra por PR; o responsável continua mesclando os próprios PRs.
- `required_status_checks`: o merge só libera com os jobs do CI verdes. Os nomes são os dos jobs do workflow de cada repositório.

Para conferir: `gh api repos/<dono>/<repo>/rulesets` (lista) e `gh api repos/<dono>/<repo>/rulesets/<id>` (detalhe).

## Rótulos de fluxo

| Rótulo | Uso |
|---|---|
| `revisao-responsavel` | PR que espera o merge ou a revisão do responsável |
| `depende-do-responsavel` | Issue que só o responsável resolve (conta, senha, configuração, decisão) |
