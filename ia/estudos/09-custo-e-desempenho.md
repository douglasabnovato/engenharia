# 9 · Custo e desempenho

## Conceito

O custo do trabalho com IA é **tokens × preço do modelo**, somado ao tempo de espera. As alavancas, da que não custa qualidade à que pode custar:

1. **Contexto enxuto:** `CLAUDE.md` curto, leitura por trecho e não do arquivo inteiro, subagente que devolve só a conclusão.
2. **Cache:** o mesmo prefixo relido sai mais barato. Não mudar à toa o começo do contexto.
3. **Esforço certo:** `low` para varredura e tarefa simples, `medium` ou `high` para código, `max` só onde a medida mostra ganho.
4. **Modelo certo por papel:** o mais capaz para revisar e orquestrar; um modelo mais barato (Haiku 5.5) para varreduras e classificação em volume.
5. **Lote:** o que não tem pressa vai em lote, a 50% do preço na API.

Medir sempre por **tarefa concluída**, e não por chamada. Uma chamada barata que precisa de três retrabalhos sai cara.

Fontes: [`05-claude-api-e-agent-sdk.md`](05-claude-api-e-agent-sdk.md) (preços), [`recursos.md`](../recursos.md) (custo por recurso).

## Hoje no ecossistema

- O `explorador` já usa o modelo mais barato; os revisores usam o mais capaz ([`arquitetura-ia.md`](../arquitetura-ia.md), Agentes).
- Os 11 especialistas da F1 herdam o modelo da sessão (`model: inherit`).
- Não há medida de tokens por entrega no relatório do dia.

## Experimento

**Hipótese:** rodar `qa`, `a11y` e `ui` com um modelo mais barato e esforço menor mantém a nota no gabarito e reduz o custo por revisão.

| Passo | Quem |
|---|---|
| 1. Com o gabarito do estudo 7 pronto, rodar cada especialista com o modelo da sessão e anotar nota e tokens | arquitetura de IA |
| 2. Rodar de novo com Sonnet 5.5 e com Haiku 5.5 | arquitetura de IA |
| 3. Ficar com o mais barato que não perde mais de 2 pontos de nota | arquitetura de IA, registro no `CHANGELOG.md` |

Medida contínua: no relatório da semana, tokens por entrega de cada sessão, tirados do uso do app.

## Métrica

- Nota no gabarito por modelo (não pode cair mais de 2 pontos).
- Tokens e custo por revisão.
- Tokens por entrega, por sessão e por semana (só tendência).

## Resultado

A medir. Depende do estudo 7.
