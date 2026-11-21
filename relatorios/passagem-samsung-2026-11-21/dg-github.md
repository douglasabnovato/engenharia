# Passagem Samsung → Acer · DG github · 21/11/2026

Fontes: transcrição da DG github (15/11 a 17/11; ela termina em 17/11 por volta das 12h) e o GitHub lido em 21/11/2026 pelo `gh`. O ciclo de 18/11 e os merges sprint → principal de 19/11 aparecem no GitHub, mas não na transcrição.

## 1. Papel

1. Abria em `C:\douglasabnovato-github` (raiz), com o título "DG github". Sessão de apoio do DG líder.
2. Dona de 40 repositórios: aircnc, instagram-feed, dev-radar, valoriza, proffy, niky, oxe-online, biblioteca, sushibar, huntweb-swapi, calculadora, doe-sangue-salve-vidas, casa-criativa, be-the-hero, cm-quiz-app, jobs-calc, letmeask, petshop, rocket-q, my-money-app, dashboards, feedback-widget, aula-de-programacao, components, learning-portal-fiori-sap, headset, controle-financas, movies, restaurante-churrascaria, signature-generator, e-commerce-t-shirt, coin-wallet, catalogo-acai, studio-d, douglasabnovato, facil-admin-para-voce, facil-admin-plataforma, facil-admin-gestao, douglasabnovato.dev, ux-design.
3. Fazia: ciclo por repositório (MVP, docs, issues, CI, alertas, LCP), por agentes em paralelo, cada um num clone temporário. Merge feature → sprint com CI verde.
4. Não fazia: escrever no `engenharia` (só propunha), learnTECH, formacao-dev, VEB, figma-design. Merge na principal só com ordem explícita do responsável.
5. Desde 20/11 o papel é da sessão "repositórios GitHub" no Acer.

## 2. Estado por repositório (principal, 21/11/2026)

CI = último run na principal. "No ar" = `curl` no link do repositório hoje.

| repo | MVP | Finalizado | No ar |
|---|---|---|---|
| aircnc | 10 de 10 | sim | 200 |
| instagram-feed | 10 de 10 | sim | 200 |
| dev-radar | 10 de 10 | sim | sem link |
| valoriza | 8 de 10 | sim | sem link |
| proffy | 9 de 10 | sim | sem link |
| niky | 10 de 10 | sim | sem link |
| oxe-online | 10 de 10 | sim | 200 |
| biblioteca | 10 de 10 | sim | 303 (Streamlit) |
| sushibar | 10 de 10 | sim | 200 |
| huntweb-swapi | 10 de 10 | sim | 200 |
| calculadora | 10 de 10 | sim | 200 |
| doe-sangue-salve-vidas | 9 de 10 | sim | sem link |
| casa-criativa | 10 de 10 | sim | sem link |
| be-the-hero | 9 de 10 | sim | sem link |
| cm-quiz-app | 10 de 10 | sim | sem link |
| jobs-calc | 9 de 10 | sim | sem link |
| letmeask | 10 de 10 | sim | sem link (CI skipped) |
| petshop | 10 de 10 | sim | 200 |
| rocket-q | 10 de 10 | sim | 200 (Render) |
| my-money-app | 10 de 10 | sim | sem link |
| dashboards | 10 de 10 | sim | 200 |
| feedback-widget | 9 de 12 | sim | 200 |
| aula-de-programacao | 9 de 10 | sim | 200 |
| components | 10 de 12 | sim | 200 |
| learning-portal-fiori-sap | 10 de 12 | **não** | 200 |
| headset | 9 de 12 | sim | sem link (#4) |
| controle-financas | 8 de 12 | sim | 200 |
| movies | 11 de 12 | sim | 200 |
| restaurante-churrascaria | 7 de 12 | sim | 200 |
| signature-generator | 11 de 12 | sim | 200 |
| e-commerce-t-shirt | 9 de 12 | sim | 200 (CI skipped) |
| coin-wallet | 11 de 12 | sim | 200 |
| catalogo-acai | 11 de 12 | sim | 200 |
| studio-d | 10 de 12 | sim | 200 |
| douglasabnovato | 9 de 10 | sim | perfil |
| facil-admin-para-voce | 10 de 12 | sim | 200 |
| facil-admin-plataforma | 8 de 12 | **não** | 200 |
| facil-admin-gestao | 10 de 12 | sim | 200 |
| douglasabnovato.dev | 10 de 12 | sim | 200 |
| ux-design | 9 de 10 | sim | 200 |

CI da principal verde em todos, exceto os dois "skipped" (só deploy condicional). feedback-widget e rocket-q têm o último run em 16/11.

## 3. Em andamento

6. **feedback-widget#31** (sprint → main, 23 commits, `revisao-responsavel`): Actions verde; o status da Vercel falha por painel (feedback-widget#11). Único PR da sprint-19 que não entrou na principal.
7. **Não commitado, em clones de 17/11** (`...\072ea2e1-567a-4c2e-869d-2662b928da44\scratchpad\agentes\d17\`). Nenhuma branch foi enviada. Provavelmente superados pelo ciclo de 18/11; conferir antes de descartar:
   - aircnc e dev-radar (`feature/2026-11-17-minimatch`): `mobile/package.json` e lockfile.
   - douglasabnovato.dev (`feature/2026-11-17-minimatch`): `package-lock.json`.
   - facil-admin-plataforma (`feature/2026-11-17-criterio`): `index.html`, `e2e/primeira-carga.spec.ts` e o novo `src/test/casca.test.tsx`.
8. **Tarefas de 17/11 sem relatório final na transcrição:** minimatch (aircnc, dev-radar, douglasabnovato.dev), fechar issues de alertas com evidência, próximo critério em facil-admin-plataforma, cm-quiz-app e movies. As issues de triagem saíram: catalogo-acai#50, facil-admin-plataforma#57, oxe-online#37.
9. **PRs abertos de 20/11 ("bloco Produto no MVP.md")**, já da sessão nova: catalogo-acai#55, components#62, controle-financas#56, e-commerce-t-shirt#54, facil-admin-plataforma#62, headset#48, learning-portal-fiori-sap#43, movies#115, restaurante-churrascaria#44, studio-d#73.
10. **Dependabot abertos no escopo:** catalogo-acai#38, #39, #41 a #43; dashboards#34 a #36; dev-radar#32 e #33 (de 28/09); douglasabnovato#63 a #65; facil-admin-plataforma#44 a #46, #48 a #51; oxe-online#26 a #29, #31, #33, #34; petshop#27 a #32; studio-d#52, #65, #66; instagram-feed#111 (app `instarocket/` congelado).

## 4. Decisões do responsável (fora do engenharia)

11. "chegamos aonde eu gostaria" (15/11, aircnc e instagram-feed): esses dois são o padrão de "pronto" para os demais.
12. App móvel antigo: "vamos deixar congelado para evoluirmos depois, ou seja, será um item registrado em nova issue. O que vale para outros repositórios." (15/11, todos). aircnc, dev-radar e be-the-hero estão no Expo 57 e não são congelados.
13. figma-design: "Quero que você fique de fora dele." (16/11).
14. "da proxima vez, faca" (16/11): comandos `gh` de um plano aprovado (merge, ruleset, Pages, Dependabot) são rodados pelo agente. Segredos, contas e painéis seguem com ele.
15. "os demais, mergear" (16/11): autorizou os 37 merges sprint → principal daquele dia. Vale só para aqueles PRs.
16. "quero o nome do repositório, quero os itens enumerados continuamente" (16/11, todas as respostas).
17. "ative nosso workflow" (17/11): aprovou o plano do dia; mostra que o fluxo R7 está valendo.

## 5. Com o responsável

18. Mesclar feedback-widget#31 e ajustar o painel da Vercel (feedback-widget#11: Root Directory `web`, Node 22, Redeploy). Ou decidir pelo Render (feedback-widget#3).
19. facil-admin-plataforma: backend publicado (#2, critérios 3 e 9), GoatCounter (#17), telas logadas no LCP (#5), triagem dos majors (#57). O `/entrar` precisa ser medido de novo no ar.
20. headset#4: criar o serviço no Render. Destrava o critério 7.
21. facil-admin-gestao#26 e facil-admin-para-voce#33: prazo de guarda e contato de privacidade.
22. restaurante-churrascaria#40 (alerta do secret scanning, adiado por ele em 19/11), #2 (publicar pelo Actions) e #12 (GoatCounter).
23. Dados no histórico do Git: proffy#28, doe-sangue-salve-vidas#22, controle-financas#43, valoriza (critério 9), aula-de-programacao#26, ux-design#39.
24. controle-financas#47 (rotas sem autenticação na API antiga); ux-design#46 e #47; letmeask#12, #14, #17, #23.
25. douglasabnovato.dev#251 e #253; be-the-hero#17; aula-de-programacao#21 (vídeos); learning-portal-fiori-sap#16.
26. Rulesets que exigem o job e2e: calculadora#30, cm-quiz-app#32, controle-financas#39, doe-sangue-salve-vidas#23, feedback-widget#27, huntweb-swapi#38, letmeask#22, my-money-app#30, niky#34, rocket-q#20, sushibar#24.
27. Limpeza: cerca de 30 issues `depende-do-responsavel` parecem já resolvidas ("Mesclar o ciclo de 07/11", "Ligar os alertas do Dependabot", ex.: movies#90, movies#99, headset#28, headset#35). Conferir e fechar com evidência.

## 6. Aprendizados novos

28. `gh pr merge` com 502 Bad Gateway não é negação de permissão: tentar de novo mais tarde funcionou (coin-wallet#44, my-money-app#37, 16/11/2026).
29. CI que não dispara na abertura do PR volta com fechar e reabrir o PR uma vez, com comentário (niky#40, 16/11/2026).
30. Brief de agente deve proibir fechar issue antes do merge na principal. A regra existe, mas o brief que a contrariou fez 6 issues serem reabertas (portfólio, 16/11/2026).
31. Comandos de clonagem e `npm ci` com 6 agentes em paralelo derrubam a medição de LCP e dão timeout no e2e local. Medir só com no máximo 1 agente rodando (portfólio, 16/11/2026).

## 7. Só no Samsung

32. Scratchpad da DG github, com clones e rascunhos: `C:\Users\User\AppData\Local\Temp\claude\11434daef2994b40\072ea2e1-567a-4c2e-869d-2662b928da44\scratchpad\`. Inclui `agentes\adr\`, `agentes\crit9\` (e `crit9\textos`), `agentes\d17\`, `agentes\lcp\medir.sh` (medição de LCP) e dezenas de scripts `edit*.py`. Só o `medir.sh` merece ir para o Acer (ou para `engenharia/scripts`, por PR). O resto se refaz por clone novo.
33. Trabalho não commitado do item 7. Se ainda valer, refazer no Acer a partir da sprint; não copiar a pasta.
34. Memórias criadas pela DG github em `C:\Users\User\.claude\projects\C--douglasabnovato-github\memory\`: `mandato-autonomo-1511.md`, `escopo-41-repositorios.md`, `mobile-congelado.md`. Ligadas: `politica-alertas-dependabot.md`, `executar-comandos-do-responsavel.md`, `formato-itens-com-repositorio.md`. Levar o conteúdo para o `engenharia` (itens 11 a 16), não os arquivos.
35. Tarefa agendada `revisao-d1-github` (6h40, `C:\Users\User\.claude\scheduled-tasks\revisao-d1-github\SKILL.md`) segue ligada no Samsung. Desligar lá quando o Acer tiver a sua, para não haver duas revisões D-1.
36. Sessão filha "Roteiro 13 e roteiros dos vídeos 6 a 9 no Studio D" (concluída). Nada pendente nela.

## 8. Próximos passos recomendados

37. Conferir os 4 clones do item 7 contra o ciclo de 18/11 e descartar ou refazer. Começar por facil-admin-plataforma (medir o `/entrar` no ar).
38. learning-portal-fiori-sap#39: LCP de 8,48 s no site é o único "Finalizado: não" que é trabalho de código.
39. Triar os Dependabot do item 10: fechar instagram-feed#111 pelo congelamento; mesclar menores com CI verde; majors pelas issues catalogo-acai#50, oxe-online#37, facil-admin-plataforma#57.
40. Fechar com evidência as issues de alertas e de "Mesclar o ciclo" já resolvidas na principal (item 27).
41. Desligar `revisao-d1-github` no Samsung e registrar no `engenharia` as decisões 11 a 16.
