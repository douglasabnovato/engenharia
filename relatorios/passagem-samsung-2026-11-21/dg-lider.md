# Passagem Samsung → Acer · DG líder · 21/11/2026

## 1. Papel

1. Sessão "DG líder", aberta em `C:\douglasabnovato-github` no Samsung. Orquestrou de 13/11 a 17/11 a DG mundo, a DG veb e a DG github (regras R1 a R17).
2. Desde 20/11, o papel é do **Líder de TODOS**, no Acer ([`ia/orquestracao.md`](../../ia/orquestracao.md), engenharia#50). Esta sessão parou em 21/11 para não duplicar o plano do dia.
3. Escrevia só no `engenharia` (relatórios e decisões, por PR na sprint). Não escrevia código nos produtos.

## 2. Estado no fim (17/11, 11h)

4. 40 repositórios da DG github com ciclo feito e o critério 9 revisto pela regra de alertas.
5. 16/11: 37 PRs sprint → principal mesclados por ordem do responsável, todos com deploy verde. 17/11: engenharia#45 e 6 Dependabot de versão menor mesclados.
6. Relatório mais recente: [`relatorios/dia-2026-11-16.md`](../dia-2026-11-16.md). De 17 a 20/11 não há relatório: o Samsung ficou desligado.

## 3. Em andamento

7. Ficou sem resposta do responsável em 17/11: mesclar os Dependabot de versão maior das Actions (checkout e setup-node 7), com CI verde: douglasabnovato#63 a #65, studio-d#52, oxe-online#26 a #29, catalogo-acai#38 e #39, facil-admin-plataforma#44 a #46.
8. feedback-widget#31 (sprint → principal) segue aberto desde 16/11: o check da Vercel falha (Root Directory no painel).
9. O plano de 17/11 foi distribuído à DG github (MVP do headset, components e valoriza; minimatch no aircnc, dev-radar e douglasabnovato.dev; LCP do movies e do facil-admin-plataforma; fechar issues de alertas; triagem dos majors vermelhos). Não houve aviso de fim: conferir na sessão "repositórios GitHub".

## 4. Decisões do responsável (palavras dele)

10. 16/11: "aceito o risco." ADR-008 do movies (react-router 6).
11. 16/11: "voce poderia ter feito todos esses codigos que voce me pediu para fazer. da proxima vez, faca." Depois do plano aprovado, o orquestrador roda os comandos `gh` de configuração e merge. Segredos, contas e painéis fora do `gh` seguem com ele.
12. 16/11: "quero o nome do repositório, quero os itens enumerados continuamente para facilitar o meu entendimento". Toda resposta usa `repo#N` e numeração contínua.
13. 16/11: "Regra geral por ADR. alertas que nao atrapalham a producao, pode passar. os que atrapalham, entender, escolher a melhor estrategia para manter a funcionalidade". Está em `arquitetura/padroes.md`.
14. 16/11: "os de terceiros, pode ficar lá. os demais, mergear". Os 79 PRs abertos em repositórios de terceiros (76 de 10/11) ficam como estão.
15. 16/11: "Sim, desligue". O Pages antigo do douglasabnovato.dev foi desligado.
16. 17/11: "ative nosso workflow". Lido como aprovação do plano do dia, sem as versões maiores das Actions (item 7).

## 5. Com o responsável (abertos em 17/11)

17. Dados pessoais: controle-financas#47 (API antiga no Render) e #43, ux-design#46, doe-sangue-salve-vidas#22.
18. Vercel do feedback-widget (item 8).
19. formacao-dev: em que conta está; 11 Dependabot de versão maior, 6 `depende-do-responsavel`, Pages.
20. learnTECH: deploy (PRs de integração e `npm run deploy` do Worker), learntech-content#12, #23, #24, #29, #30, HD-0049 e HD-0054, links do YouTube das 2 compilações, D-12.
21. Render: controle-financas#47, headset#4, proffy#26, niky#21, doe-sangue-salve-vidas#16, casa-criativa#47, valoriza#16, dev-radar#61.
22. facil-admin-plataforma#2 (Supabase), conta do GoatCounter, studio-d#52 e #53, signature-generator#68 e #72, restaurante-churrascaria#30, facil-admin-para-voce#33, engenharia#33.

## 6. Aprendizados

23. Os do dia 16/11 já estão em `ia/aprendizados.md` (engenharia#44). Novo de hoje: tarefa agendada só roda com a máquina ligada; com dois computadores, as mesmas tarefas disparam em dobro (Samsung, 21/11/2026).

## 7. Só no Samsung

24. Tarefas agendadas no Samsung (ligadas em 21/11): `abertura-do-dia-lider`, `checkpoint-lider`, `fechamento-lider`, `semana-lider`, `revisao-d1-github`, `abertura-do-dia-learntech`, `abertura-do-dia-veb`, `convites-learntech`. Em 21/11 dispararam atrasadas e em dobro com o Acer. Desligar aqui é decisão do responsável.
25. Memórias da sessão (`.claude/projects/C--douglasabnovato-github/memory/`, 24 arquivos). Regras que ainda valem e talvez não estejam no Acer: apps móveis antigos congelados (15/11); escopo de 41 repositórios, figma-design fora (16/11); contas de demonstração e chave TMDB do movies aceitas; preencher todos os campos do Project; índice de progresso de 0 a 100; avisos de início e de fim com percentual; nunca commitar nos clones locais de aula-de-programacao e ux-design (índice quebrado).
26. Arquivos na raiz `C:\douglasabnovato-github`: `pendencias-responsavel.md` (11/11), `plano-github-2026-11-10.md`, `plano-favoritos-e-my-work-2026-11-10.md`, `abertura-formacao-dev-prompt.md`, `code-review/`, `convites/` (script dos convites do learnTECH), `historico/` (planos e decisões de 27/10 a 09/11), `videos-para-youtube/` (2 compilações de 2023 para subir), `mundo-learn-tech/` (clones da DG mundo).
27. Para o Acer: os vídeos e o script `convites/` não estão no GitHub. Os planos em `historico/` são antigos; o engenharia já tem o que vale.

## 8. Próximos passos recomendados

28. Responsável: decidir se desliga as tarefas agendadas do Samsung (item 24).
29. Líder de TODOS: ler esta pasta e conferir os itens 7 a 9 com a sessão "repositórios GitHub".
30. Líder de TODOS: juntar a lista do item 17 a 22 com a dele, sem repetir.
31. Responsável: subir os 2 vídeos de `videos-para-youtube/` ou copiá-los para o Acer.
