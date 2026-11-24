# Checklist de autorrevisão de scripts e workflows [A CONFIRMAR com o responsável]

**Situação:** é proposta de processo, de 24/11/2026. Vale como guia da dona. Só vira regra com o ok do responsável.

**Para que serve:** a sessão dona confere a lista **antes** de pedir a revisão R19 ao Esp. A lista não substitui a revisão (decisão 144). Ela tira da revisão os achados que já se repetiram.

**De onde veio:** dos achados das revisões R19 de 23 e 24/11/2026:
- itens 5 a 18: sessão arquitetura de IA, a partir do `engenharia` e do formacao-dev#339;
- itens 1 a 4 e 19 a 24: sessão comunidade LearnTech, a partir das revisões da formacao-dev.

Na medida da Esp Dados de 24/11, 76% dos achados viraram mudança, com 10 retrabalhos e 2 defeitos que escaparam, nos 4 projetos.

**Como usar no PR:** o corpo diz "Autorrevisão: itens 1 a 24 conferidos" e lista os que não se aplicam. Se o Esp achar algo que a lista já cobria, isso conta como retrabalho.

## Os que mais economizam rodada

Cada um apareceu em 3 ou mais PRs seguidos.

| # | Pergunta | Achado que a originou |
|---|---|---|
| 1 | Toda **borda** de limite usa o mesmo operador em todo lugar (por exemplo, `>=` no alerta e no resumo), e tem teste **no valor exato** e um abaixo (47/48 h, 9/10)? | formacao-dev#358, item 1; #338, item 6 |
| 2 | Toda **janela de tempo** é um timestamp completo com fuso, e não uma data sem hora (que vira 00:00 UTC e alarga a janela)? Tem teste da borda e de 2 fusos (`-03:00` e `Z`)? | formacao-dev#359, item 1 (os 7 dias viravam 8); #360, item 5 |
| 3 | Todo **`--limit`** de leitura tem constante com nome e **aviso no relatório** quando bate no limite, em vez de cortar calado? | formacao-dev#338, item 5; #359, item 2; #360, item 2 |
| 4 | Se a **lista de referência** (por exemplo, os "de dentro") vier **vazia**, o script avisa no topo e não calcula o que depende dela (falha fechado)? | formacao-dev#358, item 5; #360, item 1 |

## Entrada, caminho e saída

| # | Pergunta | Achado que a originou |
|---|---|---|
| 5 | Roda com caminho **relativo** e **absoluto**, no Windows e no Linux? Maiúsculas, minúsculas e a barra `\` foram conferidas? | engenharia#66, ressalva 3 (raiz `.`) |
| 6 | O **código de saída** é testado na linha de comando, e não só a função? E com pasta ou entrada que não existe? | engenharia#66, ressalvas 2 e 4 |
| 7 | Toda **contagem** tem um teste negativo, com um texto que **não** deve contar? | engenharia#73, ressalva 1; o escape #73 → #79 |
| 8 | Um comando "só de leitura" **não grava** nada? `npm run build`, `npm test` e `npm install` gravam, e os coletores do painel também. | engenharia#72, pedido 2; #73, ressalva 4 |
| 9 | A **data** sai no fuso de Brasília (`date`), e não em UTC? | onda 1 da Esp Dados (A2); engenharia#69, achado 4 |
| 10 | Os comandos citados no README existem e rodam? | engenharia#72, ressalva 4; critério 12 |

## Segurança e falha

| # | Pergunta | Achado que a originou |
|---|---|---|
| 11 | O script **falha fechado**? Sem a ferramenta (Python, `gh`, rede), ele bloqueia com motivo claro, e não deixa passar? | engenharia#67, achados 8 e 9 |
| 12 | A checagem vale **na hora da ação**? Ou dá para mudar o estado entre a checagem e a ação (corrida)? | engenharia#67, achado 1 |
| 13 | O alvo é **explícito**? Repositório, branch e PR vêm da linha, e não do diretório ou do ambiente (`cd`, `GH_REPO`)? | engenharia#67, achado 2 |
| 14 | É uma **lista do que é permitido**, e não do que é proibido? | engenharia#67, achados 4 e 6 |
| 15 | Um **segredo** achado é citado só pelo lugar, nunca pelo valor? | engenharia#72, pedido 3 |

## Workflows do GitHub Actions

| # | Pergunta | Achado que a originou |
|---|---|---|
| 16 | As **entradas obrigatórias** da action estão em todo job que a usa, e as **permissões** são as mínimas que ela lê? | formacao-dev#339, B2 e B3 |
| 17 | As actions estão **fixadas por SHA**, com a versão em comentário? | engenharia#71 (R-c) e #76 |
| 18 | O gatilho não roda **2 vezes** o mesmo commit (push e PR)? Há `concurrency`? | engenharia#71 (R-a e R-b) e #75 |

## Dados da API e texto livre

| # | Pergunta | Achado que a originou |
|---|---|---|
| 19 | O vínculo entre PR e issue usa o que o **GitHub de fato liga** (`closingIssuesReferences`), com a regex do corpo só de reserva, aceitando `Closes: #n`? | formacao-dev#360, item 3 |
| 20 | Um **veto** (negação, pergunta) vale **por ocorrência**, e não para o texto inteiro? Tem teste com o pedido e o veto na mesma frase? | formacao-dev#340, item 1 |
| 21 | O que **conta como resposta** foi listado por inteiro (comentário, review, merge de quem é de dentro), e **bot e autor** ficam fora, com um teste para cada? | formacao-dev#358, itens 2 e 6; #359, item 3 |
| 22 | Ao **reconhecer texto livre**, há testes para variações (espaços, quebra de linha, sinônimos, acento) **e** para falsos positivos (citação `> `, "eu faço parte")? | formacao-dev#338, itens 1 e 2; #340, itens 2 a 4 |
| 23 | **Campos nulos** da API (`assignees: null`, `comments: null`, `reviews` ausente) passam por `?? []` em toda função pública, com teste? | formacao-dev#358, item 4; #338 |
| 24 | Ao escrever o script pelo terminal (heredoc ou `node -e`), as **barras invertidas** das regex sobreviveram? Confira o arquivo gravado, e não só o que foi digitado. | formacao-dev#359. A arquitetura de IA teve o mesmo deslize ao escrever o `verificar_links.mjs` (#66) e o `grep` do `docs/MVP.md` (#73), e pegou os 2 antes do commit |
