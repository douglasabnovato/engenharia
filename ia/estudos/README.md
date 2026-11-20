# Laboratório de IA · trilha de estudos

A sessão **arquitetura de IA** estuda o Claude, as metodologias e as ferramentas para desenvolver software e produtos digitais. Os outros três contextos (LearnTech, GitHub e Comunidade) são o campo de prova. O que funciona vira padrão no `engenharia`; o que se aprende vira conteúdo.

Ordem do responsável em 20/11/2026: "arquitetura de ia é para estudar claude ia e metologias e ferramentas para desenvolver projetos de softwares e produtos digitais usando esses contextos".

## Como cada estudo funciona

Cada arquivo tem as mesmas seções:

1. **Conceito:** o que é, em poucas linhas, com a fonte.
2. **Hoje no ecossistema:** o que já usamos, com o arquivo ou o número que prova.
3. **Experimento:** hipótese, contexto real, passos e quem faz. Segue o ciclo de [`ciclo-evolutivo.md`](../../processo/ciclo-evolutivo.md): hipótese → mudança → métrica antes e depois → vira padrão ou é descartado.
4. **Métrica:** o número que decide, com a linha de base.
5. **Resultado:** começa como "a medir". Quando o experimento termina, entra o número, a data e a decisão (padrão, ajuste ou descarte), com uma linha no [`CHANGELOG.md`](../../CHANGELOG.md).

Regras:
- Experimento em repositório de produto é feito pela **sessão dona** (R4). Esta sessão escreve o desenho e lê o resultado.
- Nada roda contra o `douglasabnovato.dev` (R20).
- Experimento que custa dinheiro (chamadas pagas da API) só com o ok do responsável (R12).

## Trilha

| # | Tema | Campo de prova | Situação |
|---|---|---|---|
| 1 | [Contexto e memória](01-contexto-e-memoria.md) | as 4 pastas raiz | desenhado |
| 2 | [Skills, subagentes e hooks](02-skills-subagentes-hooks.md) | GitHub e engenharia | desenhado |
| 3 | [MCP e conectores](03-mcp-e-conectores.md) | LearnTech | desenhado |
| 4 | [Tarefas agendadas e workflows](04-tarefas-agendadas-e-workflows.md) | Líder de TODOS | desenhado |
| 5 | [Claude API e Agent SDK](05-claude-api-e-agent-sdk.md) | LearnTech (triador) | desenhado |
| 6 | [Engenharia de prompt e de contexto](06-prompt-e-contexto.md) | LearnTech (`CLAUDE.md`) | desenhado |
| 7 | [Avaliação: gabaritos e evals](07-avaliacao.md) | LearnTech e engenharia | desenhado |
| 8 | [Metodologias com IA](08-metodologias.md) | GitHub | desenhado |
| 9 | [Custo e desempenho](09-custo-e-desempenho.md) | todas as sessões | desenhado |

A ordem de leitura sugerida é a da tabela: do que todo dia afeta (contexto) ao que só importa com escala (custo).

## Do estudo ao artigo

Toda semana, no ciclo de sexta, um aprendizado com resultado medido vira **proposta de artigo** para o learn-tech:
1. Esta sessão escreve a proposta: título, público, o problema, o experimento, o número e a lição.
2. A proposta vai à sessão **repositórios LearnTech**, que segue as regras editoriais dela e publica. Regra editorial nova e as aprovações A1 a A3 são do responsável.
3. O link do artigo publicado entra no "Resultado" do estudo.

## Métricas do laboratório

| Métrica | Meta inicial |
|---|---|
| Experimentos concluídos por mês | 2 |
| Regras que viraram hook ou teste | crescer mês a mês |
| Acerto dos agentes no gabarito | ≥ 80% ([`avaliacoes/`](../avaliacoes/README.md)) |
| Propostas de artigo por semana | 1 |
