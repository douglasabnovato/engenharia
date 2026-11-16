# Modelo de brief: ciclo curto de código

Para quando o repositório já passou por um ciclo completo e falta só o que o código resolve (ex.: LCP acima da meta, erro e vazio em telas, foco num diálogo). Baseado no ciclo de 09/11/2026, que levou 7 repositórios de "Finalizado: não" a "sim".

---

```markdown
# Brief do ciclo de <DD/MM/AAAA> (para agentes)

Leia antes, inteiros: `<caminho>/ia/briefs/<brief completo anterior>.md` (regras, ferramentas, formato),
`<caminho>/ia/aprendizados.md` e a decisão que motiva este ciclo: `<caminho>/decisoes/<arquivo>.md`.

O que muda em relação ao brief completo:

1. **Objetivo:** levar o repositório a "Finalizado: sim", resolvendo só os critérios que o código resolve.
   O que depende do responsável já tem issue; não refaça.
2. **Branches:** clone novo em `<scratchpad>/<pasta>/<repo>` (com `core.longpaths=true`).
   Crie `feature/<AAAA-MM-DD>` **a partir da sprint** `developer/sprint-<AAAA-MM-DD>` (não da principal).
   PR feature → sprint.
3. **Merge:** com CI verde, tente `gh pr merge --merge` uma vez. Se for negado, não insista:
   PR aberto com `revisao-responsavel` e resumo completo; diga isso na resposta final.
4. **Não abra PR para a principal.** Já existe um PR sprint → principal aberto. Ao final, comente nele
   o que foi acrescentado (PR da feature, critérios antes → depois, evidências, o que revisar).
5. **LCP:** build de produção servido com compressão, Lighthouse móvel, 3 execuções válidas,
   `timeout 150` por execução, portas próprias. Registre LCP, TBT e o elemento do LCP.
   Antes de mudar código, leia as fases do LCP no JSON. Se o site só muda depois do merge na principal,
   registre a medição local e deixe "Parcial" com a issue.
6. **MVP.md:** uma tabela só, no topo; anteriores em "Histórico". Seção `## Ciclo de <DD/MM/AAAA>`
   no `docs/PLANO-DE-ACAO.md`.
7. **Issues:** toda tarefa nova não feita vira issue completa no Project. Feche com evidência só
   depois do merge na principal; até lá, comente a evidência na issue.
8. **Revisor independente:** como no brief completo.

Repositórios e o que falta em cada um:
- `<repo>`: <critério e evidência atual, ex.: "LCP local 3,9 s; atraso de renderização; #36">
- ...

Resposta final: blocos ▶ INÍCIO / ■ FIM por repositório, mais 2 a 3 aprendizados novos.
```

---

## Quando usar

- O repositório tem sprint e PR para a principal abertos, aguardando o responsável.
- O que falta é pequeno e medido (um número, uma tela, um teste).
- Trabalhar sobre a sprint faz o trabalho novo entrar no PR que o responsável já vai revisar: um PR por repositório, não dois.
