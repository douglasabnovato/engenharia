# 18/11/2026 · Três issues de próximos passos e triagem das demais

## Contexto

A revisão de 18/11/2026, feita só com leitura, contou 41 repositórios, 825 issues e 437 abertas. Das abertas, 183 dependem do responsável. Cerca de 60 parecem desatualizadas: alertas já ligados, sprints já mescladas, principal já protegida.

O responsável pediu:

> "vamos estabelecer uma regra: tres issues em cada repositorio de proximos passos para deixar em aberto. as demais devem ser avaliadas e analisadas e implementadas se vizerem sentido para o nivel do projeto que estiver hoje a nivel de mvp engenharia de software

> as antigas devem ser analisadas comentadas e com informacoes imporatnes"

Ele também respondeu, em 18/11/2026:
- as issues `depende-do-responsavel` "ficam abertas à parte";
- a regra começa por um piloto em 3 repositórios;
- a regra fica registrada por PR neste repositório.

## Decisões

| # | Decisão | Por quê |
|---|---|---|
| P1 | Cada repositório fica com **exatamente 3 issues abertas com o rótulo `proximo-passo`**. São de código ou de produto, seguem o [modelo](../processo/modelo-issue.md) e cabem no nível atual do projeto | Pedido do responsável. O roteiro do repositório fica visível sem uma fila longa |
| P2 | As 3 são escolhidas entre as abertas que mais avançam o projeto no nível em que ele está: primeiro as que melhoram o fluxo principal e os critérios do `MVP.md`, depois as mais recentes. Se não houver 3 boas, cria-se a que falta, no modelo | "Algumas issues são novas e são para ficar em aberto" |
| P3 | As issues `depende-do-responsavel` **não contam** nas 3 e ficam abertas. Cada uma recebe um comentário com a situação conferida hoje e o passo a passo. Se a evidência mostrar que já está resolvida, o comentário diz isso e pede o fechamento. O agente não fecha | Resposta do responsável; [modelo de issue](../processo/modelo-issue.md): "Nunca fechar issue que depende do responsável" |
| P4 | Cada uma das demais abertas recebe uma destas quatro saídas, com comentário: **(a) já feita:** evidência, e fecha (se estiver só na sprint, fecha depois do merge na principal); **(b) implementar:** faz sentido no nível atual e cabe no ciclo; vai por `feature` → sprint e fecha depois do merge na principal; **(c) não planejada:** fora do nível, obsoleta ou duplicada; fecha com o motivo; **(d) vira uma das 3** de P1 | "Avaliadas, analisadas e implementadas se fizerem sentido para o nível" |
| P5 | O nível vem do topo do `docs/MVP.md`. O que não melhora nenhum critério aplicável do nível não é implementado no ciclo (ex.: funcionalidade nova num N1) | [`padroes.md`](../arquitetura/padroes.md): "não simular produto em projeto de curso" |
| P6 | **Issue antiga** é a criada há mais de 7 dias. Antes de qualquer saída, ela recebe um comentário de análise: situação atual com comando, data e resultado; o que mudou desde a abertura; links para PRs e issues relacionados; e a decisão (P3 ou P4) | "As antigas devem ser analisadas, comentadas e com informações importantes" |
| P7 | Comentários em português, curtos, sem dados pessoais, terminando com `<sub>por douglas ciborgue</sub>` | Regra de comentários do portfólio |
| P8 | Ordem: piloto em 3 repositórios (um N1, um N2, um N3). O responsável revisa. Depois, os outros 38 em lotes | Resposta do responsável |

## Formato do comentário de análise

```markdown
**Análise de 18/11/2026**
- Situação hoje: <o que foi conferido> (`<comando>` → <resultado>)
- Mudou desde a abertura: <PRs, merges, decisões>
- Decisão: <já feita | implementar | não planejada | próximo passo | depende do responsável> — <motivo em uma frase>
- Próximo passo: <o que acontece e de quem>

<sub>por douglas ciborgue</sub>
```

## Opções descartadas

- **Fechar todas as issues sem as 3:** perderia o registro do que falta e contraria P3.
- **Manter todas abertas e só comentar:** a fila continua longa, e o Project não mostra os próximos passos.

## Resultado

O resultado do piloto entra aqui, com a contagem antes e depois por repositório.
