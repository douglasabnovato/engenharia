# Ciclos por repositório

Uma ficha por ciclo, para comparar os repositórios e melhorar o processo. Pedido do responsável em 15/11/2026: "precisamos documentar as evolucoes e processos e engenharia de software para analsiarmos e aperfeicoarmos os processos de desenvolvmentos a cada repositorio trabalhado".

A sessão dona manda a ficha ao orquestrador no aviso de fim de cada repositório. O orquestrador grava aqui, pela sprint, com CI verde. O detalhe de cada ciclo fica no próprio repositório (PR, `docs/MVP.md` e issues).

## Modelo da ficha

```
### <repositório> · <data> · <sessão>
- Tipo: ciclo de MVP | verificação | correção
- Antes: critérios X de Y · PRs esperando o responsável: N · principal = produção? sim/não
- Feito: PRs (número, merge, jobs do CI) · issues fechadas com evidência
- Revisão independente: N achados (tipo) · corrigidos: N
- Revisão de fatos (se houver texto): N achados
- Depois: critérios X de Y · em produção? sim/não, como foi conferido
- Com o responsável: issues, na ordem
- O que travou: permissão, CI, conta, decisão
- Lição para o processo: 1 linha, com o item proposto para ia/aprendizados.md
```

Datas e horas sempre no horário de Brasília (`date` no Git Bash).

## Painel

| Data | Repositório | Tipo | Revisão independente (achados) | Chegou à produção no dia? | Itens com o responsável |
|---|---|---|---|---|---|
| 15/11/2026 | aircnc | verificação | — | sim (#106 e #107) | 0 |
| 15/11/2026 | instagram-feed | ciclo de MVP | 2 | sim (#98) | 1 (#104) |
| 15/11/2026 | dev-radar | ciclo de MVP | 5 | não | 3 (#72, #61, #69) |
| 15/11/2026 | valoriza | ciclo de MVP | 4 | não | 4 (#20, #11, #16, #22) |

Leitura de 15/11: nos 3 ciclos de MVP, a revisão independente achou 11 erros, todos antes do merge na sprint. Os 2 repositórios que chegaram à produção no dia foram os em que o responsável mesclou durante a verificação, junto com a sessão.

## Fichas

### aircnc · 15/11/2026 · DG github, com o responsável
- Tipo: verificação manual.
- Antes: a sprint estava 4 commits à frente da `master`, só em `Readme.md` e `docs/MVP.md`. 2 PRs esperando o responsável (#106 e #107).
- Feito: o responsável mesclou #106 (515dc50) e #107 (b652762), CI da `master` verde nos dois. #109 fechada com evidência.
- Depois: produção = `master`, conferida pelo pacote publicado igual ao build local; site, `/health` e `/spots` com 200. Nenhum PR aberto.
- Com o responsável: nada. #97 (Expo 58) segue no backlog.
- O que travou: o Dependabot do `minimatch` em `/mobile` falhou, porque rebaixaria o Expo para 52; registrado na #90.
- Lição: comparar o pacote publicado com um build local, sem `\r`; Dependabot que exige rebaixar vai para a issue de migração.

### instagram-feed · 15/11/2026 · DG github
- Tipo: ciclo de MVP, a pedido do responsável ("analise planeje execute meça e revise ... até a gente estar com um mvp de qualidade").
- Antes: 7 PRs esperando o responsável; os critérios 3 e 8 estavam em "Atende" só com testes em jsdom, sem Playwright nem axe; credencial antiga no histórico (#85).
- Feito: #100 na sprint (33a429f), 4 jobs verdes, com um e2e novo. O responsável mesclou #98, criou um usuário de banco com acesso só ao banco do app e o Blueprint do Render. #86, #87, #89 e #90 fechadas com evidência; #91 no merge.
- Revisão independente: 2 erros, corrigidos.
- Depois: em produção; site, `/health` e `/posts` com 200 e o pacote publicado igual ao da `master`.
- Com o responsável: #104. A #85 fechou às 23h50, com a remoção dos usuários antigos confirmada pelo responsável. A #88 fechou com a decisão de congelar o app móvel antigo (ADR 0001; migração na #105).
- Lição: conferir cada "Atende" contra a coluna de evidência da régua; em teste de tempo real, esperar o sinal de conectado; `aria-label` diferente do texto visível quebra a WCAG 2.5.3.

### dev-radar · 15/11/2026 · DG github
- Tipo: ciclo de MVP.
- Antes: 4 PRs do Dependabot parados; usuário antigo do banco com acesso a todo o cluster.
- Feito: #75 na sprint (545e171), 4 jobs verdes (backend, web, mobile e e2e). Critérios 10 de 10 com evidência de 15/11.
- Revisão independente: 5 erros de documentação e teste, corrigidos.
- Depois: na sprint, não na produção.
- Com o responsável: #72 (sprint → `master`, fecha 76 alertas do app antigo), #61 (publicação), #69 (abrir o app num aparelho).
- Lição: teste de tema escuro só vale se o CSS tiver `prefers-color-scheme`.

### valoriza · 15/11/2026 · DG github
- Tipo: ciclo de MVP.
- Antes: banco com 9 usuários e e-mails reais no histórico (#11).
- Feito: #23 na sprint (76d947d), job `raiz` verde. Entraram paginação (#13), OpenAPI com teste nos dois sentidos (#15) e a hipótese com meta. Issue nova #22.
- Revisão independente: 4 erros, corrigidos.
- Depois: na sprint, não na produção.
- Com o responsável: #20 (sprint → `main`), #11, #16 (publicação da API), #22 (alertas do Dependabot).
- Lição: datar a evidência com a data local, não com a UTC.
