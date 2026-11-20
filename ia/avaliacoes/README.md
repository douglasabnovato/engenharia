# Avaliações: gabaritos dos agentes

Cada agente e cada skill tem um gabarito: casos reais com a resposta esperada e uma nota. Uma mudança de prompt, de modelo ou de esforço só entra se a nota de teste não cair ([`ciclo-evolutivo.md`](../../processo/ciclo-evolutivo.md), seção 5; estudo [`07-avaliacao.md`](../estudos/07-avaliacao.md)).

## Formato de um gabarito

Um arquivo por agente, `ia/avaliacoes/<agente>.md`, com:

```markdown
# Gabarito · <agente>

**Versão do prompt:** <commit do arquivo do agente>
**Casos:** 20 (14 de ajuste, 6 de teste)

| # | Conjunto | Entrada (link ou caminho, sem dado pessoal) | Resposta esperada | Como dar a nota |
|---|---|---|---|---|
| 1 | ajuste | PR x#12, diff de `src/Form.tsx` | "falta estado de erro no envio" | acerto se o achado aparece com gravidade média ou alta |

## Rodadas

| Data | Modelo e esforço | Ajuste | Teste | Tokens | Decisão |
|---|---|---|---|---|---|
```

Regras:
- **Casos reais:** PRs, issues e conteúdos que já existem, com o defeito conhecido ou a decisão do responsável como resposta. Nada inventado para "passar".
- **Sem dado pessoal** nem trecho do `douglasabnovato.dev` (R20).
- **Teste separado:** os 6 casos de teste não são usados para ajustar o prompt.
- **Juiz:** quando a nota for dada por outro modelo, conferir 5 casos à mão por rodada.
- **Níveis:** o agente começa em AU0 (propõe). Sobe com 85% no teste e desce se a amostra revisada cair abaixo de 80%.

## Situação

| Agente | Quem fornece os casos | Casos | Última nota |
|---|---|---|---|
| `qa`, `a11y` | arquitetura de IA, de PRs antigos do GitHub (estudo 7) | a coletar | — |
| `performance`, `ui`, `ux`, `mobile` | arquitetura de IA, de PRs antigos do GitHub | a coletar | — |
| `secops`, `privacidade` | arquitetura de IA, de alertas e issues resolvidas | a coletar | — |
| `arquiteto`, `devops`, `pm` | arquitetura de IA, de ADRs e issues fechadas | a coletar | — |
| `revisor-pedagogia`, `revisor-storytelling`, `revisor-marketing` | repositórios LearnTech, de conteúdos já publicados e revisados pelo autor | a coletar | — |
| `triador` (learntech-content) | repositórios LearnTech | existe (`npm run triador:gabarito`) | 76% direitos, 67% destinos |

Ordem: `qa` e `a11y` primeiro (estudo 7), depois os revisores de conteúdo, porque o LearnTech é quem mais publica.
