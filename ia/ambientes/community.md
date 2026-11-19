# Ambiente Comunidade

Pasta `C:\douglasabnovato-community`, sessão "comunidade LearnTech". Levantado em 18/11/2026, só leitura. Mapa geral em [`README.md`](README.md).

## O que é

- **`formacao-dev`**, único repositório da organização learnTECH Community: formação fullstack em comunidade.
  - O `CATALOGO.md` tem 161 itens em 12 trilhas (T0 a T11), com 87 feitos.
  - O roadmap.sh entra só por link, por causa da licença (`docs/adr/001-roadmap-sh-so-por-link.md`).
  - Cada item é praticado num projeto só, o **Painel de Formação**, que lê o próprio `CATALOGO.md`.
- **Público:** pessoas da comunidade que estão aprendendo. A hipótese do `docs/MVP.md` é "3 pessoas concluírem a T2 em 4 semanas a partir de 10/11/2026".
- **`RELATORIO-ENTENDIMENTO.md`**, na pasta raiz: uma leitura de produto, com plano em fases e perguntas ao responsável (18/11/2026).

## Pilha

| Parte | Tecnologia | Onde |
|---|---|---|
| Painel | React 19, Vite 8, TypeScript strict, React Router, TanStack Query, zod | `painel/src/` |
| API | Node 22+, Express 5, helmet, zod; repositórios plugáveis (memória, SQLite, Mongo) | `api/src/`, `api/src/repositorios/contrato.mjs` |
| Banco | SQL versionado e scripts de migrar, semear e backup | `api/migracoes/`, `api/consultas/`, `src/banco/` |
| Contrato | OpenAPI | `api/openapi.json` |
| Infra | Docker Compose, nginx sem root, Prometheus, Render | `compose.yaml`, `nginx/`, `prometheus/`, `render.yaml` |
| Guardas | catálogo, segredos, orçamento de peso, LCP, ZAP, disponibilidade, cada um com teste | `scripts/*.mjs` |

ADRs: 002 (pilha que cresce por trilha), 003 (React) e 004 (relacional; Mongo só como estudo).

## Processo de engenharia

- **Fluxo Git** (`CONTRIBUTING.md`): `feature/AAAA-MM-DD` → `developer/sprint-<quinta>` → `main`, commits convencionais, sem force push. É o mesmo de [`fluxo-git.md`](../../processo/fluxo-git.md).
- **Issue** em quatro partes (Objetivo, Motivo, 3 a 5 critérios, Fora desta issue) e **revisão** em três (pergunta, sugestão, reconhecimento).
- **Template de PR** com checklist que obriga revisar `docs/ameacas.md` e `docs/dados-pessoais.md` quando muda rota ou dado.
- **Testes:** cerca de 157 no painel (Vitest), 245 na API (`node:test`, contrato por Ajv) e 160 e2e (Playwright + axe, Chromium claro e escuro, WebKit, Pixel 7). Cobertura mínima de 90%.
- **CI:** `ci.yml` (catálogo, app, cobertura, painel, API com SQLite e Mongo em Node 22 e 24, Docker, compose), `codeql.yml`, `varreduras.yml` (Trivy, ZAP), `imagem.yml`, `pages.yml` e `disponibilidade.yml`. Dependabot semanal.
- **Segurança e LGPD:** `SECURITY.md`, `docs/seguranca.md`, `docs/ameacas.md` (STRIDE), `docs/incidente.md` e `docs/dados-pessoais.md`.
- **Estado:** `docs/MVP.md` (12 critérios, evidência datada) e `docs/diario/` (só `dia-2026-11-11.md`).
- **Pendências do responsável:** a `main` está sem proteção (#38), nada publicado (#230).

## IA hoje

- **Uso intenso:** 210 de 347 commits têm `Co-Authored-By: Claude Opus 5.5`, quase todos em 10 e 11/11/2026, de um único autor.
- **Nenhuma configuração versionada:** sem `CLAUDE.md`, `.claude/`, `AGENTS.md`, `.mcp.json` ou hooks, no repositório e na pasta raiz.
- **Única regra escrita para agentes:** `docs/incidente.md`, "Agentes de IA seguem o papel 'quem mantém'" (não revogam, não trocam segredos, não reescrevem histórico).
- **Fora da orquestração:** o ambiente não tem sessão dona na R4 nem sigla na R8.

## Risco próprio deste ambiente

O `RELATORIO-ENTENDIMENTO.md` (§6.3 e §8.2) aponta o projeto como "pronto demais" para uma formação. Se o agente implementa os itens que as pessoas deveriam praticar, a comunidade perde o exercício. Este é o ponto mais importante da arquitetura de IA aqui: definir **o que o agente não faz**.

Sugestões para a sessão do ambiente: `C:\douglasabnovato-community\orientacoes-ia.md`.
