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

| Data | Repositório | Tipo | Critérios: declarado → pela régua → depois | Revisão independente (achados) | Chegou à produção no dia? | Itens com o responsável |
|---|---|---|---|---|---|---|
| 15/11/2026 | aircnc | verificação | — | — | sim (#106 e #107) | 0 |
| 15/11/2026 | instagram-feed | ciclo de MVP | 3 e 8 só com jsdom → corrigidos | 2 | sim (#98) | 1 (#104) |
| 15/11/2026 | dev-radar | ciclo de MVP | → 10/10 | 5 | não | 3 (#72, #61, #69) |
| 15/11/2026 | valoriza | ciclo de MVP | — | 4 | não | 4 (#20, #11, #16, #22) |
| 15/11/2026 | learntech-content | processo | 7/12 → 7/12 | não rodou | não | 6 |
| 16/11/2026 | oxe-online | ciclo de MVP | 10 → 9 → 10 | 3, depois do merge | não (Pages desligado) | 4 (#18, #19, #20, Pages) |
| 16/11/2026 | proffy | ciclo de MVP | 9 → 7 → 8 | 5, depois do merge | não | 4 (#37, #26, #27, #28) |
| 16/11/2026 | niky | ciclo de MVP | 10 → 7 → 10 | 3, depois do merge | não | 5 (#30, #21, #34, #33, #23) |
| 16/11/2026 | biblioteca | ciclo de MVP | 9 → 9 → 10 | 6, antes do merge | no ar, privado | 3 (#15, #4, #12) |
| 16/11/2026 | huntweb-swapi | ciclo de MVP | 10 → 8 → 10 | 2, antes do merge | não (Pages desligado) | 3 (#36, #38, Pages) |
| 16/11/2026 | sushibar | ciclo de MVP | 10 → 6 → 10 | 5, antes do merge | não (Pages desligado) | 4 (Pages, #24, #25, #15) |
| 16/11/2026 | doe-sangue-salve-vidas | ciclo de MVP | 10 → 7 → 9 | 3, antes do merge | não | 4 (#22, #23, #24, #16) |
| 16/11/2026 | casa-criativa | ciclo de MVP | 10 → (tema escuro falso) → 10 | 5, antes do merge | não | 2 (#65, #47) |
| 16/11/2026 | calculadora | ciclo de MVP | 9 → 6 → 9 (9 Parcial) | 4, antes do merge | sim (Netlify, #29) | 5 (#37, #18, #30, #31, #23) |
| 16/11/2026 | be-the-hero | ciclo de MVP | 9 → 8 → 9 | 2, antes do merge | não | 3 (#37, #15, #17) |
| 16/11/2026 | jobs-calc | ciclo de MVP | 9 → (escuro inexistente) → 9 | 2, antes do merge | não | 5 (#31, #10 e #20, #26, #11, #12) |
| 16/11/2026 | cm-quiz-app | ciclo de MVP | 9 → 8 → 8 (Finalizado sim) | 0 | não | 4 (#37, #14, #16, #32) |
| 16/11/2026 | letmeask | ciclo de MVP | 9 → 7 → 9 | 3, antes do merge | não (build antiga no ar) | 7 (#27, #12, #17, #14, #22, #23, #24) |
| 16/11/2026 | petshop | ciclo de MVP | 10 → 7 → 9 | 3, antes do merge | não (Pages desligado) | 2 (Pages, #21) |
| 16/11/2026 | rocket-q | ciclo de MVP | 10 → 6 → 9 | 4, antes do merge | não (o link serve outro código) | 4 (#21, #17, #18, #20) |
| 16/11/2026 | my-money-app | ciclo de MVP | 10 → 7 → 9 | 2, antes do merge | não | 5 (#36, #29, #30, #18, #17 e #26) |
| 16/11/2026 | dashboards | ciclo de MVP | 10 → (8 e 9 inflados) → 9 | 0 | versão anterior no ar; entra com o #28 | 4 (#28, #23, #10, #19) |
| 16/11/2026 | aula-de-programacao | ciclo de MVP | 9 → 8 → 9 | 2, antes do merge (1 contestado com evidência) | versão anterior no ar; entra com o #36 | 5 (#36, #33, #21, #29, #25 e #26) |
| 16/11/2026 | douglasabnovato (perfil) | ciclo de MVP | 9 → (8 e 9 sem evidência) → 8 | 5 (1 recusado com o porquê) | versão anterior no ar; entra com o #62 | 6 (#62, #56, #46, #47, #57, #44) |
| 16/11/2026 | ux-design | ciclo de MVP | 9 → 8 → 9 | 3, antes do merge | versão anterior no ar; entra com o #50 | 6 (#46, #31, #50, #45, #47, #41) |

Leitura de 15/11: nos 3 ciclos de MVP, a revisão independente achou 11 erros, todos antes do merge na sprint. Os 2 repositórios que chegaram à produção no dia foram os em que o responsável mesclou durante a verificação, junto com a sessão.

Leitura da madrugada de 16/11 (8 ciclos de MVP):
- **A nota declarada era maior que a evidência em 6 de 7 repositórios medidos**, por 1 a 4 critérios (média 2,5). O caso mais comum: critérios 3 e 8 em "Atende" sem Playwright nem axe no CI, e testes citados no `MVP.md` que não existiam.
- **A revisão independente achou 32 erros em 8 repositórios** (média 4). Nos 3 primeiros ela rodou depois do merge e exigiu PR de correção; depois que virou regra do brief, rodou antes, e nada errado chegou à sprint.
- **Teste de tema escuro falso em 5 repositórios**, embora o aprendizado já estivesse escrito: os agentes liam o `aprendizados.md` de um clone local de 09/11.
- **Nenhum chegou à produção no dia.** O gargalo mudou: depois dos 33 merges na principal, o que falta é hospedagem (Pages desligado, Render com nome de outra conta, Streamlit privado), não merge.

Leitura do lote 3 (16/11, 01h20–02h10, 6 ciclos):
- A diferença entre a nota declarada e a régua continua (1 a 3 critérios), mas a revisão independente rodou antes do merge em todos, com 0 a 4 achados.
- Em 2 repositórios (calculadora e letmeask), o agente manteve um achado da revisão sem corrigir. Desde 02h08, o brief diz: achado não corrigido vai com o porquê no PR, e o PR não é mesclado sem a DG github decidir.
- O critério 9 foi revisto em 14 repositórios pela regra segura da engenharia#33: 7 voltaram para Parcial, 1 ficou "Parcial até o merge", 4 seguem Atende com contagem atual.

Leitura do lote 4 (16/11, 02h10–03h05, 6 ciclos):
- A revisão independente achou 0 a 5 erros por repositório, e em 2 deles (dashboards e cm-quiz-app, antes) nenhum. Pela primeira vez, 2 achados foram contestados com evidência e decididos pela DG github, como pede o brief desde 02h08.
- Repositórios no ar (aula-de-programacao, dashboards, perfil, ux-design) seguem com a versão anterior até o merge na principal.
- Dados de terceiros voltaram a aparecer: imagens do catálogo do ux-design (#46), em site público.

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

### learntech-content · 15/11/2026 · DG mundo
- Tipo: ciclo de processo (método de produção a partir do hd, entregas 1 a 3 e rodada 4 do gabarito), a pedido do responsável.
- Antes: critérios 7 de 12 · PRs esperando o responsável: 0 (a integração vai em bloco) · principal = produção? sim, sem o lote desta noite.
- Feito: 11 commits na `developer` por ff-only, CI verde em cada um (1b43257 a a555120): ficha de análise, perfil do autor, registro de decisões (D-01 a D-11, P-01 a P-09, confirmados), níveis AU0 a AU2, rodada 4 do gabarito e D-11 aplicada a 9 itens do acervo. Issues novas: #29 (triagem de 94 issues) e #30 (datas em UTC em 6 scripts).
- Revisão independente: não rodou. Falha do ciclo, registrada pela própria sessão.
- Revisão de fatos: não rodou; o perfil do autor está marcado "a confirmar".
- Depois: critérios 7 de 12, sem mudança (ciclo de processo) · em produção? não; a `developer` está 31 commits à frente da `main`.
- Com o responsável: levar a `developer` para a `main`; aprovar os grupos da #29; confirmar HD-0049 e HD-0054; confirmar os níveis e as lacunas do perfil; motivo da D-11 (opcional); depois, o AU1.
- O que travou: datas em UTC (toISOString e TZ do Git Bash sem zoneinfo), corrigidas em 5d82d5e e a555120.
- Lição: gabarito de agente é revisado junto com a medição; erro concentrado num tipo pode ser da regra, não do agente.

### oxe-online · 16/11/2026 · DG github (lote 1)
- Tipo: ciclo de MVP; N1, React com Vite e MUI, site estático no Pages.
- Antes: 10/10 no papel, mas o critério 3 sem teste de navegador; `npm audit` com 4 alertas de desenvolvimento; 1 PR esperando o responsável (#18); principal fora do ar (Pages desligado, 404).
- Feito: #22 na sprint (6112af4), CI verde (Vitest 11, Playwright 8, nada pulado). Entraram: teste do fluxo com axe no claro, no escuro e em 375 px; filtro "Aceita remoto" (`?remoto=1`); `npm audit fix`; `dependabot.yml`; limpeza do CRA antigo; plano com 3 fontes; MVP com evidência.
- Revisão independente: depois do merge do #22, a pedido do orquestrador (a autorrevisão não conta). 3 erros: axe no "escuro" repetia o claro (o app não tem tema escuro); risco do `public/index.html` desatualizado; critério 11 sem o link do run. Mais 2 sugestões de espera estável nos testes. Tudo corrigido no #23 (run 43798030035, `raiz` verde).
- Depois: 10/10 com evidência; 8 issues abertas (#19, #20 e #21 novas); fora do ar até ligar o Pages.
- Com o responsável: Settings → Pages → Source = GitHub Actions antes de mesclar o #18; mesclar o #18; decidir o texto do aviso de estudo (#19); ligar os alertas do Dependabot (#20).
- O que travou: o Pages desligado (#11).
- Lição: `public/index.html` que sobra do CRA num projeto Vite vai para o build; apagar e conferir o `build/index.html`.

### proffy · 16/11/2026 · DG github (lote 1)
- Tipo: ciclo de MVP; N1, Node 22 + Express 4 + Nunjucks + SQLite.
- Antes: declarava 9/10, mas pela régua era 7/10 (critérios 3 e 8 só com evidência local); #37 esperando o responsável; fora do ar.
- Feito: #40 na sprint (20fc534): job e2e com Playwright e axe, contraste do botão Estudar, filtro por preço máximo (#30), plano, MVP e DEPLOY refeitos. Correção #45 (1915077), `raiz` 13/13 e `e2e` 3, verdes.
- Revisão independente: depois do merge (a regra chegou depois). 5 erros: contorno do botão sumia no fundo; dois testes passavam na página antiga, antes da navegação; tema escuro falso; critério 10 "Atende" sem os checks exigidos no ruleset. Todos corrigidos no #45.
- Depois: 8/10 com evidência, Finalizado sim (9 e 10 dependem do responsável) · fora do ar: o `render.yaml` usa `proffy-estudo`, porque `proffy.onrender.com` é de outra pessoa.
- Com o responsável: mesclar o #37; Blueprint no Render (#26); `raiz` e `e2e` obrigatórios no ruleset (#27); banco de telefones no histórico (#28).
- O que travou: no Windows, o `npm ci` local falhou ao compilar o better-sqlite3 11; o CI passou.
- Lição: teste "escuro" no Playwright só vale com `prefers-color-scheme` no CSS; a revisão achou o falso teste nos três repositórios do lote 1, embora o aprendizado já estivesse escrito.

### niky · 16/11/2026 · DG github (lote 1)
- Tipo: ciclo de MVP; N1, React 18 + Vite, Express 4 + SQLite.
- Antes: declarava 10/10, mas pela régua era 7/10 (hipótese sem meta; critério 3 sem Playwright no CI; axe à mão); #30 esperando o responsável; fora do ar.
- Feito: #32 na sprint (`developer-sprint-2026-11-12`, dfbef94): e2e com Playwright e axe pela API real, teclado e falha de rede; contraste do "Tentar novamente"; foco na mensagem depois de excluir; Bootstrap 5.3.9; docs refeitos. Correção #37 (run 43797667257: raiz 16, api 8, e2e 3).
- Revisão independente: depois do merge. 3 erros: tema escuro falso; teste "só teclado" usava `.focus()`; datas divergentes. Corrigidos no #37, que também guarda `test-results` quando falha.
- Depois: 10/10 com evidência · fora do ar: o front dá 200 com build antigo, e `niky-api.onrender.com` dá 404 servido por outra conta.
- Com o responsável: mesclar o #30; Blueprint no Render com nome novo para a API e `VITE_API_URL` (#21); e2e no ruleset (#34); Dependabot (#33); Lambda (#23).
- O que travou: nada.
- Lição: um `*.onrender.com` com 404 pode ser de outra conta; ler o cabeçalho `x-render-origin-server` antes de escolher o nome do serviço.

### biblioteca · 16/11/2026 · DG github (lote 1)
- Tipo: ciclo de MVP; N1, Python + Streamlit.
- Antes: 9/10; #15 esperando o responsável; app no ar, mas privado (303 para o login).
- Feito: #17 na sprint (run 43797965182; jobs `app` com 24 testes e pip-audit, e `tela` com 13). Entraram: Streamlit 1.67 e Pillow 13 (a 12.3 tinha CVEs); pip-audit no CI; página de detalhe (#7); `region` do axe resolvida pelo `<main>` do Streamlit 1.67 (#11); teste de Esc; testes de banco ausente, busca vazia e espera, que o MVP citava sem existirem; docs com fontes.
- Revisão independente: antes do merge, primeira do lote na ordem certa. 6 erros: critério 6 sem teste de espera; "22 testes" no lugar de 24; `C:\v` corrompido no README; "claro e escuro" num app de tema único; plano dizendo que o código marcava o `main`; marcador de revisão pendente no PR. Todos corrigidos.
- Depois: 10/10 · o app continua privado.
- Com o responsável: mesclar o #15; Streamlit Cloud → Settings → Sharing → public (#4); caminhos longos no Windows (#12).
- O que travou: nada.
- Lição: conferir se cada teste citado no MVP existe; em Python, `\v` numa string vira tabulação vertical (usar string raw).

### huntweb-swapi · 16/11/2026 · DG github (lote 2)
- Tipo: ciclo de MVP; N1, React 18 + Vite 8.
- Antes: declarava 10/10, mas pela régua era 8/10.
- Feito: #37 na sprint (run 43799358100): e2e com axe só pelo teclado; WCAG 2.5.3 no link "Acessar"; título da aba por página; busca acompanha a URL; atualização do vite resolve 9 alertas; README reescrito.
- Revisão independente: antes do merge. 2 erros ("só teclado" com `fill()` e `focus()`; checagem de foco fraca), corrigidos, mais 5 sugestões aplicadas.
- Depois: 10/10 · fora do ar (404, Pages desligado).
- Com o responsável: ligar o Pages, mesclar o #36, pôr o e2e no ruleset (#38).
- Lição: `outlineStyle` diferente de `none` passa com o contorno padrão do Chromium; conferir o valor que o app define.

### sushibar · 16/11/2026 · DG github (lote 2)
- Tipo: ciclo de MVP; N1, Next.js 16 estático, React 19, Tailwind 3, Vitest e Playwright.
- Antes: declarava 10/10, mas só 6/10 tinham evidência (critérios 2, 3, 8 e 9); #21 esperando; fora do ar (Pages desligado).
- Feito: #23 na sprint (42583df, run 43800589625: raiz 15 e e2e 9): axe nas 5 páginas; abas por seta e End; link de pular e foco de 3 px; 3 testes de falha do Supabase; deps de produção com audit 0; deploy condicionado a `PAGES_VIA_ACTIONS`; 12 arquivos sem uso removidos. Depois, dentro da fila aprovada pelo responsável, #21 na main (aeef304), com o deploy pulado de propósito.
- Revisão independente: antes do merge. 5 erros (contagem de arquivos, plano sem o critério 9, data inventada no DEPLOY, 403 do Dependabot ausente, comentário prometendo axe no tema escuro), corrigidos; 9 de 11 sugestões aplicadas (inclusive `retries: 0` e `timeout-minutes`).
- Depois: 10/10 · fora do ar até ligar o Pages.
- Com o responsável: Settings → Pages → GitHub Actions; Variable `PAGES_VIA_ACTIONS=true` e rodar o workflow na main; e2e no ruleset (#24); Dependabot (#25); cardápio ilustrativo (#15).
- O que travou: um push não gerou run do CI.
- Lição: antes do merge, conferir no `gh run list` que existe run para o último commit do PR. Deploy condicionado a uma Variable deixa mesclar com o Pages desligado.

### doe-sangue-salve-vidas · 16/11/2026 · DG github (lote 2)
- Tipo: ciclo de MVP; N1, Express 4, Nunjucks, PostgreSQL, node:test e Playwright.
- Antes: declarava 10/10, mas pela régua era 7/10 (critérios 3 e 8 sem Playwright e axe; 9 com evidência velha); #20 esperando; fora do ar.
- Feito: #21 na sprint (586f5f5, run 43800806434): e2e com axe e teclado, com PostgreSQL 16 no CI; página 429 em português; "Quem pode doar" com fonte do Ministério da Saúde; código antigo removido; `npm audit` no CI e patch do `pg`. Dado pessoal: a captura do README mostrava nomes completos com tipo sanguíneo (dado de saúde, sensível pela LGPD) e foi trocada por dados fictícios. Depois, dentro da fila aprovada, #20 na master (6f33391).
- Revisão independente: antes do merge. 3 erros (senha local citada no `ANALISE.md`, teste de duplicidade sem valor, run de um commit anterior), corrigidos; 6 de 7 sugestões aplicadas, a outra virou a #27.
- Depois: 9/10; critério 9 Parcial, porque o histórico público ainda tem a imagem antiga, um INSERT com nome e e-mail de terceiro e a senha local antiga · fora do ar.
- Com o responsável: histórico (#22); e2e no ruleset (#23); Dependabot (#24); publicação no Render (#16).
- O que travou: nada.
- Lição: ao procurar dado pessoal, abrir as imagens do repositório; capturas de tela guardam dados de saúde.

### casa-criativa · 16/11/2026 · DG github (lote 2)
- Tipo: ciclo de MVP; N1, Node, Express 4, Nunjucks, SQLite, Playwright e axe.
- Antes: 10/10, mas afirmava testar o tema escuro sem `prefers-color-scheme` no CSS; nenhum PR esperando (o #57 entrou pela fila aprovada); fora do ar.
- Feito: `developer/sprint-2026-11-19` criada a partir da master; #59 na sprint (run 43802260791): busca `/ideias?q=` sem diferença de maiúsculas e acentos, com `%` e `_` como texto (#50); better-sqlite3 12 e job `raiz-node-24` (#51); o projeto Playwright "escuro" virou "celular" (375 px), com teste de rolagem horizontal (#55); `.netlify/state.json` fora do repositório. 17 testes de unidade e 36 no navegador. #65 (sprint → master) aberto com `revisao-responsavel`, não mesclado por ter surgido depois da aprovação.
- Revisão independente: antes do merge. 5 erros (axe dependente da ordem dos testes; critério 8 afirmando mais que o teste; faltava o id do ruleset; plano com "matriz" e "12 testes"; descrição do PR vencida), corrigidos em 3a3eea9.
- Depois: 10/10 com evidência · fora do ar.
- Com o responsável: mesclar o #65 (#64); publicar no Render (#47); opcional: apagar 4 branches `dependabot/*` obsoletas.
- Lição: com o ruleset exigindo o check `raiz`, uma matriz de versões de Node renomeia o job e trava o merge; usar um job à parte.

### calculadora · 16/11/2026 · DG github (lote 2)
- Tipo: ciclo de MVP; N1, React 18 com CRA 5, Jest, Playwright 1.65 e axe 4.14, Netlify.
- Antes: declarava 9/10, mas pela régua era 6/10 (2, 3, 8 e 9 sem evidência); #29 esperando; a main no ar na Netlify.
- Feito: #35 na sprint (4000fde, run 43802887296): `react-scripts` em devDependencies (audit de produção de 43 alertas para 0, agora no CI); e2e com 5 testes (axe nos temas Vivo e Dark, que existem, e no erro; Tab com foco medido; Ctrl+C; Esc); WCAG 2.5.3 na tecla AC; copiar o resultado (#20); `netlify.toml` e job `publicar` com build hook opcional. Depois, pela fila aprovada, #29 na main (2c166e8).
- Revisão independente: antes do merge. 4 erros; 3 corrigidos (corrida na mensagem de cópia; conferência no DEPLOY que não provava nada; foco medido num alvo só). O quarto (critério 9 como Parcial) foi mantido como Atende pela sessão; regra ambígua, levada à engenharia#33, e a leitura segura (Parcial) vale até a decisão. 7 sugestões aplicadas.
- Depois: 10/10 pela sessão, 9/10 pela leitura segura · a produção atualiza pela Netlify com o merge.
- Com o responsável: build hook, segredo e "Ignore builds" na Netlify (#18); e2e no ruleset (#30); Dependabot (#31); "O que aprendi" (#23); critério 9 (engenharia#33).
- O que travou: um push não gerou run; resolvido com commit vazio (melhor: o mesmo commit numa branch nova).
- Lição: na Netlify, "Stopped builds" também bloqueia o build hook; para publicar só pelo CI, usar "Ignore builds" com `[ -z "$INCOMING_HOOK_URL" ]`.

### be-the-hero · 16/11/2026 · DG github (lote 3)
- Tipo: ciclo de MVP; N1, API Express + Knex, web Vite + React 18, app Expo 57 (já migrado, não congelado).
- Antes: declarava 9/10, mas pela régua era 8/10 (critério 8 sem axe no Playwright); nenhum PR esperando (o #26 entrou pela fila); fora do ar.
- Feito: #30 na `developer/sprint-2026-11-19` (2fb73fe, run 43803813013; backend, frontend, mobile e e2e verdes): axe nas 4 telas e teclado (o teste falha sem `alt`); seed e dados fictícios nos testes e no README (#29); better-sqlite3 13.2 com `ignore-scripts=true` no `.npmrc` (#22); API testada também no PostgreSQL; testes de rede e espera no web; workflow duplicado removido. #37 (sprint → master) aberto, não mesclado por ter surgido depois da aprovação.
- Revisão independente: antes do merge. 2 erros (contagem de testes no PostgreSQL e "web 5" no plano), corrigidos em 4bc4709; o resto das sugestões virou a #36.
- Depois: 9/10 (critério 9 Parcial, pela engenharia#33) · fora do ar.
- Com o responsável: mesclar o #37 (#31); Neon e Render (#15); histórico dos bancos e Dependabot (#17).
- Lição: conferir se cada mensagem de erro citada no MVP tem teste; com dependência nativa que traz binários prontos, `ignore-scripts` no `.npmrc` evita o node-gyp no Windows.

### jobs-calc · 16/11/2026 · DG github (lote 3)
- Tipo: ciclo de MVP; N1, Node 22/24, Express 4, EJS, SQLite, Playwright e axe.
- Antes: 9/10, mas os critérios 3, 8 e 11 citavam um tema escuro que não existe; nenhum PR esperando (o #22 entrou pela fila); fora do ar (404, no-server).
- Feito: #24 na `developer/sprint-2026-11-19` (run 43805299460: raiz, node24 e interface): POST sem `Origin` e sem `Referer` recebe 403 (#21); fundo `inert` com o diálogo aberto e axe com o diálogo aberto (#19); better-sqlite3 12 e job `node24` à parte (#15); fim do projeto "escuro" no Playwright (16 → 8 testes de interface); teste do painel vazio; DEPLOY sem push direto na master. #31 (sprint → master) aberto.
- Revisão independente: antes do merge. 2 erros, corrigidos: o teste de Referer passava por cair no `catch` com URL inválida; o MVP citava um run anterior ao head.
- Depois: 9/10; critério 9 Parcial (Dependabot 403 e banco com a renda mensal no histórico, #11) · fora do ar.
- Com o responsável: mesclar o #31 (#25); fechar #10 e #20, já cumpridas; Dependabot (#26); histórico (#11); publicação (#12).
- O que travou: nada.
- Lição: conferir se o teste de segurança falha pelo motivo certo, com uma mutação, e não por cair num `catch`.

### cm-quiz-app · 16/11/2026 · DG github (lote 3)
- Tipo: ciclo de MVP; N1, Vue 3 + Vite 7, Node + Express, Ably.
- Antes: declarava 9/10, mas pela régua era 8/10 (critério 8 sem Playwright e axe no CI); nenhum PR esperando (o #28 entrou pela fila); fora do ar (404).
- Feito: #30 na `developer/sprint-2026-11-19` (7e45a85, run 43805433975: raiz, realtime-quiz e e2e com 10 testes): axe e teclado no e2e; telas em português, com `lang` e um `h1` por tela; botão "Criar" desligado sem tempo real, com aviso em 20 s; falha de rede tratada; Vite 7 e audit 0; Font Awesome Free no lugar do Pro; lint da raiz corrigido e o CI confere o `dist` versionado; README reescrito, sem os contatos do autor original. #37 (sprint → main) aberto.
- Revisão independente: antes do merge, sem erros; 7 de 8 sugestões aplicadas em 3f07456; a da sala sem host virou a #36.
- Depois: 8/10, Finalizado sim (o 3 depende da chave do Ably, #14; o 9 voltou para Parcial no #39, porque os alertas estão desligados, conferido às 01h43) · fora do ar.
- Com o responsável: mesclar o #37 (#38); chave do Ably (#14); Blueprint no Render (#16); Dependabot e e2e no ruleset (#32).
- O que travou: a checagem do `dist` falhou por CRLF; resolvido com `.gitattributes` `eol=lf`.
- Lição: no Playwright, `page.route('**/auth')` não pega `/auth?rnd=`; usar `**/auth*`.

### letmeask · 16/11/2026 · DG github (lote 3)
- Tipo: ciclo de MVP; N1, React 18, Vite 8 e Firebase 11 (compat).
- Antes: declarava 9/10, mas pela régua era 7/10 (2 sem meta; 8 sem axe no navegador; 3 Parcial); nenhum PR esperando (o #20 entrou pela fila); a build no ar (letmeask-aulas.web.app) é antiga.
- Feito: #21 na `developer/sprint-2026-11-19` (run 43807579877: raiz, regras e e2e): e2e com duas contas nos emuladores de Auth e RTDB (projeto demo-letmeask), em desktop e a 375 px, só pelo teclado; o axe achou 3 defeitos reais, corrigidos (contraste do contador de 2,9 para 5,0; WCAG 2.5.3 no botão de curtir; código da sala sobre o "Encerrar" no celular); Tab preso no diálogo; firebase-tools fixado; Pages condicionado a `PAGES_VIA_ACTIONS`. #27 (sprint → main) aberto.
- Revisão independente: antes do merge. 3 erros: critério 9 como Atende, firebase-tools sem versão, título da #17. O agente corrigiu os 2 últimos e manteve o 9; a DG github corrigiu para Parcial no #28 (d5d8612).
- Depois: 9/10 · fora do ar com a build nova.
- Com o responsável: mesclar o #27; domínios e deploy no Firebase (#12); Variables e Pages (#17); fluxo no Firebase real (#14); e2e no ruleset (#22); restringir a chave da API (#23); Dependabot (#24).
- O que travou: sem Java local, o e2e e as regras só rodaram no CI.
- Lição: o emulador de Auth põe uma faixa fora dos landmarks, e o axe acusa `region`; usar `useEmulator(url, { disableWarnings: true })`.

### petshop · 16/11/2026 · DG github (lote 3)
- Tipo: ciclo de MVP; N1, Next.js 16 estático, React 19, Tailwind 3, Vitest, Playwright e axe.
- Antes: declarava 10/10, mas 3, 6 e 9 sem evidência; #19 retido porque o deploy não tinha condição e o Pages está desligado.
- Feito: #20 na `developer/sprint-2026-11-12` (run 43807684595): deploy condicionado a `PAGES_VIA_ACTIONS`; patches e audit 0; e2e com 13 testes (WhatsApp por clique e teclado, mensagem com o nome do serviço, navegação, 404 com axe, AOS sem JS, 375 px com axe, WCAG 2.5.3); 404 em português; AOS visível sem JS; 459 px de rolagem horizontal no celular, corrigidos; nome acessível do "Entrar em contato". Depois, com o deploy condicionado e dentro da fila aprovada, #19 na main (deploy pulado).
- Revisão independente: antes do merge. 3 erros, corrigidos: o AOS piscava; o teste de 375 px mascarava a rolagem horizontal; o run citado era de um commit antigo.
- Depois: 9/10, critério 9 Parcial (Dependabot 403, #21, engenharia#33) · fora do ar até ligar o Pages.
- Com o responsável: Pages → GitHub Actions; Variable `PAGES_VIA_ACTIONS=true` e rodar o workflow; Dependabot (#21).
- Lição: um teste que neutraliza a animação antes de medir o layout esconde o defeito que deveria pegar.

### rocket-q · 16/11/2026 · DG github (lote 4)
- Tipo: ciclo de MVP; N1, Node 22, Express 4, EJS, SQLite e Playwright.
- Antes: declarava 10/10, mas pela evidência eram 6/10; nenhum PR esperando (o #15 entrou pela fila). `rocket-q.onrender.com` dá 200, mas serve outro código (outro `title`, `x-powered-by: Express`, sem os cabeçalhos do helmet).
- Feito: `developer/sprint-2026-11-19` criada; #16 na sprint (195652b, run 43808289685: raiz com 18 testes e 0 pulados, e2e com 5): axe e teclado a 1280 e 375 px; lista de perguntas atualizada a cada 15 s (#10), com teste que falha sem a mudança; view morta removida; link que não é deste código retirado. #21 (sprint → main) aberto.
- Revisão independente: antes do merge. 4 erros, corrigidos (dois testes sem esperar a consulta; aviso repetido que o leitor de tela não anunciava; Node 22.12+ exigido pelo e2e), mais 5 sugestões.
- Depois: 9/10, critério 9 Parcial (403, engenharia#33, #18) · fora do ar com este código.
- Com o responsável: mesclar o #21; Blueprint no Render (#17); Dependabot (#18); e2e no ruleset (#20).
- Lição: um 200 com outro `title` e sem os cabeçalhos do helmet mostra que o link publicado não roda este código; conferir os cabeçalhos, não só o status.

### my-money-app · 16/11/2026 · DG github (lote 4)
- Tipo: ciclo de MVP; N1, React 18 + Redux com Vite; API Express 5 + Mongoose.
- Antes: declarava 10/10, mas pela régua era 7/10 (3 e 8 sem Playwright e axe no CI; 9 só com o audit); nenhum PR esperando (o #27 entrou pela fila); fora do ar (404).
- Feito: `developer/sprint-2026-11-19` criada; #34 na sprint (run 43809661371: backend, frontend, e2e e auditoria): Mongoose 8.24.9 (a 8.24.4 tinha 4 alertas altos); e2e com axe (fluxo, cadastro só com teclado, erro de validação); o axe achou 3 problemas, corrigidos (`heading-order`, #24; abas sem `tablist`; contraste do aviso durante a animação); validação da API em português (#23); código morto e CI duplicado removidos; DEPLOY novo. #36 (sprint → main) aberto.
- Revisão independente: antes do merge. 2 erros de documentação, corrigidos; 7 de 9 sugestões aplicadas; a do `retries` virou a #35.
- Depois: 9/10, critério 9 Parcial (403, engenharia#33, #29) · fora do ar; o nome `my-money-api` pode estar ocupado no Render.
- Com o responsável: mesclar o #36; Dependabot (#29); e2e no ruleset (#30); publicação (#18); fechar #17 e #26, já cumpridas.
- Lição: com `reducedMotion: 'reduce'` no Playwright, o axe não vê a animação normal; correção feita só sob `prefers-reduced-motion` não vale para todos.

### dashboards · 16/11/2026 · DG github (lote 4)
- Tipo: ciclo de MVP; N1, portal estático (HTML, Tailwind, Playwright e axe) e versão Java (Spring Boot e JSF).
- Antes: declarava 10/10, mas os critérios 8 ("claro e escuro" sem `prefers-color-scheme`) e 9 estavam inflados; nenhum PR esperando (o #20 entrou pela fila); no ar (Pages legado, 200).
- Feito: #27 na `developer/sprint-2026-11-19` (run 43810387913: build e portal): `<main>` no Analytics v1; títulos em ordem nos 3 dashboards; o axe barra também as violações moderadas (#16), com teste que falha sem a correção; 13 testes Playwright; axe a 1280 e 375 px. #28 (sprint → main) aberto.
- Revisão independente: antes do merge, sem erros; 7 de 9 sugestões aplicadas em 3285c1a.
- Depois: 9/10, critério 9 Parcial (403, engenharia#33, #23) · o portal publicado é idêntico à main (md5); o ciclo entra no ar com o #28.
- Com o responsável: mesclar o #28 (#29); Dependabot (#23); publicar a versão Java (#10); fechar a #19, já cumprida.
- Lição: o @axe-core/playwright 4.14 exige Node >=22.12; dizer isso no README.

### aula-de-programacao · 16/11/2026 · DG github (lote 4)
- Tipo: ciclo de MVP; N1, site estático em HTML e JS, Playwright e axe, Pages legado.
- Antes: declarava 9/10, mas pela régua era 8/10 (critério 8 sem axe no navegador); nenhum PR esperando (o #30 entrou pela fila); no ar (200).
- Feito: `developer/sprint-2026-11-19` criada; #35 na sprint (runs 43810626944 e 43810770903: 18 testes Playwright, nenhum pulado): axe em 4 testes (painel, busca, aula real e erro); WCAG 2.5.3 nos botões de módulo; link direto `#aula-N` com `popstate` (#22); apagar a busca volta os módulos ao estado anterior (#27); DEPLOY novo. #36 (sprint → main) aberto.
- Revisão independente: antes do merge. 2 achados: o `#aula-N` colado com o site aberto voltava ao painel (corrigido com teste); o outro dizia que o axe não acharia o problema dos botões, e o agente contestou com a execução local do axe; a DG github aceitou, porque a correção tem teste que falha sem ela. Primeiro achado contestado pela regra nova. 6 sugestões aplicadas.
- Depois: 9/10, critério 9 Parcial (403, engenharia#33, #33) e vídeos pendentes (#21) · produção igual à main (md5) até o #36.
- Com o responsável: mesclar o #36; Dependabot (#33); vídeos (#21); fechar a #29; decidir #25 e #26.
- Lição: link por hash numa página única precisa tratar o `popstate`.

### douglasabnovato (perfil) · 16/11/2026 · DG github (lote 4)
- Tipo: ciclo de MVP; N1, README de perfil com Node, `node --test`, Playwright e axe.
- Antes: 9/10, com o 8 e o 9 sem a evidência da régua; nenhum PR esperando; perfil no ar.
- Feito: #61 na `developer/sprint-2026-11-19` (0e6bfa2; runs 43811017927 e 43811158637, verificar): axe e teclado; teste com as imagens fora do ar; animação clara e escura com `<picture>`; verificador de títulos (#48); Actions fixadas por SHA e `dependabot.yml` (#49); DEPLOY novo. #62 (sprint → master) aberto.
- Revisão independente: 5 achados; 4 corrigidos. O quinto (axe no tema escuro) o agente recusou pela regra 3 do brief, explicou no PR e não mesclou; a DG github decidiu (o perfil não tem CSS escuro, só a imagem troca, com teste), registrou no PR e mesclou.
- Depois: 8/10; 9 Parcial (403, #57, engenharia#33) e 12 Parcial (#46).
- Com o responsável: mesclar o #62; Dependabot (#57); animação 403 (#56); cargo e marcos (#46); link do Discord (#47); validação (#44).
- Lição: `String.replace` com um texto que contém `` $` `` duplica o arquivo; usar `replace(a, () => b)`.

### ux-design · 16/11/2026 · DG github (lote 4)
- Tipo: ciclo de MVP; N1, site estático em HTML, CSS e JS, Playwright e axe, Pages legado.
- Antes: 9/10, com o critério 8 só com Lighthouse e teclado; nenhum PR esperando (o #42 entrou pela fila); no ar.
- Feito: `developer/sprint-2026-11-19` criada; #49 na sprint (run 43814144584, 20 testes): axe no catálogo, no filtro, no case e no carrossel; Pausar e Retomar no carrossel (WCAG 2.2.2); o link `wa.me/55SEUNUMERO` some enquanto não há número; README e meta com 61 projetos; DEPLOY novo. Clone com `--filter=blob:none`, sem commit no clone local. #50 (sprint → main) aberto.
- Revisão independente: antes do merge. 3 erros, corrigidos (marcadores de rascunho `CI_RUN` e `PR_*` esquecidos; frase falsa sobre o clone); 4 sugestões aplicadas.
- Depois: 9/10, critério 9 Parcial (403, #45, engenharia#33; #31; #46) · no ar (Pages legado, igual à main por md5); o site soma cerca de 830 MB, perto do limite de 1 GB do Pages (#33, #34).
- Com o responsável: imagens com dados de terceiros no site público (#46, citadas só pelo nome do arquivo); clientes (#31); mesclar o #50; Dependabot (#45); número de WhatsApp (#47); fechar a #41.
- Lição: procurar marcadores de rascunho com `grep` antes de abrir o PR; em repositório grande, clonar com `--filter=blob:none` ou sparse-checkout.
