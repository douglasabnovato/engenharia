# Fila da noite produtiva (desde 23/11/2026)

Pedido do responsável em 23/11/2026, às 22h40: "temos processos e qualidades e automacoes para evoluir". Antes disso, ele tinha cobrado: "se tenho impedimentos me esperando, se prepare pesquise ... todos os projetos tem mais inteligência de algoritmos eficiência para evoluir, estudar documentar, planejar, registrar issues".

Este arquivo traz 3 partes:
- o diagnóstico das automações de 23/11;
- o padrão de trabalho da noite, que não depende do responsável;
- o modelo da mensagem do Líder de TODOS para cada sessão.

## 1. Diagnóstico das automações de 23/11/2026

Fonte: o diário do Líder de TODOS de 23/11/2026, conferido pela API do GitHub.

### O que rodou sozinho

| Sessão | O que rodou | Evidência |
|---|---|---|
| arquitetura de IA | merge na sprint pela decisão 138, sem bloqueio da permissão | engenharia#59, #60, #62 e #63 |
| repositórios GitHub (17h) | 4 merges na sprint com a revisão R19 do Esp | studio-d#78, douglasabnovato#76, facil-admin-para-voce#48 e facil-admin-gestao#54 |
| tarefas agendadas | desde a decisão 135, rodam em modo Auto e não param no 1º comando | a abertura das 06h50 tinha parado no `date` |
| Comunidade e LearnTech | merge na integração depois de uma ORDEM digitada por ele | formacao-dev#326 e #327; learntech-content#52 e #53; learn-tech#153, #154 e #155 |

### O que parou por permissão

| Sessão | O que parou | Por quê |
|---|---|---|
| Comunidade (15h45 e 17h40) | `gh pr merge` do formacao-dev#326 | O modo Auto barra o merge quando o pedido vem por mensagem de outra sessão. |
| LearnTech (17h40) | a 1ª escrita (learntech-content#52) | mesma causa |
| repositórios GitHub (noite) | o lote de 4 merges do bloco Produto, antes da 1ª escrita | mesma causa; a decisão 145 não se cumpriu |
| arquitetura de IA (noite) | trocar o "[A CONFIRMAR]" da R24 por uma Decisão LIDER | a confirmação de uma regra é do responsável |

As sessões não contornaram nenhum bloqueio.

### Por que a noite ficou parada

- A fila das 17h15 era estreita: tinha só merges e triagem.
- Quando a permissão negou os merges, as sessões não tinham trabalho alternativo.
- A regra de permissão `Bash(gh pr merge:*)` não serve como está. Ela também libera o merge na `main`, porque o ruleset da principal pede 0 aprovações.

### 3 propostas (para o responsável escolher)

| # | Proposta | Como funciona | Risco | De quem é |
|---|---|---|---|---|
| P1 | **Fila sem merge** | A noite só tem os tipos da seção 2. Os merges vão para o "Com você" das 08h15, com a ORDEM de cada canal já pronta. | Baixo. Os PRs prontos esperam até a manhã. | Líder de TODOS; já cabe nas regras de hoje |
| P2 | **ORDEM noturna** | Às 17h15, ele digita uma ORDEM em cada canal, com os PRs nomeados, válida até as 08h do dia seguinte. | Médio. Ele aprova antes de ver o resultado da revisão R19. Mitigação: a ORDEM só cobre PR com a revisão R19 já postada e o CI verde. | Ele. Muda a validade "só no dia" do [`ativacao-segura.md`](ativacao-segura.md) [A CONFIRMAR com o responsável] |
| P3 | **Merge só na sprint por script** | Um script confere se a base do PR é `developer/sprint-*` antes de mesclar. A regra de permissão libera só esse script, e nunca o `gh pr merge` direto. | Médio. Quem pode editar o script pode mudar a conferência. Mitigação: o script fica no `engenharia`, com teste, e a regra aponta para o caminho fixo. | Ele. A regra de permissão é configuração (R12) [A CONFIRMAR com o responsável] |

**Recomendação da arquitetura de IA:** começar pela P1 hoje, porque não muda nenhuma regra. Avaliar a P3 depois de uma semana de P1, se os merges da manhã atrasarem a sprint.

Fica de fora: exigir 1 aprovação no ruleset da principal. Com um só dono, ele não pode aprovar o próprio PR e teria de usar o bypass. Isso é conta dele (R12).

## 2. Padrão da fila da noite produtiva

### Tipos de trabalho que nunca dependem do responsável

| Tipo | Exemplos | Onde grava | Escrita no GitHub |
|---|---|---|---|
| Pesquisa | concorrentes, benchmark de comunidades, padrões de mercado | `orquestrador/` ou `rascunhos/` local | nenhuma |
| Estudo | algoritmo, eficiência, orçamento de bundle, acessibilidade | idem | nenhuma |
| Plano | plano da semana, releases, plano de produto | idem | nenhuma |
| Rascunho de issue | até 10, no `processo/modelo-issue.md` | local; vira issue só no limite da R18 | até 10 |
| Teste | escrever e rodar testes, linha de base de Lighthouse e axe | feature + PR | até 10 |
| Documentação | README, CONTRIBUTING, docs de processo | feature + PR | até 10 |
| Revisão R19 em PDCA | revisão de PR aberto, sem merge | comentário no PR | 1 por PR |

### O que nunca entra na fila da noite

- merge na `main`, deploy e publicação em nome dele;
- segredos, contas, custo e configuração (R12);
- mudança de regra sem "[A CONFIRMAR com o responsável]";
- merge que dependa de uma ORDEM ainda não digitada.

### Regra de reserva

Toda sessão recebe, além do item principal, um **item de reserva** de um tipo sem escrita (pesquisa, estudo ou plano). Se a permissão negar o item principal, a sessão registra o bloqueio em 1 linha e passa para a reserva. A sessão não contorna o bloqueio.

## 3. Modelo da mensagem do Líder de TODOS

```
Líder · fila da noite <DD→DD/MM> (<sigla> · <tema>). Ordem do responsável às <hh>h<mm>: "<palavras dele>".

Limites: <onde escreve>; nada na main; sem merge se a permissão negar; no máximo <N> escritas; sem configuração; sem publicar em nome dele.

Entregas:
1. <item principal> — tipo: <pesquisa | estudo | plano | rascunho | teste | docs | revisão>.
2. <item 2>.
Reserva, se a permissão negar: <item sem escrita>.

No fim: resumo de até 10 linhas com links, o número de escritas e o que fica para as 08h15.
```

Cada sessão recebe a sua mensagem, com itens só dos repositórios dela (R4).

## 4. Lições da noite de 23 para 24/11/2026 [A CONFIRMAR com o responsável]

São Decisões LIDER tomadas durante a noite, pela delegação "recomendar e agir". Elas valem até ele confirmar ou mudar no relatório do dia. Fonte: o diário do Líder de TODOS de 23/11/2026 e os PRs engenharia#64 a #77.

| Lição | O que fazer | De onde veio |
|---|---|---|
| **Limite por hora corrida** (Decisão LIDER 150) | No máximo 10 escritas no GitHub em qualquer janela de 60 min: push, PR, comentário, merge e issue. Passou disso, faz a simulação e deixa para ele | Ciclos de 2 a 5 min esvaziaram o limite de "10 por ciclo". A arquitetura de IA fez 13 escritas num ciclo só |
| **1 min de folga** | Antes de escrever, conferir a hora da escrita mais antiga da janela e esperar até que ela tenha mais de 61 min | Às 02h33m18, a hora corrida teve 11 escritas por uns 20 s |
| **Ciclo de 1 a 2 h** | Um ciclo junta o trabalho de 1 a 2 h. Trabalho curto entra no mesmo ciclo, e não abre um novo | o texto da ATIVAÇÃO do ciclo evolutivo |
| **Sem janela, fila local** | Prepara o commit e o texto do comentário no local, numa pasta de fila com um `LEIA.md` que lista as escritas, e envia tudo quando a janela abrir | a fila das 00h32 (9 escritas: #72, #73 e #6) |
| **R19 colada pela dona** (Decisão LIDER 149) | O Esp grava a revisão na pasta dele, e a dona cola no PR com o título "Revisão R19 em PDCA · Esp <disciplina>, colada pela dona" e o caminho do arquivo | Até ele confirmar se o Esp escreve no GitHub (`ia/arquitetura-de-codes.md`, seção 3) |
| **R10 no texto colado** | Antes de colar, buscar nomes de outro contexto (por exemplo, a VEB). Se houver, tirar a linha e dizer no comentário que a dona tirou | 2 casos na noite, nos textos colados do #72 |
| **A hora sai do `date`** | Toda hora de aviso e de diário vem de `date`, e não de estimativa | Os resumos dos ciclos 2 a 5 estavam adiantados. No diário, a hora estimada virou `Desvio (R-Diário, hora)` |
| **Desvio rotulado** | O Líder marca no diário `**Desvio (Rnn):**` no começo do item, e quem desviou avisa por conta própria | a hipótese do `engenharia` (`docs/MVP.md`): a linha de base foi para 6 (Decisão LIDER 151) |
| **Merge pela ATIVAÇÃO** | Com a ATIVAÇÃO digitada por ele, a dona mescla na integração com o CI verde e a R19 "aprovado" ou "aprovado com ressalvas", numa tentativa só. "Pedir mudanças" espera a reconferência | #66, #68 a #73 e #75 a #77 |
| **Nunca parar** | Sem tarefa nem janela, a reserva é pesquisa, estudo ou rascunho local, sem escrita | a cobrança dele às 22h40 e o item 2 da ATIVAÇÃO |
