# Sessão "DG github" original (29/10 a 09/11/2026)

A sessão "DG github" original foi a primeira a cuidar dos repositórios do GitHub. Em 09/11/2026, às 21h40, ela ganhou um fork, a "DG github (fork)", que continuou o trabalho. Em 13/11/2026, o responsável pediu para apagar a original e manter só o fork. Este documento guarda o contexto dela antes disso.

## Como foi conferido

- As três conversas da original terminam em 09/11/2026 às 21h40, o mesmo minuto em que o fork foi criado. O app mostra 22h53 como última atividade, mas nenhuma mensagem nas conversas dela é posterior às 21h40.
- Por isso, nada do que a original fez ficou fora do fork: a conversa inteira foi herdada por ele.
- Conferido em 13/11/2026 pelo fork, lendo as conversas da original e o estado no GitHub com o `gh` (aircnc#66 e #87 fechados, #99 e #104 mesclados, #88 e #89 fechadas).

## Linha do tempo

| Data | Pedido do responsável | O que a sessão fez |
|---|---|---|
| 29/10 | Analisar o GitHub e os dois Projects, sem mexer nos repositórios de outras sessões | Varredura dos repositórios e das issues dos Projects |
| 30/10 | Plano de ação; começar pelo `movies` | Primeiro ciclo no `movies`: documentação, plano estratégico e execução. Decisão de manter a chave da TMDB (risco aceito) |
| 30/10 a 31/10 | Seguir sozinha até 31/10, 5h | Ciclo nos repositórios liberados, com relatório no fim |
| 31/10 a 01/11 | Decidir sem interferência; MVP e issues | Critérios de MVP por repositório; merges na sprint com CI verde; regras do Firestore do `restaurante-churrascaria` |
| 01/11 | Índice de 0 a 100; Projects com todos os campos; não parar | Relatórios com o índice, campos dos Projects preenchidos, pendências em `pendencias-responsavel.md` |
| 02/11 | Avisar início e entrega; plano para o responsável | Avisos a cada tarefa; plano das tarefas do responsável ordenado por facilidade |
| 03/11 | Processo de PM e engenharia para projeto novo; ciclo por repositório | Processo em seis fases e o ciclo de 03/11 (pesquisa, docs, código, MVP e 5+ issues por repositório) |
| 06/11 | Relatório do estado e do que está no ar | Relatórios de 05 e 06/11, com percentual, hospedagem e issues |
| 09/11 | Ciclo de 07/11 nos 21 repositórios não finalizados; decidir e documentar | 21 de 21 em "Finalizado: sim" na sprint, nada na principal ([decisão de 09/11](../../decisoes/2026-11-09-ciclo.md)) |
| 09/11, noite | Revisar o `aircnc` com o responsável e publicá-lo | Fluxo local conferido; PR #99 do ciclo mesclado; Dependabot #66 e #87 fechados por já estarem na `master`; início da publicação no Render e no Atlas |

## Decisões que continuam valendo

Estão na memória das sessões e na base de engenharia. As principais:
- Fluxo `feature/AAAA-MM-DD` → `developer/sprint-<próxima quinta>` → principal, e nada na principal sem o responsável ([`fluxo-git.md`](../../processo/fluxo-git.md)).
- `docs/MVP.md` com uma tabela só, "Atende" só com comando, data e resultado ([`padroes.md`](../../arquitetura/padroes.md)).
- Não parar: registrar a pendência e seguir.
- Avisar o início e a entrega de cada tarefa, com o índice de 0 a 100.
- Projects com todos os campos preenchidos.
- Chave da TMDB do `movies` e contas de demonstração mantidas como risco aceito (ADRs de cada repositório).
- Nunca commitar nos clones locais parciais (`aula-de-programacao` e `ux-design`).

## Onde estão os registros dela

- Relatórios e planos antigos: pasta `historico\` na raiz do portfólio (`portfolio-2026-10-30.md`, `plano-projects-2026-11-01.md`, `decisoes-plano-2026-11-02.md`, `processo-repositorio-2026-11-03.md`, `estado-projetos-2026-11-05.md`, `relatorio-portfolio-2026-11-05.html`, `decisao-2026-11-09.md` e o `guia-do-responsavel.md`).
- Decisões que viraram base: [`decisoes/2026-11-02-plano.md`](../../decisoes/2026-11-02-plano.md) e [`decisoes/2026-11-09-ciclo.md`](../../decisoes/2026-11-09-ciclo.md).
- Pendências do responsável: `pendencias-responsavel.md`, na raiz do portfólio.

## O que estava em andamento no fork e como terminou

No momento do fork, o responsável estava publicando o `aircnc`. O cluster M0 antigo do Atlas não voltava ("backup snapshot is too old"). O fork terminou o trabalho na mesma noite:
- Cluster novo criado no Atlas e `0.0.0.0/0` ativo.
- Render pelo Blueprint. A API ganhou um sufixo no nome, e o PR aircnc#104 apontou o site para ela.
- O usuário `aircnc-app` foi corrigido para `readWrite` só no banco `aircnc`.
- O site e a API responderam, e as issues aircnc#88 (publicação) e aircnc#89 (principal protegida) foram fechadas com evidência.

## O que ainda está aberto daquele trecho

| Item | Situação em 13/11/2026 | Quem faz |
|---|---|---|
| Usuários antigos do Atlas com acesso a todos os bancos (`readWriteAnyDatabase`): o do `instagram-feed`, com senha no histórico público, e o do `dev-radar` | instagram-feed#85 aberta, sem registro de que foi revogado; lembrete comentado em 13/11/2026 | Responsável |
| `dev-radar` e `instagram-feed` dependiam do cluster antigo; quando forem republicados, vão encontrar um banco vazio | A original disse que registraria e não registrou. O fork registrou em 13/11/2026 em dev-radar#61 e instagram-feed#87 | Feito |

## Por que a sessão pode ser apagada

Tudo o que ela fez está no GitHub (PRs, issues e commits), nos registros acima e na conversa herdada pelo fork. O único compromisso dela que ficou sem fazer, o registro do banco vazio, foi cumprido pelo fork em 13/11/2026.
