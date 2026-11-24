# Ambiente LearnTech

Pasta `C:\douglasabnovato-learntech`, sessão "repositórios LearnTech" (papel da DG mundo na [`orquestracao.md`](../orquestracao.md)). Levantado em 18/11/2026, só leitura. Mapa geral em [`README.md`](README.md).

Esta é a **segunda máquina** do learnTECH, desde 18/11/2026: tem os 5 clones, mas não tem a pasta `hd/` (`learntech-content/docs/processo/ESTADO.md`). Por isso o agente `triador` e a skill `produzir-do-hd` não rodam aqui.

## O que é

O learnTECH treina pessoas para o ecossistema de tecnologia com o que o autor fez. O **learntech-content** é a API e a fonte única de conteúdo, processo e documentação. Ele alimenta quatro sites:

| Repositório | Papel | Pilha | Publicação |
|---|---|---|---|
| learntech-content | API, conteúdo (`content/*.json` validado por Zod), processo | Cloudflare Workers, Hono, D1, Static Assets | Cloudflare (deploy manual, #9) |
| learn-tech | programas, artigos, áreas | React 19, Vite, Tailwind 4, Vitest | Vercel |
| bootcamps | eventos e formações | React, TS strict, Vite 7, Feature-Sliced Design | Vercel |
| career | empresas, vagas, perfis | JavaScript sem build, `node --test` | GitHub Pages |
| tools | ferramentas e hospedagens | JavaScript sem build, `node --test` | GitHub Pages |

- **Ligação entre eles:** `npm run copias` gera as cópias de reserva nos sites (nunca editadas à mão, ADR 5), e cada site tem contrato em `docs/contratos/<site>.md`, protegido por `tests/contratos-sites.test.ts`.
- **Restrição:** "Custo zero é restrição de projeto" (princípio P-04).

## Processo com IA (o mais maduro dos três ambientes)

- **`CLAUDE.md` em 5 de 5**, com a mesma estrutura: ler `ESTADO-DO-PROJETO`, `COMO-EVOLUIR` e o contrato antes de tudo; "Conteúdo novo entra pela API"; lista dos arquivos gerados; "O Claude não lê nem cadastra segredos"; "O Claude para na `developer`"; tabela de comandos.
- **Ciclo `docs/claudeia/`:**

  | Arquivo | Conteúdo |
  |---|---|
  | 01-relatorio | Notas de 0 a 10 por área, com `arquivo:linha` e "inferido · confirmar" |
  | 02-plano-e-arquitetura | Arquitetura atual e alvo (Mermaid) e ADRs curtos |
  | 03-registro | O que foi feito, riscos, pendências |
  | 04 e 05 | Testes automatizados (`verificar.ps1`) e roteiro manual |
  | 06-mvp-* | Execução das tarefas do MVP, com evidência |
  | 07-* | Rodadas por tema (acessibilidade no learn-tech, performance no bootcamps) |

- **Agente `triador`** (`learntech-content/.claude/agents/triador.md`): propõe a ficha de cada item do acervo; abaixo de 0,7 de confiança vira pergunta ao autor. É medido por `npm run triador:gabarito` (76% em direitos, 67% em destinos, 4 rodadas).
- **Skill `produzir-do-hd`**: ficha de 5 perguntas antes de produzir, e registro de decisão do autor (D-NN) e princípio (P-NN).
- **Governança** (`docs/processo/agentes.md`): papéis triador, produtor, revisor e verificador; aprovações A1 (plano), A2 (PR e deploy) e A3 (fechamento da leva); autonomia AU0 a AU2, com AU0 em vigor e meta de 85% no gabarito para subir.
- **Rotina:** `como-trabalhamos.md` do learnTECH, relatórios do dia em `docs/engenharia/relatorios/`, auditorias (Lighthouse, links: 1.522 URLs, 35 quebradas em 18/11).
- **Documentação testada:** `documentacao.test.ts` confere se todo link dos `.md` e todo `npm run` citado existem.

## Regras da DG mundo trazidas do Samsung (21/11/2026)

Fonte: as memórias da sessão DG mundo, enviadas ao Líder de TODOS em 21/11/2026. Elas complementam a passagem engenharia#52.

- **Exceção do deploy** (09/11 e 10/11/2026). O Claude para na `developer`. As integrações são:
  - `developer` no content, no tools e no bootcamps;
  - `developer-mvp-2026` no learn-tech;
  - `developer-mvp-2026-2` no career.

  A issue fecha só na `main`, com "Refs #N". A exceção vale só quando o responsável pede na hora. Exemplo de 10/11: PR integração → `main` com o `verificar` verde, `gh pr merge --merge` e `npm run deploy`. Fica fora da R22: o pedido é dado na própria sessão para aquele deploy, não vem de um plano aprovado. O login do `wrangler` é conta do responsável (R12) e ficou no Samsung. No Acer, quem entra é ele.
- **Logos** (12/11/2026, "Aprovo os dois"):
  - o catálogo fica em `hd\logos-learn-tech` (`CATALOGO.md`), que é privado e não vai para o GitHub;
  - cor e símbolo por site: career laranja `<!-- -->`, bootcamps verde `{ }`, tools amarelo `</>`, learn-tech azul `/* */`;
  - ainda são propostas, sem aprovação: API roxo `; }` e `engenharia` vermelho `[ ]`;
  - o "D" precisa de redesenho;
  - a pirâmide de 6 cubos é só para `og:image`, nunca para favicon;
  - imagem com dado de outra pessoa não é publicada.

Ficam nos `CLAUDE.md` e nas regras de onde já estão, sem repetir aqui:
- o fluxo do dia (R7, R7a, R8);
- a ficha de ciclo e a revisão que nunca fica em branco (CLAUDE-raiz);
- o modelo de negócio, o ambiente gratuito e a identificação obrigatória (R12);
- os repositórios de terceiros (R13);
- a espera de 4 horas (R11);
- a assinatura das issues, o formato do relatório e a prioridade hd → MVP → produto: são do learnTECH e ficam no `CLAUDE.md` dele (`como-trabalhamos.md`).

## O que vale levar para os outros ambientes

1. `CLAUDE.md` curto por repositório, com "antes de qualquer tarefa", regras que não mudam e tabela de comandos.
2. Autonomia medida: gabarito, nível AU e descida automática quando o acerto cai.
3. Documentação testada e contratos protegidos por teste.
4. Decisão do autor citada entre aspas e convertida em princípio.
5. "Escrito, não executado" para teste ou script que o agente não conseguiu rodar.

## Lacunas próprias

| Lacuna | Evidência |
|---|---|
| `CLAUDE.md` dos 4 sites repetem as seções Privacidade e Git quase linha a linha | os 4 `CLAUDE.md` |
| Regras sem bloqueio: nada impede push na `developer` errada, `git add -A` ou edição dos arquivos gerados | sem `.claude/settings.json` em nenhum repositório |
| Tarefa agendada parou em pedido de permissão | `docs/engenharia/relatorios/dia-2026-11-12.md` |
| Papéis de revisor, verificador e produtor só no texto | só `triador` em `.claude/agents/` |
| `triador` com `Write` sem limite de caminho e sem `model` fixo | `triador.md` |
| Ciclo `claudeia` sem skill: títulos, 07 e diagnóstico variam; script de CI dentro de pasta de docs | `docs/claudeia/` dos 4 sites; `verificar.ps1` |
| Estado em quatro arquivos que se sobrepõem; `ESTADO-DO-PROJETO` dos sites parado em 10/11 | `ESTADO.md`, `ESTADO-DO-PROJETO.md`, `MVP.md`, `PROXIMOS-PASSOS.md` |
| Nome da integração diverge e a CI do bootcamps escuta a branch errada | `developer`, `developer-mvp-2026`, `developer-mvp-2026-2`; CI em `developer-mvp` |
| learn-tech sem lockfile; `format:check` fora da CI no learn-tech e na API | `ci.yml` |
| Gabarito só para o triador | `agentes.md` (métricas por lote ainda manuais) |

Sugestões para a sessão do ambiente: `C:\douglasabnovato-learntech\orientacoes-ia.md`.
