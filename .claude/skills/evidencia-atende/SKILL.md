---
name: evidencia-atende
description: Use antes de marcar um critério como "Atende" no docs/MVP.md ou de comentar a evidência de uma issue. Garante comando, data e resultado.
---

# Evidência de "Atende"

Base: [`processo/definicao-de-pronto.md`](../../../processo/definicao-de-pronto.md).

Um critério só é **Atende** com os três:
- **Comando** que outra pessoa pode rodar: `npx vitest run`, `gh run view <id>`, `curl -sI <url>`.
- **Data** no formato dd/mm/aaaa.
- **Resultado** com número: `168 testes, 0 falhas`, `0 violações`, `HTTP 200`.

Sem algum dos três, o critério fica **Parcial**.

Comentário na issue:

```
Evidência (dd/mm/aaaa)
- Critério 1: <comando> → <resultado>
- Critério 2: ...
Commit/PR: <hash ou link> · CI: <run>
Falta: <o que falta e de quem>
<sub>por douglas ciborgue</sub>
```

Regras:
- O que depende de deploy ou de conta fica "Parcial" até ser conferido no site publicado.
- Não feche issue `depende-do-responsavel`.
- Não feche sem a evidência dos critérios.
