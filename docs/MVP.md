# MVP do engenharia

**O MVP em uma frase:** toda sessão do Claude Code no portfólio encontra, em menos de 1 minuto, a regra, o processo ou o modelo de que precisa, e cada regra tem a sua fonte (as palavras do responsável ou uma decisão).

Nível: **N2 vitrine** ([`padroes.md`](../arquitetura/padroes.md)). O repositório é só documentação, sem site e sem tela.

Conferido em 23/11/2026, às 23h, pela arquitetura de IA, a sessão dona (engenharia#56).

## Hipótese

Acreditamos que regras num lugar só, com fonte e com links testados, farão as sessões errarem menos regra. Saberemos quando o número de correções do tipo "regra mal lida" no diário do Líder de TODOS cair pela metade em 2 semanas, contra a semana de 17 a 23/11/2026.

## Os 12 critérios

| # | Critério | Situação | Evidência (comando, data e resultado) |
|---|---|---|---|
| 1 | Problema e público claros | Atende | A 1ª frase do [`README.md`](../README.md) diz o que é e para quem: "Base central de engenharia do portfólio ... vale para todos os repositórios" |
| 2 | Hipótese a validar | Atende | a seção "Hipótese", acima |
| 3 | Fluxo principal completo | Não se aplica: não há tela | O fluxo é "achar a regra". No lugar do e2e, o CI `verificar` confere todos os links internos. Execução 45307074709, de 23/11/2026, na sprint: sucesso |
| 4 | Escopo enxuto | Atende | a seção "Fora do MVP", abaixo |
| 5 | Medição de uso | Parcial | Não há painel de visitas, porque o repositório não tem site. A medida é a da hipótese: o diário do Líder. PRs mesclados desde 17/11: 10 (`gh api .../pulls?state=closed`, 23/11/2026) |
| 6 | Falhas tratadas | Parcial | Não há tela. Os scripts tratam entrada ruim: o hook passa sem travar com JSON inválido (`test_entradas_estranhas_nao_travam`), e o `verificar_links.mjs` sai com 1 quando a pasta não existe (PR #66) |
| 7 | Desempenho aceitável | Não se aplica: sem site publicado | — |
| 8 | Acessibilidade básica | Não se aplica: sem tela | — |
| 9 | Segurança e conformidade | Parcial | Não há dependência de pacote nem `package.json`. Na busca por segredos (`git grep` de chave, token e senha, 23/11/2026), nada achado. O Dependabot está desligado (`gh api .../dependabot/alerts`: 403, "disabled"), que é o caso da engenharia#33 |
| 10 | Entrega confiável | **Parcial** | Há CI nos PRs. A `main` **não tem proteção**: `gh api repos/douglasabnovato/engenharia/rules/branches/main` devolveu `[]`, e `branches/main` deu `protected: false` (23/11/2026). Criar o ruleset é do responsável (R12, [`fluxo-git.md`](../processo/fluxo-git.md)) |
| 11 | Testes dos fluxos críticos | Atende | Os testes do hook e do `verificar_links` rodam no CI, sem `skipped` no log da execução 45307074709 |
| 12 | Documentação honesta | Atende | Os comandos do [`scripts/README.md`](../scripts/README.md) foram conferidos nos scripts, e os links foram conferidos pelo CI |

**Resultado:** 5 atendem, 4 são parciais e 3 não se aplicam (12).

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
