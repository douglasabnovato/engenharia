# 6 · Engenharia de prompt e de contexto

## Conceito

**Engenharia de prompt** é escrever a instrução. **Engenharia de contexto** é decidir *o que* entra na janela do modelo, *em que ordem* e *quando sai*. Nos modelos atuais, a segunda pesa mais.

Princípios que valem para `CLAUDE.md`, skills, agentes e briefs:
1. **Diga o objetivo e o porquê, não só a regra.** O modelo generaliza melhor quando entende o motivo.
2. **Menos é mais.** Instrução escrita para modelos antigos ("SEMPRE", "NUNCA", repetições, CAIXA ALTA) hoje deixa o modelo rígido demais. Cada linha deve mudar um comportamento.
3. **Aponte, não copie.** O `CLAUDE.md` cita o arquivo da regra. Duas cópias da mesma regra acabam divergindo.
4. **O brief é todo o contexto do subagente.** Ele precisa do objetivo, do que já foi descartado e do formato da resposta. Mande as fontes, não a sua conclusão.
5. **Estado em arquivo.** O que precisa sobreviver à compactação vai para um arquivo.

Fontes: [boas práticas de prompt](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview), [`recursos.md`](../recursos.md) (armadilhas).

## Hoje no ecossistema

| Fato | Evidência |
|---|---|
| Os 4 `CLAUDE.md` dos sites do LearnTech repetem as seções Privacidade e Git quase linha a linha | [`ambientes/learntech.md`](../ambientes/learntech.md) |
| O `modelo-issue.md` e a skill `issue-no-modelo` se contradiziam sobre o Project | corrigido na F1 ([decisão G7](../../decisoes/2026-11-20-governanca-ia.md)) |
| Briefs de agente com modelo pronto | [`briefs/`](../briefs/) |

## Experimento

**Hipótese:** uma auditoria dos `CLAUDE.md` do LearnTech, procurando instruções datadas, contradições e cópias, reduz o tamanho sem perder comportamento.

| Passo | Quem |
|---|---|
| 1. Rodar a auditoria (`/claude-api prompt-audit`) sobre os 5 `CLAUDE.md` e as skills e agentes do learntech-content: só relatório e diff proposto | arquitetura de IA, só leitura |
| 2. Passar o relatório à dona | arquitetura de IA |
| 3. Aplicar o que o responsável aprovar | repositórios LearnTech |
| 4. Medir antes e depois: linhas, tokens e as mesmas 5 tarefas de teste | repositórios LearnTech |

## Métrica

- Tokens dos `CLAUDE.md` somados: reduzir pelo menos 30%.
- Contradições e cópias encontradas e resolvidas.
- As mesmas 5 tarefas, antes e depois, sem regra quebrada.

## Resultado

A medir.
