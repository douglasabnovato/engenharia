# Decisão de 23/11/2026 · 138: merge na integração pela sessão dona

**Quem conduziu:** o Líder de TODOS. **Quem registra:** a arquitetura de IA, dona do `engenharia` (R4).

**Palavras do responsável** (23/11, 15h25, no chat do Líder): "Aprovo a 138".

**Documento de base:** `orquestrador/revisao-processos-2026-11-23.md`, seção 4, proposta 138 (nota 4,7 na matriz).

## Decisão

A R21 ("código só com a ordem direta dele") vale para duas coisas: a produção (sprint → principal) e a configuração. O merge na integração faz parte do plano aprovado (R22).

| PR | Quem mescla | Condição |
|---|---|---|
| feature → sprint | a sessão dona, numa tentativa | CI verde e revisão do Esp da disciplina (R19); registro no Diário. Se a permissão negar, o PR fica com `revisao-responsavel` e a sessão não contorna |
| sprint → principal | só o responsável, uma vez por semana, na quinta do fechamento da sprint | CI verde e revisão |

## Por quê

- **Fato:** a fila "Com você" tinha cerca de 32 PRs. Boa parte era feature → sprint com CI verde, à espera só do clique dele.
- **Efeito esperado:**
  - a fila cai para cerca de 7 PRs, os da produção e os de configuração;
  - o Executado do Diário sobe no mesmo dia.

## O que não muda

- Segredos, contas, deploy que exige conta dele e custo (R12).
- O repositório sob curadoria, `douglasabnovato.dev` (R20): mudança item a item, com o ok dele.
- Mudança de regra (`ia/orquestracao.md`, `CLAUDE-raiz.md`, definições de agentes e skills): o texto é do responsável, então o merge na sprint é com o ok dele, mesmo com CI verde e revisão R19 (achado 12 da Esp PM).
- As permissões e as regras de negação do app prevalecem sobre esta decisão.

Onde foi aplicada: [`processo/fluxo-git.md`](../processo/fluxo-git.md), "Quem pode mesclar o quê".
