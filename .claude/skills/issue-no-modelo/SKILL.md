---
name: issue-no-modelo
description: Use para abrir uma issue em repositório do portfólio no modelo (Objetivo, Motivo, Critérios, Fora desta issue), com rótulos e item no Project com todos os campos.
---

# Issue no modelo

Base: [`processo/modelo-issue.md`](../../../processo/modelo-issue.md).

1. **Não duplicar:** antes, `gh issue list -R <dono>/<repo> --state all --search "<palavras>"`. Outra sessão pode estar abrindo a mesma issue: confira também as criadas na última hora. Se já existe, complete a existente.
2. **Corpo** num arquivo (nunca com heredoc aninhado), com as quatro seções. Título com verbo no infinitivo e o resultado. De 3 a 5 critérios conferíveis por comando, tela ou número. Sem dado pessoal nem nome de terceiro.
3. **Depende do responsável?** Rótulo `depende-do-responsavel`, e os critérios viram o passo a passo (onde clicar ou qual comando).
4. **Criar:** `gh issue create -R <repo> --title "..." --body-file corpo.md --label <rótulo>`. Se o rótulo não existir, crie antes com `gh label create`.
5. **Project:** `gh project item-add <número> --owner <dono> --url <issue>` e preencha todos os campos (Status, Prioridade, Tamanho, Origem, Tipo, Frente, Resultado, Depende de, Pontos, Objetivo, Início, Fim) com `gh project item-edit`, com 2 s entre as chamadas.
6. **Referência:** a partir daí, commits e PRs citam a issue (`(#N)`, `Closes #N`). Feche só com evidência e depois do merge na principal.
