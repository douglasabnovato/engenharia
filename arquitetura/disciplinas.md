# Padrão mínimo por disciplina

O que cada disciplina cobra de um repositório, por nível. Os níveis são os de [`padroes.md`](padroes.md): **N1 estudo**, **N2 vitrine** e **N3 produto**. Cada nível inclui o anterior.

Pedido do responsável em 20/11/2026: "precisamos de uma arquitetura de ia que siga engenharia de software, arquitetura de software, devops, secops, ux, ui, mobile, e mais detalhes de qa, performance". Origem: revisão do Líder de TODOS de 20/11/2026, seção 4.

## Como usar

- A **sessão dona** constrói e confere o checklist do nível do repositório.
- O **agente especialista** da disciplina revisa a mudança e devolve achados ([`.claude/agents/`](../.claude/agents/)). Ele só lê; quem corrige é a sessão dona (R19 de [`orquestracao.md`](../ia/orquestracao.md)).
- O PR de N2 e N3 cita, no corpo, as disciplinas tocadas e o resultado de cada checklist.
- Toda vez que um item vira "Atende", ele leva **comando, data e resultado** ([`definicao-de-pronto.md`](../processo/definicao-de-pronto.md)).

## Tabela

| Disciplina | Agente | N1 estudo | N2 vitrine | N3 produto |
|---|---|---|---|---|
| Arquitetura de software | `arquiteto` | README com a pilha | + ADR em `docs/adr/NNNN-titulo.md` ([`modelo-adr.md`](modelo-adr.md)) e C4 nível 1 ([`modelo-c4.md`](modelo-c4.md)) | + C4 nível 2 |
| DevOps | `devops` | CI com lint, testes e build; ruleset na principal | + deploy automatizado; verificação de que o site está no ar | + disponibilidade agendada; rollback documentado |
| SecOps | `secops` | alertas do Dependabot; nenhum segredo no repositório | + `dependabot.yml` com grupos; `npm audit` de severidade alta na CI; varredura de segredos | + CodeQL; Trivy, se houver imagem; `SECURITY.md`; modelo de ameaças |
| QA | `qa` | e2e do fluxo principal | + teste unitário das regras; estados de erro e vazio | + cobertura mínima de 70% nas regras; plano de testes |
| Performance | `performance` | LCP medido uma vez | + orçamento do [`ciclo-evolutivo.md`](../processo/ciclo-evolutivo.md) no corpo do PR (mediana de 3) | + Lighthouse CI que falha o PR fora do orçamento |
| Acessibilidade | `a11y` | axe sem violação séria | + teclado; tema claro e escuro | + `jsx-a11y` (ou equivalente) no lint |
| Mobile | `mobile` | layout em 375 px | + e2e em 375 px | + checklist de toque e de offline; no Expo, build EAS |
| UX | `ux` | hipótese escrita | + teste com 3 pessoas de fora | + medição de uso (GoatCounter) |
| UI | `ui` | tokens de cor e espaço | + tokens compartilhados entre as telas | + componentes do repositório `components` |
| Privacidade e LGPD | `privacidade` | nenhum dado pessoal real | + aviso de privacidade, se coletar algo | + inventário de dados e base legal |
| Produto | `pm` | problema e público em uma frase | + hipótese com meta e "Fora do MVP" | + medição da hipótese e decisão registrada |
| Documentação | `revisor-de-fatos` | README e `docs/MVP.md` | + pacote de docs ([`modelo-analise.md`](modelo-analise.md), ARQUITETURA, DEPLOY) | + `CONTRIBUTING.md` e `CHANGELOG.md` |

Engenharia de software (fluxo Git, definição de pronto, revisão de correção) vale igual em todos os níveis: [`fluxo-git.md`](../processo/fluxo-git.md), [`definicao-de-pronto.md`](../processo/definicao-de-pronto.md) e o agente `revisor-independente`.

## Onde cada ambiente está hoje

Leitura de 20/11/2026 (revisão do Líder de TODOS, seção 3). ✅ coberto · 🟡 parcial · ❌ ausente.

| Disciplina | GitHub (41) | LearnTech (5) | Comunidade (1) |
|---|---|---|---|
| Arquitetura | 🟡 ADR em 13, três formatos de nome | 🟡 ADRs num arquivo só, sem C4 | 🟡 ADR 001 a 004, sem C4 |
| DevOps | ✅ CI em 40; 🟡 deploy automatizado em 7 | ✅ | ✅ |
| SecOps | ❌ `dependabot.yml` em 5, CodeQL em 0 | ❌ sem Dependabot, CodeQL nem Trivy | ✅ CodeQL, Trivy, ZAP, segredos |
| QA | ✅ Playwright em 37; 🟡 unitário em 27 | ✅ API; 🟡 sites | ✅ |
| Performance | ❌ Lighthouse CI em 0 | ✅ metas e orçamento de bundle | 🟡 orçamento e LCP, sem Lighthouse |
| Acessibilidade | ✅ axe em 36 | ✅ | ✅ |
| Mobile | 🟡 teste em 375 px em 18 | 🟡 Lighthouse mobile manual | 🟡 |
| UX | 🟡 hipótese em 40, teste com pessoas em 1 | 🟡 sem hipótese (#23) | 🟡 |
| UI | 🟡 tokens em 6; `components` sem uso | 🟡 tokens por site | 🟡 tema claro e escuro |
| Privacidade | 🟡 aviso em 5 | ✅ | 🟡 |
| Produto | 🟡 medição rara | 🟡 sem medição (#24) | 🟡 nada publicado |

O melhor de cada um, para replicar:
- **Comunidade → todos:** `varreduras.yml` (CodeQL, Trivy, ZAP), `scripts/segredos.mjs`, `dependabot.yml` com grupos, `SECURITY.md`, `incidente.md`, actions fixadas por SHA.
- **LearnTech → todos:** `CLAUDE.md` por repositório, agente medido por gabarito, Lighthouse com metas e orçamento, testes de contrato.
- **GitHub → todos:** axe no e2e, teste em 375 px, pacote de docs.

A auditoria mensal do [`ciclo-evolutivo.md`](../processo/ciclo-evolutivo.md) atualiza esta seção.
