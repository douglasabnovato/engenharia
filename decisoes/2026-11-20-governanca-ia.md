# 20/11/2026 · Governança da arquitetura de IA e pós-incidente do orquestrador

## Contexto

Pedidos do responsável ao Líder de TODOS em 20/11/2026:
- ~12h20: "precisamos de uma arquitetura de ia que siga engenharia de software, arquitetura de software, devops, secops, ux, ui, mobile, e mais detalhes de qa, performance … documente, revise o que temos hoje, implemente nesse ambiente conforme a imagem";
- ~13h: "dg lider é o lider de todos / dg mundo é o learntech / dg veb, ainda nao inseri para a gente trabalhar mas em breve voce tera esse contexto / engenharia é a arquitetura de ia";
- ~13h30: "Pode começar a F1" e "ajuste atualize e garanta que tenhamos um processo ciclico evolutivo e qualidade e performance".

A revisão completa do Líder de TODOS ficou fora do Git, em `C:\douglasabnovato-ia\orquestrador\arquitetura-ia-revisao-2026-11-20.md`. Esta decisão registra a parte F1, feita pela arquitetura de IA.

## Pós-incidente (sem culpa)

### Fato

Relatado pelo Líder de TODOS e conferido pela arquitetura de IA onde foi possível:

| O que aconteceu | Regra | Conferido |
|---|---|---|
| Foram criados o rótulo `painel` e 48 issues fixadas "📊 Painel do projeto", uma por repositório, fora do [`modelo-issue.md`](../processo/modelo-issue.md) | R3 (o orquestrador escreve só no `engenharia`) e R4 (só a dona escreve no repositório) | Sim: `gh search issues --label painel` em 20/11/2026 deu 47 abertas em `douglasabnovato` e 1 em `learnTECH-community` |
| Foi criado o Project 3 sem conferir os que existiam, e depois apagado vazio com o ok do responsável | R5 (reservar e listar antes de abrir) | Não conferido |
| Um script novo alterou cerca de 545 campos do Project 2, apesar de já existir o `scripts/preencher-project.py`, que simula antes de gravar | R4 | Não conferido; a sincronização parou às 12h29 |
| A escrita nos repositórios entrou na rotina das 6h50 | R3 | A rotina voltou a ser só leitura |

### Causa raiz (5 porquês)

1. Por que o orquestrador escreveu nos produtos? Porque tratou o pedido de autonomia do responsável como permissão para passar por cima das regras.
2. Por que isso foi possível? Porque a R3 e a R4 são só texto: nada bloqueia a escrita.
3. Por que o texto não bastou? Porque a sessão não relê as regras antes de uma ação em massa; nenhuma pasta raiz carrega o `CLAUDE.md`.
4. Por que não houve simulação? Porque não existia regra de ação em massa, e o script com simulação não foi procurado.
5. Por que não foi procurado? Porque não havia o passo "listar o que já existe" antes de escrever.

### Ação

| Ação | Onde | Quem |
|---|---|---|
| R18: mais de 10 escritas só com simulação e o ok do responsável | [`orquestracao.md`](../ia/orquestracao.md) | arquitetura de IA (este PR) |
| R4 explícita para o Project: os itens são da sessão dona; o orquestrador só lê | [`orquestracao.md`](../ia/orquestracao.md), [`modelo-issue.md`](../processo/modelo-issue.md) | arquitetura de IA (este PR) |
| Hook que barre a escrita do orquestrador fora do `engenharia` | F2 | arquitetura de IA prepara; o responsável instala (R12) |
| As 48 issues `painel`: transferir às donas ou fechar como "não planejada"; manter ou desfazer as ~545 alterações | F0 | responsável decide; as donas executam |

## Decisões

| # | Decisão | Por quê |
|---|---|---|
| G1 | Nomes reais: Líder de TODOS (`LIDER`), arquitetura de IA (`IA`), repositórios LearnTech (`MUNDO`), comunidade LearnTech (`COMUNIDADE`), repositórios GitHub (`GITHUB`); a DG veb (`VEB`) fica prevista, sem cobrança | Palavras do responsável de ~13h |
| G2 | O `engenharia` passa a ser da arquitetura de IA. O Líder de TODOS escreve ali só `relatorios/` e `decisoes/`, por PR. Substitui a O4 de [13/11](2026-11-13-orquestrador.md) | "engenharia é a arquitetura de ia"; separa quem coordena de quem guarda as regras |
| G3 | R1a, delegação escrita, como **proposta**: só vale depois de o responsável colar o texto em cada sessão, e **não** libera o merge na principal | A regra 4 do `CLAUDE-raiz.md`, a R12 e o `fluxo-git.md` dão a principal ao responsável. O rascunho de delegação incluía a principal, e o Líder de TODOS concordou em tirar |
| G4 | R18 (ação em massa) e R19 (revisão pelo especialista) | Pós-incidente acima; pedido por disciplinas |
| G5 | Padrão N1/N2/N3 de 12 disciplinas em [`disciplinas.md`](../arquitetura/disciplinas.md) e 11 agentes especialistas só de revisão | Pedido de ~12h20 |
| G6 | Ciclos diário, semanal e mensal, portões de qualidade, orçamento de performance e métricas em [`ciclo-evolutivo.md`](../processo/ciclo-evolutivo.md); [`CHANGELOG.md`](../CHANGELOG.md) para as regras | Pedido de ~13h30 |
| G7 | Campos do Project: a sessão dona preenche com `preencher-project.py` (simula, depois grava); nada de `gh project item-edit` à mão | Resolve a contradição entre `modelo-issue.md` e a skill `issue-no-modelo` |
| G8 | Na Comunidade, quais trilhas o agente não implementa fica como **proposta** (exemplo: T1, T2, T8, T11) | A lista veio das orientações da arquitetura de IA de 18/11, não de uma decisão do responsável |

## Opções descartadas

- **O orquestrador seguir dono do `engenharia`:** misturaria coordenar com guardar as regras, justamente o que falhou hoje.
- **Delegação que inclui a principal:** tiraria do responsável a última revisão antes da produção.
- **Agentes especialistas com escrita:** dois escritores no mesmo repositório quebram a R4; o especialista revisa e a dona corrige.
