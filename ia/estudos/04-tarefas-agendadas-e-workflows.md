# 4 · Tarefas agendadas e workflows

## Conceito

- **Tarefa agendada:** um prompt que o app dispara num horário fixo, numa sessão nova. É bom para rotina (revisão D-1, fechamento). Só roda com o app aberto e o computador acordado, e pede as permissões na primeira execução.
- **Workflow com vários agentes:** um script que orquestra muitos subagentes em fases (revisar, verificar, consolidar). É poderoso e caro. Só roda com o pedido explícito do responsável.
- **Agendamento na nuvem** (rotinas): roda sem o computador ligado, mas sem acesso às pastas locais.

Regra de custo: do mais simples ao mais caro. Primeiro a própria sessão, depois um subagente, depois uma tarefa agendada, e só então um workflow.

Fontes: [tarefas agendadas](https://code.claude.com/docs/en/scheduled-tasks), [`recursos.md`](../recursos.md), [`orquestracao.md`](../orquestracao.md) (R7).

## Hoje no ecossistema

- A R7 descreve 7 tarefas. Nesta máquina existem só `abertura-do-dia-lider` e `fechamento-do-dia-lider` (inferido · confirmar; [`arquitetura-ia.md`](../arquitetura-ia.md), seção Automação).
- Até 12/11/2026, nenhum workflow com vários agentes tinha sido usado ([`recursos.md`](../recursos.md)).

## Experimento

**Hipótese:** com as revisões D-1 das 6h30 rodando de fato, o plano das 6h50 sai completo sem o Líder de TODOS ler os repositórios na hora.

| Passo | Quem |
|---|---|
| 1. Linha de base: em 5 dias, quanto tempo o plano das 6h50 leva e quantas leituras de repositório o Líder faz | Líder de TODOS |
| 2. Criar as 3 revisões D-1 (GitHub, LearnTech, Comunidade), só de leitura, com prompt curto que chama a skill `relatorio-do-dia` | responsável aprova (F4) |
| 3. Medir por 5 dias | Líder de TODOS |

Estudo de workflow, só se o responsável pedir: a auditoria mensal N1/N2/N3 de 48 repositórios é um bom candidato (muitas leituras independentes). Antes de rodar, estimar o custo pelo número de agentes.

## Métrica

- Revisões D-1 concluídas por dia: meta 3 de 3.
- Tempo do plano das 6h50.
- Execuções travadas em permissão: meta 0.

## Resultado

A medir.
