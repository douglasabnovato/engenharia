# Mapa de papéis e carga das sessões

Responde à pergunta do LIDER de 20/11/2026, feita a partir da ordem do responsável: "se entenderem que precisamos criar mais codes dentro de cada contexto, tambem pode planejar estruturar para me orientar".

Levantado em 20/11/2026, por volta das 19h45, pela arquitetura de IA. Fontes: lista de sessões do app, `gh search` e a pasta de memória de cada sessão. Os números de issues e PRs são do momento da leitura. A busca do GitHub atingiu o limite de uso no fim; os números que faltaram estão marcados "—".

## Mapa

| Sessão (sigla) | Pasta | Repositórios | PRs abertos | Issues abertas | Gargalo de hoje |
|---|---|---|---|---|---|
| Líder de TODOS (`LIDER`) | `C:\douglasabnovato-community` | lê todos; escreve `engenharia/relatorios` e `decisoes` | — | — | divide pasta e memória com a COMUNIDADE (achado 1) |
| arquitetura de IA (`IA`) | `C:\douglasabnovato-ia` | `engenharia` | 2 (#50, #51) | 13 | o merge do responsável |
| repositórios GitHub (`GITHUB`) | `C:\douglasabnovato-github` | 41 (inclui o `douglasabnovato.dev`, sob R20) | 51 | 367 | fila esperando o responsável (R7a) |
| repositórios LearnTech (`MUNDO`) | `C:\douglasabnovato-learntech` | 5 | 0 | 137 | o `hd/` não está nesta máquina (triador e produção parados) |
| comunidade LearnTech (`COMUNIDADE`) | `C:\douglasabnovato-community` | `learnTECH-community/formacao-dev` | 8 | 125 | porta de entrada para colaboradores ainda fechada |
| DG veb (`VEB`) | — | prevista | — | — | contexto ainda não inserido |

## Achados

1. **O LIDER e a COMUNIDADE abrem na mesma pasta e por isso dividem a mesma memória.** O Claude Code guarda a memória por pasta (`~/.claude/projects/C--douglasabnovato-community/memory/`). O índice dessa pasta, lido em 20/11/2026, começa com "Papel de orquestrador" e tem 13 memórias do LIDER. A sessão comunidade LearnTech carrega essas memórias ao abrir. É o mesmo tipo de falha do pós-incidente de 20/11: uma sessão agindo com o papel de outra.
2. **O GitHub não precisa de mais braços agora.** Com 51 PRs abertos, a R7a já bloqueia construção nova. Outra sessão só aumentaria a fila que espera o responsável.
3. **O LearnTech está limitado pela máquina, não pela sessão.** Sem o `hd/`, a produção de conteúdo e o triador não rodam aqui (`learntech-content/docs/processo/ESTADO.md`).
4. **A Comunidade cresce para fora.** O plano de comunidade do LIDER (parte B) pede resposta em até 48 horas a pessoas de fora. Se der certo, a carga sobe em triagem e revisão, não em código.

## Proposta

| # | Proposta | Por quê | Quem faz |
|---|---|---|---|
| P1 | **Mover o LIDER para uma pasta própria**, por exemplo `C:\douglasabnovato-lider`, e levar as memórias de orquestrador para lá. A pasta `C:\douglasabnovato-community` fica só da COMUNIDADE | Achado 1: separa papéis e memórias | responsável cria a sessão; o LIDER prepara a lista de memórias a mover |
| P2 | **Não criar sessões novas agora** no GitHub e no LearnTech. Reavaliar quando os PRs esperando o responsável ficarem abaixo de 30% (meta do [`ciclo-evolutivo.md`](../../processo/ciclo-evolutivo.md)) | Achados 2 e 3 | LIDER, no ciclo semanal |
| P3 | **Gatilho para uma sessão de conteúdo no LearnTech:** quando o `hd/` estiver nesta máquina e o artigo semanal estiver rodando, avaliar separar "conteúdo" (produção e revisão com os revisores de conteúdo) de "código" (API e sites) | Achado 3; produção e código disputam o mesmo contexto | MUNDO avalia no modo melhoria |
| P4 | **Gatilho para uma sessão de triagem na Comunidade:** quando houver mais de 5 contribuições de fora por semana, avaliar uma sessão que só faz triagem e boas-vindas, sem escrever código | Achado 4 | COMUNIDADE avalia no modo melhoria |

Criar ou mover sessão é decisão do responsável (R21). Esta é a recomendação da arquitetura de IA para o LIDER levar a ele.
