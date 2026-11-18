# Ambiente GitHub

Pasta `C:\douglasabnovato-github`, sessão "repositórios GitHub" (papel da DG github na [`orquestracao.md`](../orquestracao.md)). Levantado em 18/11/2026, só leitura. Mapa geral em [`README.md`](README.md).

## O que é

- Clones dos **40 repositórios de portfólio** e do `figma-design`. São projetos de curso e estudo reabertos em outubro e novembro de 2026 e levados à régua de MVP de [`padroes.md`](../../arquitetura/padroes.md), com níveis N1, N2 e N3.
- **`revisao/`**: revisão transversal de 18/11/2026, feita pelo `gh` e pelos `docs/MVP.md`.
  - `revisao-2026-11-18.md`: 380 de 432 critérios atendidos (88%), 37 de 40 repositórios com "Finalizado: sim", 437 issues abertas (183 com `depende-do-responsavel`), 34 PRs abertos (27 do Dependabot), ruleset `principal-protegida` em 40 de 40.
  - Tabelas `.tsv` e `.txt` com a contagem por repositório e as issues por tema.
  - Seção "Trabalho que o Claude pode fazer sem você" e a R7a citada.

## Pilhas

| Grupo | Exemplos | Base |
|---|---|---|
| Node + React/Expo | aircnc, be-the-hero, dev-radar, instagram-feed, my-money-app, controle-financas, feedback-widget, headset, niky | Express 5, Mongoose, pg, SQLite, Prisma, Vite, Expo, Socket.IO |
| Express com SSR | casa-criativa, proffy, doe-sangue-salve-vidas, jobs-calc, rocket-q, cm-quiz-app, valoriza | Nunjucks, EJS, Vue, TypeORM |
| SPA React/TS | calculadora, coin-wallet, letmeask, oxe-online, studio-d, catalogo-acai, douglasabnovato.dev, facil-admin-plataforma, movies, components | Vite, MUI, Supabase, Firebase |
| Next.js e Vue | petshop, sushibar; e-commerce-t-shirt, restaurante-churrascaria | Next, Vue, Supabase, Firebase |
| Conteúdo e estático | aula-de-programacao (461 páginas), facil-admin-gestao, facil-admin-para-voce, ux-design, douglasabnovato, dashboards | HTML |
| Outros | biblioteca (Python), learning-portal-fiori-sap (UI5), figma-design (sem código) | — |

## Processo de engenharia

- **Pacote de docs** em cerca de 32 repositórios: `ANALISE`, `ARQUITETURA` (C4 em Mermaid), `AVALIACAO`, `DEPLOY`, `MVP`, `PLANO-DE-ACAO`, `PLANO-ESTRATEGICO`. Modelos em [`arquitetura/`](../../arquitetura/).
- **`docs/MVP.md`** em 40 de 40. Cinco usam `documentacao/` em vez de `docs/`.
- **ADRs** em 11 repositórios, quase todas "aceitar alertas de desenvolvimento do Dependabot". A numeração tem três formatos (`0006-`, `ADR-004-`, `0001-`).
- **CI** em 40 de 41 (`ci.yml`). Playwright em 38, job `e2e` em 29, axe em cerca de 31.
- **Dependabot:** alertas em 40, mas `dependabot.yml` só em 5 (catalogo-acai, douglasabnovato, facil-admin-plataforma, oxe-online, studio-d). Há 27 PRs do Dependabot abertos, que o agente não pode mesclar.
- **Fluxo Git** de [`fluxo-git.md`](../../processo/fluxo-git.md). A principal mistura `main` e `master`.

## IA hoje

- **Uso intenso:** 1.655 de 4.775 commits (cerca de 35%) com `Co-Authored-By: Claude Opus 5.5`, entre 30/10 e 17/11/2026.
- **Configuração de IA no repositório:** nenhuma. São 0 de 41 com `CLAUDE.md`, `.claude/`, `AGENTS.md` ou instruções de outra ferramenta. O `components/docs/05-ajustes-e-backlog.md` já pede o seu (item A-24, "A fazer").
- **Modelo de operação documentado no produto:** `studio-d/roteiros/engenharia-com-ia/` (papéis, briefs, revisor que recebe só o diff, seis fases de projeto novo). É o mesmo de [`como-trabalhamos.md`](../como-trabalhamos.md), contado como conteúdo.
- **`docs/claudeia/`** em components, douglasabnovato.dev e facil-admin-para-voce, no formato da revisão independente do LearnTech.
- **IA dentro de produto:** `controle-financas/server/src/services/receiptExtractor.js` lê cupom fiscal com LLM. A issue #29 trata do erro de leitura.

## Lacunas próprias

| Lacuna | Evidência |
|---|---|
| Sem `CLAUDE.md` por repositório: comando de teste, principal (`main`/`master`) e pasta de docs mudam e o agente descobre a cada vez | 0 de 41; A-24 do components |
| Pacote de docs sem validação: pasta, nome de ADR e README variam | `docs/` × `documentacao/`; README.md (18), Readme.md (12), readme.md (11) |
| Dependabot sem configuração e com fila parada | 5 de 40 com `dependabot.yml`; 27 PRs abertos |
| Cerca de 60 issues desatualizadas | `revisao-2026-11-18.md`, Achado 1 |
| Hooks locais quase inexistentes | `.husky` só no movies |
| `figma-design` fora do padrão | sem MVP, ruleset, CI nem Dependabot |
| Feature de IA sem avaliação | `receiptExtractor.js` sem conjunto de cupons de teste com resposta esperada (inferido · confirmar) |

Sugestões para a sessão do ambiente: `C:\douglasabnovato-github\orientacoes-ia.md`.
