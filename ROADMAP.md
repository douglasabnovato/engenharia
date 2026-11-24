# Roteiro do engenharia

Atualizado em 23/11/2026 pela arquitetura de IA (engenharia#56). O MVP e os 12 critérios estão em [`docs/MVP.md`](docs/MVP.md).

Prioridade: **P0** destrava outras sessões · **P1** fecha um critério do MVP · **P2** melhora.

| # | Passo | Prioridade | Issue ou PR | Depende de |
|---|---|---|---|---|
| 1 | Mesclar a cadeia #50 → #51 → #53 (R19 a R24, agentes e estudos) | P0 | engenharia#50, #51 e #53 | o responsável (muda regra) |
| 2 | Proteger a `main` com o ruleset `principal-protegida` (critério 10) | P0 | — | o responsável (R12) |
| 3 | Verificação no Acer sem Python | P1 | engenharia#66 (#58) | a revisão do Esp QA e o merge |
| 4 | Merge só na integração por hook (P3 da fila da noite) | P1 | engenharia#67 | a escolha do responsável entre a P1 e a P3, e ligar o hook (#17) |
| 5 | Registro da arquitetura de codes | P1 | engenharia#68 (#55) | o ok do responsável; depois, a orquestracao.md |
| 6 | ATIVAÇÃO permanente não é ORDEM | P1 | engenharia#65 | a confirmação do responsável |
| 7 | Medida MVP de 4 critérios para o painel | P1 | `processo/medida-mvp.md` | as 3 perguntas ao responsável |
| 8 | Decidir o critério 9 sem Dependabot | P1 | engenharia#33 | — |
| 9 | Gabarito medido do agente `secops` | P2 | engenharia#57 | o passo 1 (o agente entra pelo #50) |
| 10 | Empacotar o engenharia como plugin para as 4 pastas | P2 | engenharia#54 | o passo 1 |
| 11 | Agentes `dados` e `devrel` (lacunas da arquitetura de codes) | P2 | a abrir depois do passo 5 | o ok do responsável |
