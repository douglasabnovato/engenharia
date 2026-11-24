# MVP do engenharia

**O MVP em uma frase:** toda sessão do Claude Code no portfólio encontra, em menos de 1 minuto, a regra, o processo ou o modelo de que precisa, e cada regra tem a sua fonte (as palavras do responsável ou uma decisão).

Nível: **N2 vitrine** ([`padroes.md`](../arquitetura/padroes.md)). O repositório é só documentação, sem site e sem tela.

Conferido em 23/11/2026, às 23h, pela arquitetura de IA, a sessão dona (engenharia#56).

## Hipótese

Acreditamos que regras num lugar só, com fonte e com links testados, farão as sessões saírem menos das regras. Saberemos quando os **desvios de regra** registrados no diário do Líder de TODOS caírem para a metade da linha de base (arredondada para baixo) na semana de 24 a 30/11/2026: de 6 para 3 ou menos, ou de 5 para 2 ou menos, conforme o caso 1 abaixo [A CONFIRMAR].

**Desvio de regra:** uma entrada do diário (`orquestrador/dia-AAAA-MM-DD.md`) em que uma sessão fez uma ação que saiu de uma regra numerada (Rnn), de uma decisão ou de um critério da régua. A entrada cita a regra. Uma tentativa barrada pela permissão, sem efeito, não conta.

**Linha de base, semana de 18 a 23/11/2026:** **5 ou 6 desvios**, conforme a resposta do responsável sobre o caso 1.
- **Recontagem:** o Esp Dados recontou em 24/11, às 05h33, pela definição. Deu 6, com o caso 1 [A CONFIRMAR].
- **Pelo rótulo:** o Líder rotulou no diário os 3 casos aceitos (R19 do #59, R18 e R4). O comando abaixo dá **5** de 18 a 23/11, conferido pela dona em 24/11, às 05h34.
- **O caso 1** (restaurante-churrascaria) tem 2 leituras:
  - a hipótese fala em desvio "registrado no diário": ele foi registrado em 18/11, então **conta**, e a base é 6, com meta de 3 ou menos;
  - a definição fala em uma ação "feita" que saiu da regra: o "Atende" foi escrito antes da semana, então **não conta**, e a base é 5, com meta de 2 ou menos.

  **Pergunta ao responsável:** o caso 1 conta?

Os diários existentes são 18, 19, 20, 22 e 23/11. Não há diário de 17 nem de 21/11.

| Data | Desvio | Regra |
|---|---|---|
| 18 e 19/11 | **caso 1 [A CONFIRMAR]:** o restaurante-churrascaria dizia "Atende" no critério 9, com uma chave exposta. Foi achado em 18/11 e corrigido em 19/11 | critério 9 de `padroes.md` |
| 23/11 | o engenharia#59 entrou na sprint sem a revisão R19 | R19 |
| 23/11 | 11 escritas no GitHub, sem simulação, 1 acima do limite | R18 |
| 23/11 | uma ORDEM colada no canal errado foi executada por uma sessão que não era a dona (diário de 23/11, atualização da LearnTech às 19h: "ele colou a ordem na sessão GitHub, e não na LearnTech"; "Desvios: (1) R4") | R4 |
| 23/11 | o formacao-dev#338 mudou código (`scripts/triagem.mjs`) e entrou na sprint só com autorrevisão, que a decisão 144 permite só em PR de documentação (rotulado no diário, `Desvio (R19/144)`) | R19, decisão 144 |
| 23/11 | a arquitetura de IA fez 13 escritas no GitHub num ciclo, sem simulação (rotulado no diário, `Desvio (R18)`) | R18 |

**Como contar:** o Líder marca cada caso no diário com `**Desvio (Rnn):**` (adotado em 23/11/2026, às 23h09). O total da semana sai de:

```
cat dia-2026-11-2[4-9].md dia-2026-11-30.md 2>/dev/null | grep -c '^- \*\*Desvio (\(R[0-9]\|[0-9]\|[Dd]ecisão\|critério\)'
```

Só conta o rótulo no começo de um item da lista. Uma linha que só explica o rótulo não conta. O padrão aceita `Rnn`, número, `Decisão` (por exemplo, `Desvio (Decisão 150)`) e `critério`. Um rótulo sem regra numerada, decisão ou critério, como `Desvio (hora)` ou `Desvio (R-Diário, ...)`, não conta, pela definição acima (achado 1 da R19 do Esp Dados no engenharia#73).

**Mesma régua nas 2 semanas:** a linha de base foi contada à mão pela dona; a meta será contada pelo rótulo. Na 1ª contagem, o Esp Dados reconta a semana de 18 a 23/11 com a mesma definição. A recontagem de 24/11 confirmou 5 casos certos e 1 [A CONFIRMAR], e a linha de base fica pela resposta do responsável (passo 1 do [`ROADMAP.md`](../ROADMAP.md)).

## Os 12 critérios

| # | Critério | Situação | Evidência (comando, data e resultado) |
|---|---|---|---|
| 1 | Problema e público claros | Atende | A 1ª frase do [`README.md`](../README.md) diz o que é e para quem: "Base central de engenharia do portfólio ... vale para todos os repositórios" |
| 2 | Hipótese a validar | **Parcial** | A hipótese tem meta, definição e linha de base (5 ou 6, conforme o caso 1 [A CONFIRMAR]). Fica Parcial até o rótulo `Desvio (Rnn)` entrar no modelo do diário do Líder e a 1ª contagem sair (passo 1 do roteiro) |
| 3 | Fluxo principal completo | Não se aplica: não há tela | O fluxo é "achar a regra". No lugar do e2e, o CI `verificar` confere todos os links internos. Execução 45307074709, de 23/11/2026, na sprint: sucesso |
| 4 | Escopo enxuto | Atende | a seção "Fora do MVP", abaixo |
| 5 | Medição de uso | Parcial | Não há painel de visitas, porque o repositório não tem site. A medida é a da hipótese: o diário do Líder. PRs mesclados desde 17/11: 27 (`gh api .../pulls?state=closed`, 24/11/2026, às 17h50) |
| 6 | Falhas tratadas | Parcial | Não há tela. Os scripts tratam entrada ruim: o hook passa sem travar com JSON inválido (`test_entradas_estranhas_nao_travam`, ok na execução 45307074709 do CI, em 23/11/2026), e o `verificar_links.mjs` sai com 1 quando a pasta não existe (teste `linha de comando: pasta inexistente sai com 1`, ok na execução 45309548627 do CI, em 23/11/2026) |
| 7 | Desempenho aceitável | Não se aplica: sem site publicado | — |
| 8 | Acessibilidade básica | Não se aplica: sem tela | — |
| 9 | Segurança e conformidade | Parcial | Não há dependência de pacote nem `package.json`. Busca por segredos em 23/11/2026, com o comando abaixo da tabela: 0 linhas. O Dependabot está desligado (`gh api .../dependabot/alerts`: 403, "disabled"), que é o caso da engenharia#33. As actions do CI estão fixadas por SHA desde o #76 (24/11/2026). |
| 10 | Entrega confiável | **Parcial** | Há CI nos PRs. A `main` **não tem proteção**: `gh api repos/douglasabnovato/engenharia/rules/branches/main` devolveu `[]`, e `branches/main` deu `protected: false` (23/11/2026). Criar o ruleset é do responsável (R12, [`fluxo-git.md`](../processo/fluxo-git.md)) Reconferido em 24/11/2026, às 17h50: ainda `[]`. Desde o #71, o CI também roda no push da `main`, e o C3 da medida passa a ser medido depois do merge semanal. |
| 11 | Testes dos fluxos críticos | Atende | Os testes do hook e do `verificar_links` rodam no CI, sem `skipped`. Última execução na sprint: 45464532236, em 24/11/2026, com 10 de 10 testes Node e os testes do hook, 0 skipped |
| 12 | Documentação honesta | Atende | Em 23/11/2026: `node scripts/verificar_links.mjs` deu "Links internos quebrados: 0"; os 2 comandos da seção "No Acer" do [`scripts/README.md`](../scripts/README.md) rodaram (0 quebrados; testes 10 de 10); todo script da tabela existe (`ls scripts scripts/hooks`) |

**Resultado:** 4 atendem, 5 são parciais e 3 não se aplicam (12).

Busca por segredos do critério 9:

```
git grep -nIiE "(api[_-]?key|token|secret|senha)\s*[:=]\s*['\"][A-Za-z0-9_\-]{16,}"
```

## Na medida MVP de 4 critérios (rascunho)

Pela régua de 4 critérios do [`medida-mvp.md`](../processo/medida-mvp.md), que está [A CONFIRMAR]:

| Critério | Situação |
|---|---|
| C1 MVP escrito | atende, com este arquivo |
| C2 no ar | não se aplica: só documentação. A régua precisa da exceção "repositório sem site", como o de perfil |
| C3 CI verde na principal | não atende: o CI não roda no push da `main`, só nos PRs para ela |
| C4 README vitrine | atende em parte: tem o que é e como consultar, mas não tem link, porque não há site |

Daqui saem 2 perguntas para a medida MVP: a exceção do C2 para repositório só de documentação, e se o C3 aceita o CI verde do último PR mesclado na `main`.

## Fora do MVP

- site publicado ou documentação em página (é só Markdown);
- o empacotamento como plugin (engenharia#54);
- os gabaritos medidos dos agentes (engenharia#57);
- qualquer coisa da VEB (R10).
