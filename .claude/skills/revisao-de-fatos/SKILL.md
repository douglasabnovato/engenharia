---
name: revisao-de-fatos
description: Use antes de publicar um documento, roteiro ou relatório que cita números, datas, nomes de commits, PRs ou issues. Confere cada fato contra a fonte.
---

# Revisão de fatos

Num roteiro de 12/11/2026, a revisão achou 10 erros, entre eles um placar errado e uma data trocada.

1. Liste cada afirmação verificável do texto: número, data, hash, PR, issue, nome de arquivo ou link.
2. Para cada uma, ache a fonte primária: `gh`, `git log`, o arquivo ou `curl` do link.
3. Se o texto for longo, delegue ao agente `revisor-de-fatos`. Ele recebe o texto e a lista de fontes, **não** a sua conclusão.
4. Corrija cada achado e registre a correção na lista: "dizia X, a fonte diz Y".
5. O que não tem fonte sai do texto ou vira "a confirmar".

Saída: a tabela `afirmação · fonte · confere? · correção`.
