# 8 · Metodologias com IA

## Conceito

A IA não substitui o método. Ela amplifica o método que existe, seja bom ou ruim.

| Metodologia | Como fica com IA | Nosso artefato |
|---|---|---|
| **Especificação primeiro** | A issue com critérios verificáveis é o contrato. O agente implementa contra ela, e o revisor confere contra ela | [`modelo-issue.md`](../../processo/modelo-issue.md) |
| **TDD com IA** | Primeiro o teste que falha (escrito ou revisado por quem conhece a regra), depois o código. O teste impede o agente de "passar" sem resolver | [`definicao-de-pronto.md`](../../processo/definicao-de-pronto.md) |
| **PDCA** | Planejar, fazer, checar e agir, em ciclos curtos, com métrica antes e depois | [`ciclo-evolutivo.md`](../../processo/ciclo-evolutivo.md) |
| **Lean** | Limite de trabalho em andamento, eliminar espera e retrabalho, medir o fluxo | R7a, limite de 3 itens em andamento, lead time |
| **Revisão independente** | Quem revisa não viu a implementação e recebe o diff, não a conclusão | agente `revisor-independente` |

## Hoje no ecossistema

- A issue no modelo existe desde novembro. Antes dele, 117 de 179 issues iniciais foram fechadas como não planejadas ([`modelo-issue.md`](../../processo/modelo-issue.md)).
- Playwright em 37 de 41 repositórios do GitHub e unitário em 27 ([`disciplinas.md`](../../arquitetura/disciplinas.md)).
- Não há registro de qual PR nasceu de um teste que falhava primeiro.

## Experimento

**Hipótese:** em correções de defeito, escrever primeiro o teste que reproduz o defeito reduz a falha de mudança.

| Passo | Quem |
|---|---|
| 1. Escolher 10 issues de defeito abertas em repositórios N2 do GitHub | repositórios GitHub |
| 2. Em 5, o primeiro commit é só o teste que falha (com o run vermelho como evidência); depois a correção. Nas outras 5, o fluxo de hoje | repositórios GitHub |
| 3. Comparar: commits `fix` nas 48 horas seguintes, CI verde de primeira, tempo até o merge | arquitetura de IA |

## Métrica

- Falha de mudança nos dois grupos (meta da casa: ≤ 15%).
- CI verde na primeira execução (meta: ≥ 85%).
- Lead time (meta: mediana ≤ 3 dias).

## Resultado

A medir. Amostra pequena: serve para decidir se vale ampliar, não para provar.
