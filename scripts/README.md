# Scripts

Ferramentas do coordenador e do responsável. Todas usam o GitHub CLI autenticado (`gh auth status`). O caminho do `gh` vem da opção `--gh`, da variável `GH` ou do `PATH`. No Windows, rode com `PYTHONUTF8=1` para não corromper acentos.

| Script | O que faz | Escreve no GitHub? | Quem roda |
|---|---|---|---|
| [`estado.py`](estado.py) | Lê o estado de cada repositório: critérios e "Finalizado" do `MVP.md`, seção do ciclo no plano, PRs abertos e o CI de cada um, CI da branch, issues com 3+ critérios, site respondendo | **Não** | Coordenador, no início e no fim de cada lote |
| [`relatorio.py`](relatorio.py) | Gera um HTML com o JSON do `estado.py` e o índice do ciclo | **Não** (só um arquivo local) | Coordenador |
| [`preencher-project.py`](preencher-project.py) | Preenche os campos dos itens do Project a partir das issues; põe responsável, rótulo de tipo e milestone quando faltam | Sim, **só com `--gravar`**. Sem a opção, simula | Coordenador, no fim de cada lote |
| [`hooks/bloquear_proibidos.py`](hooks/bloquear_proibidos.py) | Hook `PreToolUse` do Claude Code: recusa force push, `--no-verify`, push na principal, apagar branch remota e reescrever histórico. Testes: `python -m unittest discover -s scripts/hooks` | **Não** | O Claude Code, a cada comando, depois que o responsável liga ([`ia/hooks.md`](../ia/hooks.md)) |
| [`configurar-responsavel.sh`](configurar-responsavel.sh) | Liga o Pages ou cria o ruleset "principal-protegida" | Sim (configuração do repositório) | **Só o responsável** |

Nenhum script apaga nada: não remove issues, itens, rótulos, branches nem configurações. Os que escrevem só acrescentam ou atualizam campos, e são idempotentes (rodar duas vezes não duplica).

## Exemplos

```bash
# Estado da sprint de 21 repositórios, procurando a seção do ciclo
PYTHONUTF8=1 python scripts/estado.py --dono <dono> --repos aircnc,movies,proffy \
  --branch developer/sprint-2026-11-12 --ciclo "Ciclo de 09/11/2026" --saida estado.json

# Todos os repositórios, menos os fora do escopo
PYTHONUTF8=1 python scripts/estado.py --dono <dono> --excluir repo-a,repo-b

# Relatório HTML
PYTHONUTF8=1 python scripts/relatorio.py --estado estado.json --saida relatorio.html --notas notas.json

# Project: primeiro simula, depois grava
PYTHONUTF8=1 python scripts/preencher-project.py --dono <dono> --projects 2 --niveis niveis.json
PYTHONUTF8=1 python scripts/preencher-project.py --dono <dono> --projects 2 --niveis niveis.json --gravar

# Responsável: ligar Pages e proteger a principal
DONO=<dono> bash scripts/configurar-responsavel.sh pages repo-a repo-b
DONO=<dono> bash scripts/configurar-responsavel.sh proteger repo-a repo-b
```

## Formatos

`niveis.json` (para `preencher-project.py`):
```json
{ "aircnc": "Estudo", "movies": "Piloto", "components": "Produto" }
```

`notas.json` (para `relatorio.py`):
```json
{ "aircnc": { "feito": "CI na sprint; testes de falha de rede", "falta": "você: publicar (#88)" } }
```

## Leitura do `MVP.md`

O `estado.py` procura no `MVP.md` as linhas `**Resumo:** X de Y aplicáveis atendidos` e `**Finalizado:** sim|não`. Fora desse formato, o repositório aparece com `-` ou `?`.
