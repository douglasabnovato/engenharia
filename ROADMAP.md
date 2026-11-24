# Roteiro do engenharia

Atualizado em 23/11/2026 pela arquitetura de IA (engenharia#56). O MVP, a hipótese e os 12 critérios estão em [`docs/MVP.md`](docs/MVP.md).

**Prioridade:**
- **P0:** destrava outras sessões ou fecha um risco;
- **P1:** fecha um critério do MVP ou mede a hipótese;
- **P2:** melhora.

A coluna "Ganho" diz que critério fecha ou que métrica move.

## Bloco A · com a dona e o Líder (não esperam o responsável)

| # | Passo | Prioridade | Ganho | Issue ou PR | Quem faz |
|---|---|---|---|---|---|
| 1 | Pôr o rótulo `Desvio (Rnn)` no modelo do diário e contar a 1ª semana (24 a 30/11) contra a linha de base de 4 | P1 | mede a hipótese e fecha o critério 2 | a abrir | o Líder, que é dono do diário, com a dona, que conta e registra aqui |
| 2 | Ajustes 1 e 4 do pm (hipótese só no `pm`; North Star no topo do `docs/MVP.md`) | P1 | menos duplicata na revisão; North Star medida | depois da cadeia, no passo 7 | a arquitetura de IA |
| 3 | Gabarito medido do agente `secops` | P2 | autonomia medida (recall e falso positivo) | engenharia#57 | a arquitetura de IA, depois do passo 7 |
| 4 | Empacotar o engenharia como plugin para as 4 pastas | P2 | menos regra copiada à mão | engenharia#54 | a arquitetura de IA, depois do passo 7 |

## Bloco B · esperam o responsável (a fila real, em ordem)

| # | Passo | Prioridade | Ganho | Issue ou PR |
|---|---|---|---|---|
| 5 | Proteger a `main` com o ruleset `principal-protegida` | P0 | critério 10; é condição da P3 | — (R12) |
| 6 | Confirmar que a ATIVAÇÃO permanente não é ORDEM | P0 | o ciclo evolutivo roda sem dúvida de regra | engenharia#65 |
| 7 | Mesclar a cadeia #50 → #51 → #53 (R19 a R24, agentes e estudos) | P0 | menos desvio de regra (hipótese); destrava os passos 2, 3 e 4 | engenharia#50, #51 e #53 |
| 8 | Responder às 3 perguntas da medida MVP, incluindo as exceções C2 e C3 deste repositório | P1 | régua única no painel | `processo/medida-mvp.md` |
| 9 | Decidir o critério 9 sem Dependabot: ligar ou aceitar o risco | P1 | critério 9 | engenharia#33 |
| 10 | Decidir a divergência do Esp no GitHub (Decisão LIDER 149) | P1 | papéis sem contradição | `ia/arquitetura-de-codes.md` |
| 11 | P3 (merge só na integração por hook): só depois de Python instalado, do hook testado ligado e do passo 5 | P2 | a 138 sem ORDEM por merge | engenharia#67 (em espera, Decisão LIDER 148) |
| 12 | Agentes `dados` e `devrel` (lacunas da arquitetura de codes) | P2 | revisão de Dados e de DevRel | a abrir depois do passo 10 |

Já feito em 23/11/2026: a verificação no Acer sem Python (engenharia#66) e o registro da arquitetura de codes (engenharia#68), os dois mesclados na sprint.
