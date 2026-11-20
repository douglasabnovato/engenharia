# Mudanças nas regras

Toda mudança de regra, processo, skill, agente ou hook do `engenharia`, da mais nova para a mais antiga. Cada linha cita o PR e a decisão. O ciclo semanal de [`processo/ciclo-evolutivo.md`](processo/ciclo-evolutivo.md) acrescenta uma linha por melhoria.

Tipos: **Novo**, **Mudou**, **Removido**, **Corrigido**.

## 20/11/2026 · laboratório de IA

Ordem do responsável: "arquitetura de ia é para estudar claude ia e metologias e ferramentas para desenvolver projetos de softwares e produtos digitais usando esses contextos".

- **Novo:** [`ia/estudos/`](ia/estudos/README.md), trilha de 9 estudos, cada um com experimento num contexto real e métrica:
  1. contexto e memória;
  2. skills, subagentes e hooks;
  3. MCP;
  4. tarefas agendadas e workflows;
  5. Claude API e Agent SDK;
  6. prompt e contexto;
  7. avaliação;
  8. metodologias;
  9. custo e desempenho.
- **Novo:** [`ia/avaliacoes/`](ia/avaliacoes/README.md), com o formato dos gabaritos dos agentes e a situação de cada um.
- **Novo:** 3 revisores de conteúdo, só de leitura, para o learnTECH: `revisor-pedagogia`, `revisor-storytelling` e `revisor-marketing`.
- **Novo:** do estudo ao artigo, uma proposta por semana para a sessão repositórios LearnTech publicar.

## 20/11/2026 · governança da arquitetura de IA (F1)

Decisão: [`decisoes/2026-11-20-governanca-ia.md`](decisoes/2026-11-20-governanca-ia.md).

- **Mudou:** nomes, pastas e siglas reais das sessões. Líder de TODOS (`LIDER`), arquitetura de IA (`IA`), repositórios LearnTech (`MUNDO`), comunidade LearnTech (`COMUNIDADE`), repositórios GitHub (`GITHUB`) e DG veb (`VEB`, prevista).
- **Mudou:** R4. O `engenharia` passa a ser da arquitetura de IA; o Líder de TODOS escreve ali só `relatorios/` e `decisoes/`, por PR.
- **Novo:** R1a "recomendar e agir": a sessão que espera o responsável pergunta ao LIDER, que decide pela matriz ("Decisão LIDER Dnn") e registra no relatório; o responsável revisa. Fora: ação irreversível, R12, R20, publicação em nome dele, regra editorial e A1 a A3. Vale por sessão, depois da colagem do texto pelo responsável, e não muda as permissões do app.
- **Novo:** R18 (ação em massa só com simulação e ok) e R19 (revisão pelo especialista da disciplina).
- **Novo:** R20, repositório sob curadoria do responsável (hoje só o `douglasabnovato.dev`): fora de lote e automação, mudança item a item com o ok dele, nenhum fato sem evidência dada por ele.
- **Novo:** [`arquitetura/disciplinas.md`](arquitetura/disciplinas.md), com o padrão N1/N2/N3 de 12 disciplinas.
- **Novo:** [`processo/ciclo-evolutivo.md`](processo/ciclo-evolutivo.md), com os ciclos diário, semanal e mensal, o pós-incidente, os portões de qualidade, o orçamento de performance e as métricas.
- **Novo:** 11 agentes especialistas, só de revisão: `arquiteto`, `devops`, `secops`, `ux`, `ui`, `mobile`, `qa`, `performance`, `a11y`, `privacidade` e `pm`.
- **Corrigido:** contradição entre `processo/modelo-issue.md` e a skill `issue-no-modelo` sobre preencher os campos do Project.
- **Corrigido:** horário da abertura do dia (6h30, não 7h) em `ia/arquitetura-ia.md` e `ia/recursos.md`.

## Antes de 20/11/2026

As mudanças anteriores estão nas decisões datadas de [`decisoes/`](decisoes/) e no histórico do Git.
