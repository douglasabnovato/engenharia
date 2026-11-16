# Passo a passo do responsável · 16/11/2026

Levantado às 09h08 de 16/11 pelo DG líder, com `gh`. Esta lista cobre 36 PRs sprint → principal e 194 issues com `depende-do-responsavel`. Ela vale para o portfólio no GitHub. O learnTECH e a VEB ficam nas sessões donas.

Tudo aqui é seu: merge na principal, configuração, contas e decisões. As sessões não fazem nenhum destes passos.

## Parte 1 · Uma vez, para todos (cerca de 1 h)

Faça nesta ordem. Os comandos rodam no Git Bash, dentro de um clone do `engenharia`.

### 1.1 Riscos de dados pessoais (cerca de 20 min)

| Ordem | Issue | O que fazer |
|---|---|---|
| 1 | controle-financas#47 | Tirar do ar a API antiga (suspender o serviço no Render) ou mandar a sessão pôr token nas rotas. Hoje não vaza porque o banco está fora. |
| 2 | doe-sangue-salve-vidas#22 | Decidir: aceitar o histórico como dado de teste, ou reescrever o histórico (ação sua, com `git filter-repo`). |
| 3 | controle-financas#43 | A mesma decisão para as fotos com dados pessoais. |
| 4 | ux-design#46 | Decidir: manter as imagens do catálogo, borrar ou remover. |
| 5 | douglasabnovato.dev#253 | Editar ou apagar os trechos de terceiros nas issues antigas. |

### 1.2 Mesclar os PRs sprint → principal (cerca de 1 h)

O CI de todos foi conferido às 09h08 e não há conflito. Para cada um, abra o PR, olhe o resumo e clique em **Merge pull request** (merge commit, não squash). Os 33 PRs liberados:

aula-de-programacao#36, be-the-hero#37, biblioteca#26, calculadora#37, casa-criativa#65, catalogo-acai#35, cm-quiz-app#37, coin-wallet#43, components#53, controle-financas#46, dashboards#28, dev-radar#80, douglasabnovato#62, douglasabnovato.dev#276, e-commerce-t-shirt#41, engenharia#2, facil-admin-gestao#42, facil-admin-para-voce#37, facil-admin-plataforma#40, headset#38, instagram-feed#108, jobs-calc#31, learning-portal-fiori-sap#34, letmeask#27, movies#104, my-money-app#36, niky#39, restaurante-churrascaria#34, rocket-q#21, signature-generator#118, studio-d#61, sushibar#30, ux-design#50.

Atalho por linha de comando, um por vez:

```bash
gh pr merge 36 --repo douglasabnovato/aula-de-programacao --merge
```

Retidos hoje:
- **feedback-widget#31**: CI com falha na Vercel. Espere o diagnóstico (tarefa B).
- **huntweb-swapi#36 e oxe-online#18**: o deploy roda sem a condição do Pages. Espere a tarefa C, ou ligue o Pages antes (1.4).

Antes de mesclar:
- **facil-admin-gestao#42**: troca os degradês por cores sólidas. Confira a página.
- **engenharia#2**: entra primeiro. Depois dele, atualize o clone local (`git pull` em `C:\douglasabnovato-github\engenharia`), que está parado em 09/11.

Quando um PR é mesclado, as issues "Mesclar o ciclo de 07/11" e "Mesclar o ciclo de 16/11" desse repositório fecham sozinhas ou ficam sem objeto. Feche as que sobrarem.

### 1.3 Ligar os alertas do Dependabot (cerca de 5 min)

São 33 issues "Ligar os alertas do Dependabot". Um laço liga em todos:

```bash
for r in aula-de-programacao be-the-hero biblioteca calculadora catalogo-acai cm-quiz-app coin-wallet components controle-financas dashboards doe-sangue-salve-vidas douglasabnovato e-commerce-t-shirt facil-admin-gestao facil-admin-para-voce facil-admin-plataforma feedback-widget headset jobs-calc learning-portal-fiori-sap letmeask movies my-money-app niky oxe-online petshop restaurante-churrascaria rocket-q studio-d sushibar ux-design valoriza; do gh api -X PUT repos/douglasabnovato/$r/vulnerability-alerts && echo "$r ok"; done
```

Depois disso, a sessão relê os alertas abertos, e o critério 9 pode ir para "Atende". Decida também a engenharia#33.

### 1.4 Proteger a principal (cerca de 10 min)

São 15 repositórios sem ruleset:

```bash
DONO=douglasabnovato bash scripts/configurar-responsavel.sh proteger calculadora catalogo-acai coin-wallet dev-radar feedback-widget headset huntweb-swapi jobs-calc movies my-money-app niky oxe-online proffy restaurante-churrascaria studio-d
```

Depois, no painel de cada um (Settings → Rules → Rulesets → principal-protegida), acrescente **Require status checks** com os jobs do CI. Inclua o `e2e` onde há issue pedindo isso: calculadora#30, cm-quiz-app#32, controle-financas#39, doe-sangue-salve-vidas#23, feedback-widget#27, huntweb-swapi#38, letmeask#22, my-money-app#30, niky#34, rocket-q#20, sushibar#24.

### 1.5 Ligar o Pages (cerca de 5 min)

Faça depois do merge dos PRs, porque o workflow do Pages chega com eles:

```bash
DONO=douglasabnovato bash scripts/configurar-responsavel.sh pages huntweb-swapi oxe-online petshop sushibar learning-portal-fiori-sap facil-admin-gestao
```

E desligue o Pages antigo do douglasabnovato.dev (#270), que publica o código-fonte. O caminho é Settings → Pages → Unpublish.

### 1.6 Medição de uso (cerca de 15 min, uma conta só)

Crie uma conta gratuita no GoatCounter. Um código serve para todos os sites. Mande o nome do código à DG github. A sessão põe o script nos sites, com o aviso de coleta e sem dado pessoal.

Isso resolve 16 issues de medição: catalogo-acai#7, coin-wallet#24, components#27, controle-financas#35, douglasabnovato.dev#251, e-commerce-t-shirt#18, facil-admin-gestao#21, facil-admin-para-voce#19, facil-admin-plataforma#17, feedback-widget#15, headset#20, learning-portal-fiori-sap#16, movies#58, restaurante-churrascaria#12, signature-generator#87, studio-d#4.

## Parte 2 · Por repositório

Esta parte traz o que sobra depois da Parte 1. **Render** quer dizer criar o serviço gratuito pelo Blueprint e com um nome próprio; o passo a passo está na issue. **Validar** quer dizer pedir a uma pessoa de fora que use o site e anotar o resultado na issue.

| Repositório | Passos que sobram | Pode ficar "Finalizado" depois? |
|---|---|---|
| aula-de-programacao | #17 validar; #21 validar os vídeos; #25 decidir os banners; #26 decidir se enxuga o histórico (330 MB) | sim, com a validação |
| be-the-hero | #15 Render; #17 decidir o histórico com os bancos | sim, depois do Render |
| biblioteca | #4 tornar público o app no Streamlit Cloud; #12 ligar caminhos longos no Windows (só para uso local) | sim, com o #4 |
| calculadora | #18 publicar na Netlify só depois do CI; #23 decidir o futuro do projeto | sim |
| casa-criativa | #47 Render | sim, depois do Render |
| catalogo-acai | #3 confirmar as decisões da loja; #16 validar | sim, com o #3 |
| cm-quiz-app | #14 criar a chave gratuita do Ably e pô-la como segredo; #16 Render | sim, depois dos dois |
| coin-wallet | #23 confirmar a meta; #25 validar; #26 confirmar a Netlify como endereço oficial | sim |
| components | #28 Render pelo Blueprint; #41 ligar a varredura de segredos; #23 fica com a sessão | sim, depois do Render |
| controle-financas | #47 e #43 (Parte 1); #7 publicar a API atual; #19 publicar o front pelo Actions; #22 confirmar a meta | não hoje: depende da API |
| dashboards | #10 decidir se publica a versão Java no Render | sim |
| dev-radar | #61 Render | sim, depois do Render |
| doe-sangue-salve-vidas | #22 (Parte 1); #16 Render; #10 fica com a sessão, depois do Render | não hoje |
| douglasabnovato | #56 o 403 (espere a tarefa A); #46 confirmar cargo, marcos e selos; #47 mandar um convite válido do Discord; #44 validar | sim, depois do 403 |
| douglasabnovato.dev | #253 e #270 (Parte 1); #252 validar; #265 e #267 decisões de produto | sim |
| e-commerce-t-shirt | #16 e #28 publicar no alwaysdata pelo CI (segredos seus); #17 validar | sim, depois da publicação |
| engenharia | #2 merge; #16 ativar as skills em todas as sessões; #17 ligar o hook que bloqueia force push; #33 decidir o critério 9 | — |
| facil-admin-gestao | #19 confirmar depoimentos e o "98%"; #23 informar LinkedIn, Instagram e WhatsApp reais; #25 dizer quais imagens apagar; #37 Pages (1.5); #22 validar | sim |
| facil-admin-para-voce | #17 confirmar preços, selos e depoimentos; #33 dizer o prazo de guarda e o contato de privacidade; #21 e #24 dizer o que apagar; #20 validar | sim |
| facil-admin-plataforma | #2 restaurar o Supabase (o projeto gratuito pausa sem uso; o DNS não resolve); #16 e #5 ficam com a sessão (tarefa F) | não hoje: depende do Supabase |
| feedback-widget | #11 Vercel (espere a tarefa B); #3 Render da API; #31 merge depois da B | não hoje |
| headset | #4 Render; #19 confirmar a meta; #15 fica com a sessão, depois da publicação | sim, depois do Render |
| huntweb-swapi | #25 Pages (1.5); merge do #36 depois da tarefa C | sim |
| instagram-feed | só o merge do #108 | sim |
| jobs-calc | #11 decidir o histórico com o banco; #12 Render | sim, depois do Render |
| learning-portal-fiori-sap | #3 Pages (1.5); #17 confirmar a meta; #15 fica com a sessão, depois do Pages | sim |
| letmeask | #12, #14 e #17 confirmar o Firebase e escolher a hospedagem (Pages ou Firebase Hosting); #23 restringir a chave do Firebase aos endereços do app, no console do Google Cloud | não hoje: depende do Firebase |
| movies | #98 o 403 (espere a tarefa A); #59 validar; #57 e #83 ficam com a sessão | sim, depois do 403 |
| my-money-app | #18 Render | sim, depois do Render |
| niky | #21 republicar no Render; #23 rodar a Lambda e guardar os prints | não hoje |
| oxe-online | #11 Pages (1.5); #19 fica com a sessão; merge do #18 depois da tarefa C | sim |
| petshop | #11 Pages (1.5) | sim |
| proffy | #26 Render com nome próprio; #28 decidir o histórico com os telefones; #36 merge do ciclo antigo | sim, depois do Render |
| restaurante-churrascaria | #30 dizer se o cliente é real; #2 publicar as regras do Firestore; #16 confirmar a meta | sim, depois do #30 e do #2 |
| rocket-q | #17 Render pelo Blueprint | sim, depois do Render |
| signature-generator | #112 o 403 (espere a tarefa A); #100 confirmar a meta; #96 validar; #68 e #72 confirmar o fechamento ou reabrir | sim, depois do 403 |
| studio-d | #52 e #53 decidir o Dependabot; #10 e #54 revisar os roteiros antes de gravar | sim |
| sushibar | #10 Pages (1.5); #15 decidir se o cardápio e o WhatsApp seguem ilustrativos | sim |
| ux-design | #46 (Parte 1); #31 confirmar os clientes citados; #47 número do WhatsApp; #39 decidir se enxuga o histórico (680 MB); #32 validar | sim, depois do #46 |
| valoriza | #11 decidir o banco com 9 usuários no histórico; #16 Render da API | sim, depois do Render |

## Como avisar o que fez

Basta uma linha no chat do DG líder, por exemplo "mesclei os 33" ou "Dependabot ligado". O DG líder confere pelo `gh`, distribui o que destravou e registra no relatório do dia.

<sub>por douglas ciborgue</sub>
