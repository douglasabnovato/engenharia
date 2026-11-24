# Checklist de autorrevisão de scripts e workflows [A CONFIRMAR com o responsável]

**Situação:** proposta de processo, de 24/11/2026. Vale como guia da dona e só vira regra com o ok do responsável.

**Para que serve:** a sessão dona confere a lista **antes** de pedir a revisão R19 ao Esp. A lista não substitui a revisão (decisão 144). Ela tira da revisão os achados que já se repetiram.

**Como usar:**
- **Quais itens:** os 4 primeiros sempre. Depois, só os grupos que o PR toca. Um PR só de workflow, por exemplo, confere os itens 1 a 4 e 16 a 18.
- **Perguntas com mais de uma parte:** o "sim" vale só se todas as partes forem sim.
- **Quando não souber responder:** diga no PR, e a pergunta vai para o Esp.
- **No PR:** o corpo diz "Autorrevisão: itens X a Y conferidos" e cita os que não se aplicam.
- **Retrabalho:** um achado do Esp que a lista já cobria pode contar como retrabalho na medida da Esp Dados. **[A CONFIRMAR com a Esp Dados]**, pelo Líder de TODOS.

## Os que mais economizam rodada (cada um apareceu em 2 ou mais PRs)

| # | Pergunta |
|---|---|
| 1 | Toda **borda** de limite usa o mesmo operador em todo lugar e tem teste **no valor exato** e num abaixo? |
| 2 | Toda **janela de tempo** é um timestamp completo com fuso, com teste da borda e de 2 fusos (`-03:00` e `Z`)? |
| 3 | Todo **`--limit`** de leitura tem constante com nome e **aviso no relatório** quando bate no limite? |
| 4 | Se a **lista de referência** vier **vazia**, o script avisa no topo e para (falha fechado)? |

## Entrada, caminho e saída (scripts)

| # | Pergunta |
|---|---|
| 5 | Roda com caminho **relativo** e **absoluto**, no Windows e no Linux, com a caixa das letras conferida? |
| 6 | O **código de saída** é testado na linha de comando, inclusive com entrada que não existe? |
| 7 | Toda **contagem** tem 2 testes: um texto que **não** deve contar e um que **deve**? |
| 8 | Um comando "só de leitura" **não grava** nada (`npm run build`, `npm test`, `npm install` e os coletores do painel gravam)? |
| 9 | A **data** sai no fuso de Brasília (`date`), e não em UTC? |
| 10 | Toda evidência citada (no README, no `MVP.md` ou no PR) tem o **comando exato**, que roda e dá o resultado escrito? |

## Segurança e falha

| # | Pergunta |
|---|---|
| 11 | Sem a ferramenta (Python, `gh`, rede), o script **bloqueia** com motivo claro, e não deixa passar? |
| 12 | A checagem vale **na hora da ação**, sem dar para mudar o estado entre a checagem e a ação? (Se não souber, diga no PR.) |
| 13 | O alvo (repositório, branch, PR) vem **explícito** da linha, e não do diretório ou do ambiente? (Confira lendo o código: nada de `cd` nem `GH_REPO`.) |
| 14 | É uma **lista do que é permitido**, e não do que é proibido? (Confira lendo o código.) |
| 15 | Um **segredo** achado é citado só pelo lugar, nunca pelo valor? (Confira com `git diff`: o valor não aparece.) |

## Workflows do GitHub Actions

| # | Pergunta |
|---|---|
| 16 | As **entradas obrigatórias** da action estão em todo job que a usa, e as **permissões** são as mínimas que ela lê? |
| 17 | As actions estão **fixadas por SHA**, com a versão em comentário? |
| 18 | O gatilho não roda **2 vezes** o mesmo commit (push e PR), e há `concurrency`? |

## Dados da API e texto livre

| # | Pergunta |
|---|---|
| 19 | O vínculo entre PR e issue usa o que o **GitHub de fato liga** (`closingIssuesReferences`), com a regex do corpo só de reserva? |
| 20 | Um **veto** (negação, pergunta) vale **por ocorrência**, com teste do pedido e do veto na mesma frase? |
| 21 | O que **conta como resposta** foi listado por inteiro (comentário, review, merge de quem é de dentro), com bot e autor fora? |
| 22 | O **texto livre** tem testes de variações (espaço, quebra de linha, sinônimo, acento) **e** de falsos positivos (citação `> `)? |
| 23 | **Campos nulos** da API passam por `?? []` em toda função pública, com teste? |
| 24 | Ao escrever o script pelo terminal (heredoc ou `node -e`), as **barras invertidas** sobreviveram? (Confira o arquivo gravado: `grep -cF '\' <arquivo>` dá o número de linhas com barra, que deve bater com o esperado.) |

## Origens

Itens 5 a 18 e o 10: sessão arquitetura de IA. Itens 1 a 4 e 19 a 24: sessão comunidade LearnTech. As 2 listas foram unidas em 24/11/2026 e revisadas pelo Esp ES (R19 no engenharia#80).

| # | Achado que originou |
|---|---|
| 1 | formacao-dev#358, item 1; #338, item 6 |
| 2 | formacao-dev#359, item 1; #360, item 2 da R19 do Esp QA (arquivo local `orquestrador/esp/qa/revisao-r19-formacao-dev-360-2026-11-24.md`, ainda não colado no PR) |
| 3 | formacao-dev#338, item 5; #359, item 2; #360, item 2 da R19 (mesmo arquivo local) |
| 4 | formacao-dev#358, item 5; #360, item 1 da R19 (mesmo arquivo local) |
| 5 | engenharia#66, ressalva 3 (a caixa e a raiz `.`) |
| 6 | engenharia#66, ressalvas 2 e 4 |
| 7 | engenharia#73, ressalva 1 (contava a mais); o escape #73 → #79 (não contava `Desvio (Decisão 150)`) |
| 8 | engenharia#72, pedido 2; #73, ressalva 4 |
| 9 | onda 1 da Esp Dados (achado A2); engenharia#69, achado 4 |
| 10 | engenharia#69, achado 5 (evidências que não se reproduziam); #72, pedido 2. Completa a definição de pronto ("'Atende' exige comando, data e resultado") |
| 11 | engenharia#67, achados 8 e 9 |
| 12 | engenharia#67, achado 1 |
| 13 | engenharia#67, achado 2 |
| 14 | engenharia#67, achados 3, 4 e 6 |
| 15 | engenharia#72, pedido 3 |
| 16 | formacao-dev#339, B2 e B3 |
| 17 | engenharia#71 (R-c) e #76 |
| 18 | engenharia#71 (R-a e R-b) e #75 |
| 19 | formacao-dev#360, item 3 da R19 do Esp QA (arquivo local, ainda não colado no PR) |
| 20 | formacao-dev#340, item 1 |
| 21 | formacao-dev#358, itens 2 e 6; #359, item 3 |
| 22 | formacao-dev#338, itens 1 e 2; #340, itens 2 a 4 |
| 23 | formacao-dev#358, item 4; #338 |
| 24 | autorrevisão da dona no formacao-dev#359, em relato da sessão comunidade LearnTech (não é achado de R19). A arquitetura de IA teve o mesmo deslize ao escrever o `verificar_links.mjs` (#66) e o `grep` do `docs/MVP.md` (#73), e pegou os 2 antes do commit |
