# 13/11/2026 · Orquestrador (DG líder) acima das sessões

## Contexto

O responsável pediu: "me apresente um prompt para eu criar um claude code para ser o lider orquestrador dg lider para os dg mundo, dg veb e dg github fork. vamos desenhar as regras da arquitetura de ia nesse ecossistema".

Até aqui, a DG mundo fazia dois papéis: dona do learnTECH e líder das outras sessões. Em 12 e 13/11/2026, isso trouxe três problemas:
- 8 issues abertas em duplicidade para o mesmo pedido;
- duas leituras da mesma regra de merge;
- avisos de todas as sessões disputando a mesma conversa que também entregava código.

## Decisões

| # | Decisão | Por quê |
|---|---|---|
| O1 | Nova sessão **DG líder** como orquestrador, aberta em `C:\douglasabnovato-github` | Separa coordenar de entregar; a pasta carrega o `CLAUDE.md` do portfólio |
| O2 | A DG mundo passa a ser **sessão de projeto** do learnTECH. Isso substitui o papel "líder" da D2 de 12/11 | Um papel por sessão |
| O3 | Papéis: **orquestrador**, **sessão de projeto** e **sessão de apoio** | Mantém a D2, trocando "líder" por "orquestrador" |
| O4 | Cada repositório tem uma sessão dona; o `engenharia` é do orquestrador | Evita trabalho duplicado e conflito de arquivo |
| O5 | Reserva no orquestrador antes de abrir issue ou branch em repositório compartilhado | Evita issues duplicadas |
| O6 | Relatório consolidado em `engenharia/relatorios/`, público, sem detalhe interno da VEB | Um lugar só para o dia de todas as sessões |
| O7 | O orquestrador não escreve código nos produtos | Coordenar e entregar na mesma conversa disputa o contexto |

Regras completas: [`ia/orquestracao.md`](../ia/orquestracao.md). Prompt de criação: [`ia/prompts/dg-lider.md`](../ia/prompts/dg-lider.md).

## Opções descartadas

- **A DG mundo seguir como líder:** é mais barato, mas mistura coordenação e entrega na mesma conversa, e as duplicidades de 12/11 mostraram o custo.
- **Cada sessão se coordenar sozinha:** sem um ponto único, nenhuma sessão vê o todo, e o responsável recebe listas repetidas.

## Pendências

- O responsável cria a sessão com o prompt e confirma O1 a O7.
- Depois de criada, mudar as tarefas agendadas das 7h para mandar o resumo ao orquestrador. O orquestrador propõe essa mudança, e o responsável aprova.
