# 1 · Contexto e memória

## Conceito

O Claude Code começa cada sessão só com o que é carregado:
- o `CLAUDE.md` da pasta aberta e das pastas acima dela, com arquivos importados por `@caminho`;
- a memória local da sessão (`~/.claude/projects/<pasta>/memory/`, com o índice `MEMORY.md`).

Quando a conversa enche, ela é **resumida** (compactação), e o detalhe que só estava na conversa se perde.

Três regras práticas:
- O que vale para todos vai para um arquivo carregado sempre, e não para a memória de uma sessão (R17).
- O que muda todo dia (estado, fila, decisões) vai para um arquivo no repositório (`ESTADO.md`, `docs/MVP.md`, relatório do dia), e não para a conversa.
- O `CLAUDE.md` deve ser curto e apontar para os documentos, em vez de copiá-los.

Fontes: [memória do Claude Code](https://code.claude.com/docs/en/memory), [`arquitetura-ia.md`](../arquitetura-ia.md) (camadas 1 e 3).

## Hoje no ecossistema

| Fato | Evidência |
|---|---|
| Nenhuma das 4 pastas raiz tem `CLAUDE.md` | [`ambientes/README.md`](../ambientes/README.md), 18/11/2026 |
| O LearnTech tem `CLAUDE.md` em 5 de 5 repositórios, com seções repetidas | [`ambientes/learntech.md`](../ambientes/learntech.md) |
| O orquestrador quebrou a R3 e a R4 porque as regras não estavam carregadas | [pós-incidente de 20/11](../../decisoes/2026-11-20-governanca-ia.md) |
| Estado em quatro arquivos que se sobrepõem no LearnTech | `ESTADO.md`, `ESTADO-DO-PROJETO.md`, `MVP.md`, `PROXIMOS-PASSOS.md` |

## Experimento

**Hipótese:** com o `CLAUDE.md` raiz carregado (F2), as sessões quebram menos regras e perguntam menos o que já está escrito.

| Passo | Quem |
|---|---|
| 1. Linha de base: contar, nos relatórios de 14 dias, as regras quebradas e as perguntas cuja resposta já estava no `engenharia` | arquitetura de IA |
| 2. Instalar o `CLAUDE.md` raiz nas 4 pastas (plugin da F2) | responsável |
| 3. Medir de novo por 14 dias | arquitetura de IA |

## Métrica

- Regras quebradas por semana (linha de base: 1 incidente grave em 20/11, ver o pós-incidente).
- Perguntas ao responsável cuja resposta estava escrita.
- Tamanho do contexto inicial de cada sessão (tokens do `CLAUDE.md` e dos importados): ficar abaixo de 5 mil.

## Resultado

A medir.
