# Definição de pronto

Duas definições: a de uma **mudança** (issue ou PR) e a de um **repositório** ("Finalizado").

## Mudança pronta

- Critérios da issue cumpridos, com evidência.
- Teste automatizado do fluxo alterado, rodando no CI (sem `skip`).
- Erro, vazio e carregamento tratados.
- Teclado e contraste conferidos (claro e escuro).
- Lint, testes e build verdes localmente e no CI.
- `docs/MVP.md` e README atualizados quando a mudança mexe num critério.
- Publicado e verificado no site, quando houver site (até lá, "Parcial").

## "Atende" exige evidência

Um critério só é "Atende" com **comando, data e resultado**. Exemplos:

| Ruim | Bom |
|---|---|
| "Testes passando" | "`npm test` em `backend`: 13 testes, 0 falhas, 09/11/2026" |
| "Acessível" | "`npx playwright test a11y`: axe sem violações em login e painel, claro e escuro, 09/11/2026" |
| "Rápido" | "Lighthouse móvel no site publicado, 3 execuções: 2,1 / 2,3 / 2,2 s, mediana 2,2 s, TBT 90 ms, elemento `h1`, 09/11/2026" |
| "Seguro" | "`npm audit --omit=dev`: 0 vulnerabilidades; Dependabot pela API: 0 alertas abertos, 09/11/2026" |

Sem evidência, o critério é "Parcial" ou "Não atende".

## Repositório "Finalizado"

**Finalizado: sim** quando:
1. todos os critérios aplicáveis (pelo nível, ver [`arquitetura/padroes.md`](../arquitetura/padroes.md)) estão em "Atende", **exceto** os que dependem do responsável; e
2. cada um desses tem uma issue aberta com o rótulo `depende-do-responsavel` e o passo a passo.

Isso separa o que o código entrega do que só uma conta, uma senha ou uma pessoa resolve.

Casos que já apareceram:
- Critério 10 "Parcial" porque a principal não está protegida: não impede "Finalizado", desde que exista a issue de proteção.
- Critério 7 "Parcial" com LCP local abaixo de 2,5 s, mas sem medição no site (que só muda depois do merge do responsável): o processo aceitou "Finalizado: sim" com a issue de medição aberta, e deixou para o responsável decidir se exige a medição no ar.

## Topo do `docs/MVP.md`

```markdown
**Nível:** N1 | N2 | N3
**Resumo:** X de Y aplicáveis atendidos
**Finalizado:** sim | não — o que falta e de quem (#issues)
```

Uma tabela só, a atual. As anteriores vão para "Histórico", com a data.
