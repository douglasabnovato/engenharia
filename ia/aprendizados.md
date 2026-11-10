# Aprendizados

Tudo o que os ciclos de outubro e novembro de 2026 ensinaram, organizado por tema. Cada item: a regra e, entre parênteses, onde e quando apareceu. Leia o tema da pilha do repositório antes de começar.

Para acrescentar: escrever a regra em 1 a 2 linhas, no tema certo, sem repetir um item que já existe (se for variação, melhorar o item existente).

## Sumário

- [Análise e honestidade dos documentos](#análise-e-honestidade-dos-documentos)
- [Segurança e segredos](#segurança-e-segredos)
- [Windows e Git Bash](#windows-e-git-bash)
- [Git e locks](#git-e-locks)
- [Node, npm, pnpm e outras dependências](#node-npm-pnpm-e-outras-dependências)
- [Testes em geral](#testes-em-geral)
- [Playwright e axe](#playwright-e-axe)
- [Lighthouse e LCP](#lighthouse-e-lcp)
- [CI e GitHub Actions](#ci-e-github-actions)
- [Render](#render)
- [MongoDB Atlas](#mongodb-atlas)
- [Vercel, Netlify e Pages](#vercel-netlify-e-pages)
- [Streamlit](#streamlit)
- [Expo](#expo)
- [React, Vue e Vite](#react-vue-e-vite)
- [Permissões do agente](#permissões-do-agente)
- [Issues e Projects](#issues-e-projects)

## Análise e honestidade dos documentos

- Ler os comentários das issues abertas, não só o corpo: um comentário mandava mesclar um PR que já estava mesclado. (learning-portal-fiori-sap, 03/11/2026)
- Conferir se as ADRs foram cumpridas no código: uma mandava remover 547 KB de dados raspados, e o arquivo seguia lá. (calculadora e sushibar, 03/11/2026)
- Uma resposta HTTP 200 não prova nada sozinha. Abrir o link com `curl` antes de confiar no README (dois davam 404) e comparar o HTML com o repositório: pode ser build antigo ou site de outra pessoa (`title`, `theme-color`, caminhos, autor). (huntweb-swapi e instagram-feed, 03/11; niky, be-the-hero e proffy, 06/11/2026)
- Procurar no README frases que digam que o CI publica o site e conferir no workflow; era falso. (petshop, 06/11/2026)
- Issue de "próximo passo" pode já estar cumprida por teste existente; ler os testes e o log do CI antes de planejar e fechar com o run como evidência. (components, facil-admin-plataforma e feedback-widget, 09/11/2026)
- PR antigo de outra rodada pode ter trabalho válido; conferir `git log <principal>..<branch>` antes de chamá-lo de redundante. (dashboards e vizinhos, 06/11/2026)
- Montar a cadeia de `require` ou `import` a partir do ponto de entrada para achar código legado: pastas inteiras podem não ser carregadas por nada. (casa-criativa e vizinhos, 06/11/2026)
- Os critérios de MVP escritos depois do código deixaram 272 de 468 critérios para trás; escrever o `MVP.md` no primeiro dia. (portfólio, 02/11/2026)
- Num projeto N2, o código pode deixar o projeto "Finalizado" sem mudar a contagem de critérios, porque o que falta depende do responsável; o avanço aparece nas outras componentes do índice. (learning-portal-fiori-sap, 03/11/2026)
- Um índice que media atividade (issues, campos) marcou 90 e caiu para 74 com os critérios de MVP; medir resultado, não volume. (portfólio, 02/11/2026)

## Segurança e segredos

- Apagar o arquivo com a credencial não revoga a senha, que segue no histórico; revogar é do responsável. (instagram-feed, 03/11/2026)
- Ao tratar um vazamento, procurar também o nome do usuário da credencial e frases como "senha removida" nos docs, que podem afirmar algo falso. (instagram-feed e huntweb-swapi, 03/11/2026)
- Antes de apagar um arquivo vazado, seguir a cadeia de `require` ou `import` para levar junto o que só ele usava. (instagram-feed e huntweb-swapi, 03/11/2026)
- Sem a chave de um serviço externo, subir só com as telas e avisar pela interface e por `/health`, em vez de derrubar o processo. (casa-criativa e vizinhos, 06/11/2026)
- Com `helmet` (`Referrer-Policy: no-referrer`), o Chrome manda `Origin: null` e uma checagem de mesma origem recusa todo POST real; rodar ao menos um POST pelo navegador antes de marcar o critério 3. (proffy, casa-criativa e jobs-calc, 09/11/2026)
- Dados pessoais em bancos versionados e em issues públicas apareceram em 4 repositórios e 12 issues; revisar privacidade (LGPD) antes do primeiro commit. (portfólio, 02/11/2026)
- Uma mudança removeu um acesso de demonstração intencional e foi revertida; registrar esse tipo de decisão em ADR. (portfólio, 02/11/2026)

## Windows e Git Bash

- Clonar com `git clone -c core.longpaths=true` e comparar `git ls-files | wc -l` com `git ls-tree -r HEAD | wc -l` antes do primeiro commit; um índice incompleto gerou ~1.968 exclusões. (ux-design, 06/11/2026)
- Repositório acima de 300 MB: o clone completo cai; usar `git clone --filter=blob:none --no-checkout` com sparse-checkout sem mídia e adicionar só as pastas mexidas. (aula-de-programacao e ux-design, 09/11/2026)
- Com `core.autocrlf=true`, o comando `file` mostra CRLF que não existe no repositório. (coin-wallet e vizinhos, 05/11/2026)
- Conferir `git ls-files --eol` antes de reescrever um arquivo: gravar LF sobre índice CRLF troca o arquivo inteiro; nesse caso usar `git -c core.autocrlf=false add`. (dashboards, 06/11; components, 09/11/2026)
- Variáveis com caminho (`PUBLIC_URL=/movies`) viram `C:/Program Files/Git/movies`; usar `MSYS_NO_PATHCONV=1`. (movies, 09/11/2026)
- `python - <<EOF` no Git Bash corrompe acentos; gravar o script em arquivo e rodar com `PYTHONUTF8=1`. (aircnc, 09/11/2026)
- Subir servidor com `&` no mesmo comando trava o Bash; usar comando em segundo plano separado ou o `webServer` do Playwright. (proffy e vizinhos, 09/11/2026)
- Teste que estoura o tempo só no computador local (carga alta) não é bug; rodar só o arquivo afetado e decidir pelo CI. (signature-generator e vizinhos, 06/11/2026)
- Não rodar testes pesados (MUI + jsdom) junto com `npm install`; o Vitest estourou o tempo por disputa de CPU. (oxe-online e petshop, 06/11/2026)
- Com vários agentes na mesma máquina, as portas padrão (5173, 4173) colidem: portas próprias por repositório pelo `env` do `webServer`, ou config temporária sem commit. (aircnc e biblioteca, 09/11/2026)
- Porta livre em IPv4 pode estar ocupada em `[::1]` por outro agente; conferir as duas pilhas e o `title` com `curl -6`. Parar o próprio servidor pelo PID (`Get-NetTCPConnection`). (e-commerce-t-shirt e components, 09/11/2026)
- Padrão de `sparse-checkout` que começa com `/` vira caminho do Windows; usar `MSYS_NO_PATHCONV=1`. (ux-design, 10/11/2026)
- `sed -i` com acento ou `·` não casa em arquivo CRLF; usar o Edit e conferir o `diff --stat`. (huntweb-swapi, 10/11/2026)
- `python -I` ignora `PYTHONIOENCODING` e `PYTHONUTF8`; usar `python -I -X utf8` para imprimir acentos e setas no console do Windows. (coordenador, 10/11/2026)
- Agentes em paralelo sobrescrevem arquivos de mesmo nome no scratchpad; uma subpasta por agente. (lote A, 10/11/2026)

## Git e locks

- Fazer push da `feature` a cada commit: uma queda de sessão deixou 5 agentes com trabalho só no clone. (coin-wallet, facil-admin-*, oxe-online e petshop, 05/11/2026)
- Antes de levar um commit "não enviado", conferir `git branch -r --contains <sha>`; ele já estava na principal. (catalogo-acai, 06/11/2026)
- Antes do merge, conferir o número de arquivos do PR; um número inesperado denuncia índice quebrado. (ux-design, 06/11/2026)
- Nunca usar opção de force, nem `--force-with-lease`; um uso por engano foi registrado como desvio (foi avanço simples, sem perda). (components, 09/11/2026)
- O npm 11 no Windows tira `@esbuild/*` do lock até com `--package-lock-only`; quando só entra um pacote, montar o lock a partir do da principal e conferir as remoções antes do commit. (controle-financas e vizinhos, 09/11/2026)
- `pnpm update -r <pacote> --depth Infinity` com vários pacotes reescreveu o `pnpm-workspace.yaml` inteiro; editar o catálogo à mão e conferir `git diff --stat`. (components, 09/11/2026)
- Scripts de dados (ex.: `popular_banco.py`) podem regerar arquivos versionados; restaurar com `git checkout` antes do commit. (biblioteca e vizinhos, 06/11/2026)
- Comprimir imagens não reduz o clone quando o peso está no histórico; isso é decisão do responsável. (aula-de-programacao e ux-design, 09/11/2026)
- Troca de texto num `MVP.md` com a mesma linha repetida nas tabelas do Histórico acerta várias ou falha: limitar a troca à tabela do topo e conferir o `git diff --stat`. (e-commerce-t-shirt, 10/11/2026)

## Node, npm, pnpm e outras dependências

- `better-sqlite3` 11 não compila no Windows com Node 24; para testar sem mexer no lock: `npm ci --ignore-scripts && npm i --no-save better-sqlite3@12`. Senão, testar só no CI. (aircnc e vizinhos, 06/11/2026)
- Contar alertas pela API do Dependabot (todos os pacotes), não pelo `npm audit` de um pacote. Com o Dependabot desligado (API 403/404), `npm audit --omit=dev` ou `pnpm audit --prod` é a única fonte: rodar sempre no critério 9. (aircnc, 06/11; components, 09/11/2026)
- `composer audit` pode passar a falhar sem mudança no código; atualizar com `composer update pacote --with pacote:~X.Y.Z` para não trocar de versão maior. (e-commerce-t-shirt, 06/11/2026)
- No Windows, `pip` falha por caminho longo com Streamlit em venv no scratchpad; rodar localmente só o backend e deixar o teste da interface para o CI, registrando no PR. (biblioteca, 06/11/2026)
- Dependências envelheceram até exigir migração (13 PRs do Dependabot parados); atualizar toda semana, em passos pequenos. (portfólio, 02/11/2026)

## Testes em geral

- Rodar os testes de interface uma vez com outra ordem dos dados: um seletor `first()` passava por acaso. (learning-portal-fiori-sap, 03/11/2026)
- Todo script `test:*` novo precisa de um passo no workflow; script fora do CI não é testado. (e-commerce-t-shirt e movies, 06/11/2026)
- Testes com `skip` sem variável de ambiente ficam "verdes" sem rodar; conferir `# skipped` no log do CI. (feedback-widget e vizinhos, 06/11/2026)
- Percorrer a tela com valores no formato brasileiro ("1500,50"); a API recusava a vírgula e os testes só usavam ponto. (my-money-app, 09/11/2026)
- Provar que o teste falha sem a correção (`git show <sprint>:arquivo > arquivo`) e congelar o relógio (`page.clock.setFixedTime`) quando a tela depende de horário; o CI roda em UTC. (e-commerce-t-shirt e restaurante-churrascaria, 09/11/2026)
- No UI5, `sort([])` não devolve a ordem original da lista. (learning-portal-fiori-sap e vizinhos, 05/11/2026)
- `react-hooks/rules-of-hooks` acusa função `use*` importada dentro de função comum no teste; usar alias na importação, sem desligar a regra. (signature-generator e vizinhos, 06/11/2026)
- No jsdom, em página grande, preferir `waitFor` com `getElementById` a `findByRole`. (components, 09/11/2026)

## Playwright e axe

- Conferir a tela também com o sistema em modo escuro: um `prefers-color-scheme: dark` herdado do template deixava o texto ilegível, e o axe só no claro não pegou. (sushibar, 03/11/2026)
- Projetos claro e escuro no mesmo servidor dividem o banco: usar o nome do projeto nos dados, `reducedMotion: "reduce"` e `context.route` para cortar rede externa; com diálogo aberto, escopar o axe no `.modal`. (proffy e vizinhos, 09/11/2026)
- Rodar o axe com dados reais e em largura de desktop; tabela larga gerou `scrollable-region-focusable` que o teste com dois itens não mostrava. Desligar `transition` antes de medir foco por `getComputedStyle`. (cm-quiz-app e my-money-app, 09/11/2026)
- O axe não mede contraste no jsdom; testar os pares de tokens do CSS à parte. (facil-admin-plataforma, 09/11/2026)
- `Dialog` do Radix sem `DialogTrigger` não devolve o foco; só teste de teclado com Esc mostra. (facil-admin-plataforma, 09/11/2026)
- Armadilha de foco em widget não modal só age com o foco dentro dele; testar partindo de um link da página. (feedback-widget, 09/11/2026)
- Em dev, o Vite recarrega na primeira visita de app SSR e desfaz o percurso por Tab; envolver em `expect().toPass()`. (components, 09/11/2026)
- No `webServer` do Playwright, passar `PORT`, CORS e `VITE_API_URL` pelo `env`. (aircnc, be-the-hero e dev-radar, 09/11/2026)

## Lighthouse e LCP

**Como medir**
- Registrar as 3 execuções, não só a mediana; a primeira, com cache frio, pode ficar bem acima. Se a mediana passar de 2,5 s, repetir a série antes de registrar (a mesma página deu 2,67 s e 1,70 s). (biblioteca e vizinhos, 06/11; catalogo-acai e vizinhos, 06/11/2026)
- Lighthouse no Windows: `--headless=new` devolve NO_FCP; usar `--chrome-flags="--headless --no-sandbox"`, conferir `runtimeError` e repetir até ter 3 execuções válidas. (facil-admin-gestao, 06/11/2026)
- Com agentes em paralelo, CPU em 100% distorce a série sem erro (FCP de 6 a 22 s): usar `timeout 150` por execução, registrar o TBT, aceitar só execuções com `observedFirstContentfulPaint` abaixo de ~2 s e TBT abaixo de ~5 s, alternando antes e depois na mesma série. (movies, headset e e-commerce-t-shirt, 09/11/2026)
- Servir o build com compressão, como o Pages: `http-server` sem `-g` inflou o JS de 61 para 181 KB e o LCP de ~2,3 para ~3,0 s. Antes de comparar com série antiga, conferir `transferSize` para ver se ela teve compressão. (movies, 09/11/2026; e-commerce-t-shirt, 09/11/2026)
- Conferir que a porta serve o nosso build (title ou md5 contra o `dist`); o Lighthouse mediu a página de outro agente sem erro. (components e feedback-widget, 09/11/2026)
- Medir de novo todo LCP "Atende" antigo antes de mantê-lo: um foi de 2,19 s para 14,8 s. (e-commerce-t-shirt, 06/11/2026)
- O LCP "depois" só existe com o site publicado; prever um segundo par de PRs ou aceitar a medição local como "Parcial". (facil-admin-gestao e facil-admin-para-voce, 06/11/2026)

**Como ler**
- Ler as fases do LCP no JSON do Lighthouse antes de prometer ganho: com 80% de atraso de renderização, o gargalo é o JS, não o CSS. (headset e vizinhos, 09/11/2026)
- Conferir `largest-contentful-paint-element`: um aviso que surge depois de uma chamada pode virar o elemento do LCP. (feedback-widget e vizinhos, 06/11/2026)
- Se o framework troca o esqueleto antes de a imagem pintar, ela nunca vira LCP; um `PerformanceObserver` de `largest-contentful-paint` no Playwright mostra quem gera entrada. Dar ao contêiner do esqueleto um seletor diferente do React ajuda a ler o JSON. (movies e headset, 09/11/2026)
- Numa SPA com API e JS em paralelo, o LCP simulado fica preso ao FCP; medir o peso por pacote pelo sourcemap (`vite build --sourcemap`) antes de prometer ganho. (e-commerce-t-shirt, 09/11/2026)

**O que funcionou**
- Script inline que dispara um fetch cedo precisa vir antes de qualquer `<link rel="stylesheet">`; depois do CSS de fontes ele só roda quando o CSS termina. (restaurante-churrascaria, 09/11/2026)
- CSS do Google Fonts bloqueia: `media="print"` com `onload` e `noscript` tirou 0,5 s; carregar o CSS de fontes depois do `load` derrubou o FCP para ~1,2 s, porque fontes de outro domínio entram na conta antes da 1ª pintura. (facil-admin-plataforma e e-commerce-t-shirt, 09/11/2026)
- Pré-renderizar o HTML só baixa o LCP simulado se o `<script type="module">` sair do head: um carregador inline no fim do body, que pede o JS depois do `first-contentful-paint`, levou de 3,68 para 1,82 s. Com `requestAnimationFrame` o JS ainda saía antes da pintura. Comparar `observedLargestContentfulPaint` com o simulado antes de investir em SSG. (components, 09/11/2026)
- Reduzir JS sozinho pode não mover o LCP simulado se CSS e fontes ainda bloqueiam a 1ª pintura. (e-commerce-t-shirt, 09/11/2026)

## CI e GitHub Actions

- Abrir o workflow e conferir os gatilhos: ele só rodava em PR para a `main`. Incluir `developer/**` (ou `developer-**`) em `pull_request.branches`. (learning-portal-fiori-sap, 03/11/2026)
- Logo depois de criar o PR, `gh pr checks --watch` pode sair com "no checks reported"; esperar o run aparecer em `gh run list`. (calculadora e sushibar, 03/11/2026)
- O run de push na `developer` logo após o merge pode ficar mais de 10 minutos na fila; esperar antes do PR para a principal. (facil-admin-gestao e facil-admin-para-voce, 06/11/2026)
- Antes de apagar um `ci/*.yml` duplicado, ver se ele tem passos que o workflow ativo não tem (deploy, `npm audit`). (aircnc e vizinhos, 06/11/2026)
- Em 06/11/2026 o `ubuntu-latest` passou a ser o 26.04: Playwright 1.56 não instalou o Chromium (1.63 instalou). Se falhar em `playwright install`, subir o Playwright antes de olhar o código. (oxe-online e petshop, 06/11/2026)
- `playwright install --with-deps` no Ubuntu 26.04 pode levar 12 minutos; olhar os passos do job antes de supor travamento. (casa-criativa e vizinhos, 06/11/2026)
- `gh pr checks --watch` sai assim que aparecem só os checks da Vercel ou da Netlify; esperar o run do Actions em `gh run list` antes do merge. (catalogo-acai, 10/11/2026)
- O ruleset sem `required_status_checks` exige PR, mas deixa mesclar com o CI vermelho; conferir os critérios da issue de proteção antes de usar `Closes`. (lotes de 10/11/2026)

## Render

- Endereço do Render pode ser de outra pessoa: o nome `.onrender.com` pode pertencer a outra conta, e o Render acrescenta um sufixo (`aircnc-api-45yf`). Conferir o endereço real e corrigir `VITE_API_URL`, `PUBLIC_URL` e `CORS_ORIGINS` no `render.yaml`. (aircnc, 09/11/2026; be-the-hero e proffy, 06/11/2026)
- Testar o JS publicado para ver qual API ele chama, em vez de confiar na variável. (aircnc, 09/11/2026)
- O Blueprint cria a API e o site a partir de `rootDir` no mesmo repositório. (aircnc, 09/11/2026)
- `/health` que não toca o banco não prova a conexão. (aircnc, 09/11/2026)
- Serviço acima de 512 MB de memória derruba API e formulários no plano gratuito. (components, 27/10/2026)

## MongoDB Atlas

- Um projeto do Atlas aceita um só cluster M0; cluster pausado com versão antiga não volta: criar outro. (aircnc, 09/11/2026)
- Ao criar o cluster, desmarcar "Automate security setup" e "Preload sample dataset"; o Quickstart cria usuários Atlas Admin. (aircnc, 09/11/2026)
- Um usuário por app, com `readWrite` no banco: Database = nome do banco, Collection vazia (`readWrite@aircnc`, e não `readWrite@database.aircnc`). (aircnc, 09/11/2026)
- `0.0.0.0/0` só fica Active com o cluster ativo. (aircnc, 09/11/2026)
- `user is not allowed to do action [find]` é permissão; `bad auth` é senha. (aircnc, 09/11/2026)

## Vercel, Netlify e Pages

- Deploy para Pages por Actions fica travado por uma Variable até o responsável mudar a fonte do Pages; a principal fica verde sem mexer em configuração. (restaurante-churrascaria, 06/11/2026)
- Status da Netlify vêm com `conclusion` nulo no rollup; decidir pelo código de saída de `gh pr checks`. (restaurante-churrascaria e vizinhos, 06/11/2026)
- Status externo vermelho há meses por configuração (Vercel) não bloqueou o merge; valeu o CI do GitHub. A correção da configuração é do responsável. (feedback-widget, 06/11/2026)

## Streamlit

- `st_keyup` reage a keyup e o `fill()` do Playwright não o dispara; digitar com `press_sequentially` e conferir que a lista diminuiu. Esperar o menu e o iframe antes do teste de teclado. (biblioteca, 09/11/2026)

## Expo

- O `zod` vulnerável vinha do `@expo/cli` 57.0.27; `npm install expo@~57.0.32` resolve dentro do mesmo SDK, sem Expo 58. Conferir o lock dos outros apps Expo 57. (aircnc, 09/11/2026)

## React, Vue e Vite

- `React.lazy` só suspende na primeira vez por instância; não testar âncora e carregamento com o mesmo nome. (components, 09/11/2026)
- Vue 3: cliente de SDK externo guardado em `data` vira proxy reativo; usar `markRaw`. O Vue 3 monta dentro de `#app`: raiz com `id="app"` duplica o id. (cm-quiz-app, 09/11/2026)
- Vite: `manualChunks` em objeto leva dependências compartilhadas para chunks nomeados (o do Radix importava o do Supabase); usar `manualChunks` em função e conferir os `modulepreload` do `dist/index.html`. (facil-admin-plataforma, 09/11/2026)

## Permissões do agente

- O merge feature → sprint pode ser negado ("Merge Without Review") e a negativa não é uniforme entre repositórios: tentar uma vez; se negar, deixar o PR aberto com `revisao-responsavel` e abrir a issue `depende-do-responsavel` com o passo a passo. (proffy, casa-criativa, jobs-calc e feedback-widget, 09/11/2026)
- Abrir o PR feature → sprint já com `revisao-responsavel`, resumo completo e a issue "Mesclar o ciclo", sem esperar a tentativa de merge. (controle-financas, headset e dashboards, 09/11/2026)
- Apagar a `feature` remota (`git push --delete`) é bloqueado; fica com o responsável. Os limites do processo vencem guias que sugerem apagar branches. (oxe-online e petshop, 06/11; huntweb-swapi, 03/11/2026)
- Criar workflow agendado de publicação foi bloqueado; vira issue. (e-commerce-t-shirt e movies, 06/11/2026)
- O merge de PR do Dependabot foi negado; cita-se na issue de manutenção. (aircnc e vizinhos, 06/11/2026)
- `gh pr edit --body` foi negado a um agente, e `gh pr comment` não: para registrar algo num PR já aberto, comentar. (lote C, 10/11/2026)
- Ligar o Pages pela API (`POST repos/<dono>/<repo>/pages`) foi negado ao coordenador como "publicar site novo", mesmo com a autorização geral; criar o ruleset pela API passou. (coordenador, 10/11/2026)

## Issues e Projects

- Não preencher os campos do Project à mão (mais de 5 minutos por repositório): criar a issue com rótulos e milestone e rodar `gh project item-add`; quem coordena roda o preenchimento em lote. (learning-portal-fiori-sap, 03/11/2026)
- Os rótulos `mvp` e `depende-do-responsavel` podem não existir; criar antes de abrir as issues. (calculadora e sushibar, 03/11/2026)
- 117 de 179 issues iniciais, sem objetivo nem critério, acabaram fechadas como não planejadas; toda issue nasce com objetivo, motivo e 3 a 5 critérios. (portfólio, 02/11/2026)
