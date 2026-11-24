# Medida MVP por repositório · rascunho (23/11/2026)

**Rascunho para o responsável aprovar [A CONFIRMAR com o responsável].** Ainda não vale como regra, e o painel não muda até a aprovação.

## Por que

Hoje a coluna "MVP" do painel conta os critérios do `docs/MVP.md` de cada repositório. A régua varia: uns têm 10 critérios e outros têm 12. Por isso "9 de 10" e "9 de 12" não se comparam. A situação "completo" do painel (`gerar-painel.mjs`) só olha Finalizado e link.

A proposta é uma régua única de 4 critérios, iguais para todos os repositórios, que dá para conferir pela API.

## Os 4 critérios

| # | Critério | Como conferir | Fonte |
|---|---|---|---|
| C1 | **MVP escrito:** `docs/MVP.md` com a frase do MVP e os critérios | o arquivo existe e tem a seção `## Critérios` | API do GitHub (conteúdo) |
| C2 | **No ar:** o link do About responde 200 ou 30x | `painel.sh`, como já faz | link do About |
| C3 | **CI verde na principal:** o último workflow da `main` passou | `gh run list --branch main --limit 1` | Actions |
| C4 | **README vitrine:** o que é, como rodar e o link | as 3 seções no README | API do GitHub (conteúdo) |

- **Leitura:** 4 de 4 é "MVP"; 2 ou 3 é "parcial"; 0 ou 1 é "sem MVP".
- **Exceções:**
  - o repositório de perfil (`douglasabnovato`) não precisa do C2, como já é no painel;
  - repositório sem CI conta o C3 como não atendido, para virar issue.

## Perguntas para o responsável

1. Os 4 critérios servem, ou algum entra no lugar de outro (por exemplo, Release v1.0.0)?
2. O denominador são os 41 repositórios da R24? O número ainda está "[A CONFIRMAR]" (o `figma-design` dentro ou fora).
3. A régua antiga (10 ou 12 critérios do `docs/MVP.md`) fica como detalhe dentro do C1, ou sai do painel?

Depois do ok, o Líder de TODOS ajusta `orquestrador/scripts/painel.sh` e `gerar-painel.mjs`, que são dele e ficam fora do GitHub.
