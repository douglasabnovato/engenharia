# 7 · Avaliação: gabaritos e evals

## Conceito

Sem medida, não se sabe se uma mudança de prompt, de modelo ou de esforço melhorou ou piorou. Um **gabarito** (eval) é um conjunto de casos com a resposta esperada e um jeito de dar nota.

| Parte | Boa prática |
|---|---|
| Casos | Vêm do trabalho real; cobrem o comum, a borda e o erro já visto. Começar com 20 |
| Nota | Exata quando dá (campo certo ou errado); rubrica com critérios curtos quando não dá |
| Juiz | Quando a nota é dada por outro modelo, conferir uma amostra à mão |
| Separação | Casos de ajuste e casos de teste separados, para não "decorar" o gabarito |
| Regra | Mudança de prompt ou de modelo só entra se a nota de teste não cair |

Fontes: [`ciclo-evolutivo.md`](../../processo/ciclo-evolutivo.md), seção 5; [`avaliacoes/`](../avaliacoes/README.md).

## Hoje no ecossistema

- **Triador do learntech-content:** `npm run triador:gabarito`, 4 rodadas, 76% em direitos e 67% em destinos. A meta para sair de AU0 é 85% (`learntech-content/docs/processo/agentes.md`).
- **Especialistas da F1 e revisores de conteúdo:** ainda sem gabarito. O formato está em [`avaliacoes/`](../avaliacoes/README.md).
- **Régua do MVP:** é um gabarito do repositório, não do agente. "Atende" exige comando, data e resultado.

## Experimento

**Hipótese:** com 20 casos reais por agente, dá para decidir pelo número se o agente sobe de AU0 e se uma mudança de prompt ajudou.

| Passo | Quem |
|---|---|
| 1. Montar 20 casos para o `qa` e o `a11y`, a partir de PRs antigos com defeito conhecido (o defeito é a resposta esperada) | arquitetura de IA, com leitura dos repositórios |
| 2. Rodar os dois agentes e dar a nota | arquitetura de IA |
| 3. Ajustar o prompt uma vez e rodar de novo nos casos de teste | arquitetura de IA |
| 4. Repetir para os revisores de conteúdo com casos do LearnTech | repositórios LearnTech fornece os casos |

## Métrica

- Acerto por agente: meta ≥ 80% para uso e 85% para subir de nível.
- Diferença de nota antes e depois de cada mudança de prompt.

## Resultado

A medir.
