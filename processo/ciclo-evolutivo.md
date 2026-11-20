# Ciclo evolutivo, qualidade e performance

Como o portfólio melhora sozinho, semana a semana: três ciclos encaixados, portões de qualidade por PR, metas do processo e a avaliação da própria IA.

Pedido do responsável em 20/11/2026: "ajuste atualize e garanta que tenhamos um processo ciclico evolutivo e qualidade e performance". Origem: revisão do Líder de TODOS de 20/11/2026, seção 6a.

## 1. Três ciclos (PDCA)

| Ciclo | Planejar | Fazer | Checar | Agir (a melhoria) |
|---|---|---|---|---|
| **Diário** | revisão D-1 às 6h30 por sessão dona; plano às 6h50 | sessões donas, no máximo 3 itens em andamento por sessão | ponto de controle às 12h30; fechamento às 18h30 | o fechamento registra **1 aprendizado** do dia, com causa e ação |
| **Semanal** (sexta, 17h) | escolher de 1 a 3 melhorias (kaizen) pelas métricas da seção 4 | a arquitetura de IA transforma cada melhoria numa issue no `engenharia` | métricas da semana contra a anterior | a melhoria entra como regra, skill, agente ou hook, por PR, com uma linha no [`CHANGELOG.md`](../CHANGELOG.md) |
| **Mensal** (última sexta) | auditoria N1/N2/N3 por disciplina e repositório ([`disciplinas.md`](../arquitetura/disciplinas.md)) | as sessões donas sobem um nível onde falta | placar de nível por ambiente | ajustar as metas e o padrão mínimo de `disciplinas.md` |

Os horários são os da R7 de [`orquestracao.md`](../ia/orquestracao.md). As tarefas agendadas só rodam com o app aberto e o computador acordado.

**De onde vêm as melhorias:** das propostas do modo melhoria (R21). Toda sessão sem tarefa manda uma proposta ao LIDER, que as pontua pela matriz durante a semana. Na sexta, as de maior nota com o ok do responsável viram as melhorias da semana. Assim, o ciclo semanal não depende de alguém lembrar o que melhorar.

## 2. Pós-incidente sem culpa

Todo incidente gera um registro em [`decisoes/`](../decisoes/) com:
1. **Fato:** o que aconteceu, com números e horários.
2. **Causa raiz:** pelos 5 porquês. A pergunta é "por que o processo deixou?", e não "quem errou?".
3. **Ação:** o que muda e quem faz.

**Regra de ouro:** regra crítica que falhou uma vez vira **hook ou teste**, não lembrete. Exemplo: o orquestrador quebrou a R3 e a R4 em 20/11/2026 ([decisão](../decisoes/2026-11-20-governanca-ia.md)). A ação é a R18 agora e um hook na F2.

## 3. Portões de qualidade por PR

Somam à [`definicao-de-pronto.md`](definicao-de-pronto.md). O PR só vai para a sprint quando passa nos portões do nível do repositório.

| # | Portão | N1 | N2 | N3 |
|---|---|---|---|---|
| 1 | CI verde: lint, testes e build (R14) | sim | sim | sim |
| 2 | e2e do fluxo principal; axe sem violação séria | sim | sim | sim |
| 3 | Orçamento de performance (abaixo) | — | resultado no corpo do PR | Lighthouse CI falha o PR |
| 4 | Segurança mínima do nível ([`disciplinas.md`](../arquitetura/disciplinas.md), SecOps) | alertas | + segredos e audit | + CodeQL |
| 5 | Revisão do agente especialista de cada disciplina tocada (R19) | — | sim | sim |
| 6 | `docs/MVP.md` com comando, data e resultado; link no ar quando houver deploy | sim | sim | sim |

### Orçamento de performance

No celular, mediana de 3 execuções do Lighthouse:

| Métrica | Limite |
|---|---|
| Performance do Lighthouse | ≥ 90 |
| LCP | < 2,5 s |
| CLS | < 0,1 |
| TBT | < 200 ms |
| JavaScript inicial | ≤ 200 KB gzip |

Um repositório pode ter um orçamento mais apertado, e aí vale o dele. Exemplo: o bootcamps usa 100 KB gzip de JS inicial.

## 4. Métricas do processo

Vão para o relatório da semana, com a tendência.

| Métrica | Meta inicial | Fonte |
|---|---|---|
| Vazão: itens concluídos por semana | subir semana a semana | PRs mesclados e issues fechadas |
| Tempo de entrega, da issue aberta ao merge | mediana ≤ 3 dias | `gh` |
| Itens parados há mais de 4 horas | 0 sem dono (R11) | Project 2 |
| Itens esperando o responsável | abaixo de 30% do total | rótulo `revisao-responsavel` |
| CI verde na primeira execução | ≥ 85% | Actions |
| Falha de mudança: merge que precisou de correção em 48 horas | ≤ 15% | commits `fix` |
| Repositórios com "Finalizado: sim" e link no ar | subir até todos | `docs/MVP.md` |
| Repositórios dentro do orçamento de performance | subir mês a mês | relatórios de Lighthouse |
| Acerto dos agentes no gabarito | ≥ 80% | gabaritos (seção 5) |

## 5. Evolução da própria IA

- **Gabarito e nota.** Cada agente e cada skill tem um gabarito: casos com a resposta esperada. Uma mudança de prompt só entra se a nota não cair. O modelo é o `npm run triador:gabarito` do learntech-content.
- **Autonomia por nota.** Os agentes começam propondo (AU0). Sobem de nível com 85% de acerto em 20 casos e descem se a amostra revisada cair abaixo de 80%, como em `learntech-content/docs/processo/agentes.md`.
- **Regras com versão.** Toda mudança de regra, skill, agente ou hook tem uma linha no [`CHANGELOG.md`](../CHANGELOG.md) e é citada no relatório do dia.
- **Memória que sobe.** Uma vez por mês, a revisão das memórias leva para o `engenharia` o que vale para todos (R17).
