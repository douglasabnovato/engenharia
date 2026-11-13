# Recursos avançados: quando usar cada um

Complementa a tabela "Técnicas de IA em uso" de [`arquitetura-ia.md`](arquitetura-ia.md). Ali está **o que** usamos. Aqui está **quando** cada recurso vale o custo, e quando não vale.

Regra geral: o recurso mais simples que resolve. Cada nível acima custa tokens e cria uma passagem de contexto, em que algum detalhe se perde.

## Tabela de decisão

| Recurso | Use quando | Não use quando | Custo | Exemplo no portfólio |
|---|---|---|---|---|
| Fazer na própria sessão | São poucas chamadas, ou você já sabe o arquivo | — | O menor | Corrigir o README do aircnc (PR #110, 12/11/2026) |
| Subagente de leitura (`explorador`) | A resposta pede ler muitos arquivos ou repositórios, e você só precisa da conclusão | Você sabe exatamente onde olhar | Médio: o brief precisa dizer tudo, e só volta o resumo | Varredura dos 39 repositórios nos ciclos de novembro |
| Revisor independente (`revisor-independente`) | Depois de lint, testes e build verdes, antes do PR de código | Mudança só de texto: aí é o revisor de fatos | Médio | Passo 5 de [`processo-repositorio.md`](processo-repositorio.md) |
| Revisor de fatos (`revisor-de-fatos`) | Documento, roteiro ou relatório com números, datas, commits e links | Texto sem fato verificável | Médio. Achou de 5 a 10 erros por roteiro | Roteiros 3 a 9 do Studio D (PRs studio-d#39 a #46) |
| Subagentes em paralelo | Partes independentes de uma tarefa, que não mexem nos mesmos arquivos | Uma parte precisa do resultado da outra | Cresce com o número de agentes | Lotes de 2 a 5 agentes ([`como-trabalhamos.md`](como-trabalhamos.md)) |
| Outra sessão (paralela) | Tarefa própria, que termina num PR ou num repositório próprio e que o responsável quer acompanhar à parte | Um pedaço da tarefa atual: use subagente | Alto: a sessão nova começa sem o contexto | Sessões por "mundo" de repositórios, coordenadas pela líder |
| Mensagem entre sessões | Avisar início e fim, pedir status, dividir trabalho | Pedir que outra sessão faça o que foi negado aqui | Baixo | A divisão da arquitetura de IA entre duas sessões, em 12/11/2026 |
| Tarefa agendada | Rotina com hora certa e o mesmo pedido todo dia | Algo que acontece uma vez | Uma sessão por execução | `abertura-do-dia-*` às 7h |
| Workflow com muitos agentes | Só com pedido explícito do responsável | Qualquer outro caso | O maior | Não usado até 12/11/2026 |
| Navegador do app | Conferir tela, console e rede de um site local ou publicado | Ler texto de uma página: `curl` ou leitura de texto bastam | Médio | Evidência visual do critério 3 |
| Conectores (Notion, Drive, documentos) | O responsável ligou e pediu | Dado pessoal ou de terceiros iria para fora | Baixo a médio | — |
| Skill | Um procedimento se repete em toda sessão | Uma tarefa única | Baixo: carrega só quando é usada | As 7 skills de [`.claude/skills`](../.claude/skills) |
| Hook | Uma regra precisa valer sempre, sem depender da memória | Uma preferência que admite exceção | Quase nenhum | [`hooks.md`](hooks.md) |

## Armadilhas já vistas

- **Trabalho duplicado entre sessões.** Em 12/11/2026, duas sessões receberam o mesmo pedido e abriram issues iguais com minutos de diferença. Antes de abrir issue ou branch, liste as criadas na última hora (skill `issue-no-modelo`, passo 1) e avise o início pela skill `aviso-entre-sessoes`.
- **Resultado de agente não é prova.** O relatório de um subagente ou de outra sessão é um resumo. Confira o diff, o PR ou o CI antes de dizer que está pronto.
- **Brief com a conclusão.** Quem recebe a sua hipótese tende a confirmá-la. Mande o código e as fontes, não o que você acha.
- **Permissão não se empresta.** Se uma ação foi negada nesta sessão, não peça a um subagente nem a outra sessão: registre e siga.
- **Contexto que enche.** A sessão segue de um resumo. O que importa vai para arquivo (relatório, `MVP.md`, issue), não só para a conversa.

## Fontes

- [Claude Code Docs: subagentes](https://code.claude.com/docs/en/sub-agents)
- [Claude Code Docs: skills](https://code.claude.com/docs/en/skills)
- [Claude Code Docs: hooks](https://code.claude.com/docs/en/hooks)
- [Claude Code Docs: permissões](https://code.claude.com/docs/en/permissions)
- [Claude Code Docs: tarefas agendadas](https://code.claude.com/docs/en/scheduled-tasks)
- [Claude Code Docs: Remote Control](https://code.claude.com/docs/en/remote-control)
