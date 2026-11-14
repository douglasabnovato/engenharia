# Modelo de brief: ciclo completo por repositório

Consolidado dos briefs de 03/11, 07/11 e 09/11/2026. Troque os `<placeholders>` e apague o que não se aplica. O brief é o único contexto do agente: tudo o que ele precisa saber está aqui ou num arquivo citado.

---

```markdown
# Brief do ciclo de <DD/MM/AAAA> (para agentes)

Você executa o ciclo de <DD/MM/AAAA> nos repositórios indicados na sua tarefa, um depois do outro,
no GitHub de `<dono>`. Trabalhe sozinho até o fim, sem pedir confirmação; só pare diante de algo
irreversível. Tudo em português do Brasil, frases curtas e diretas.

## Leia antes, inteiros
- `<caminho>/engenharia/ia/processo-repositorio.md` (passos 0 a 8, decisões, limites).
- `<caminho>/engenharia/ia/aprendizados.md`, em especial os temas da pilha do repositório.
- `<caminho>/engenharia/arquitetura/padroes.md` (níveis e régua dos 12 critérios).
- A decisão que motiva este ciclo: `<caminho>/decisoes/<arquivo>.md`.

## Ferramentas
- GitHub CLI: `<caminho do gh>` (autenticado; nunca imprima nem digite tokens). Bash.
- Clone novo com `git clone -c core.longpaths=true` em `<scratchpad>/<pasta-do-ciclo>/<repo>`.
  NUNCA trabalhe nem faça commit em `<pasta local de uso diário>/<repo>`.
- Busca na web para a pesquisa (cite as fontes por link, com palavras próprias).
- Commits terminam com `Co-Authored-By: <linha de atribuição>`; corpo dos PRs termina com `<linha do PR>`.
  Use `--body-file` com arquivo no scratchpad.
- Push a cada commit.

## Regras do responsável (valem acima do processo onde divergirem)
1. `docs/MVP.md` é a fonte única do estado: uma tabela só, a atual, no topo; anteriores em "Histórico".
   Linhas `**Resumo:** X de Y aplicáveis atendidos` e `**Finalizado:** sim|não`.
2. O plano novo vai numa seção `## Ciclo de <DD/MM/AAAA>` no `docs/PLANO-DE-ACAO.md`.
3. Régua: em N1, critérios 5 e 7 são "Não se aplica (N1)". Critério 10 só é "Atende" com a principal protegida.
4. Finalizado = todos os aplicáveis em "Atende", exceto os que dependem do responsável, cada um com
   issue `depende-do-responsavel`.
5. Pelo menos 5 issues abertas de próximos passos, no modelo (Objetivo, Motivo, 3 a 5 Critérios de entrega,
   Fora desta issue). Reaproveite as existentes. Project #<n> (`gh project item-add <n> --owner <dono> --url <url>`).
   Não preencha os campos do Project à mão.
6. Branches: `feature/<AAAA-MM-DD>` → `developer/sprint-<quinta AAAA-MM-DD>` → principal.
   <Exceções de nome por repositório, se houver.> Crie a sprint a partir da principal se não existir.
7. Merge feature → sprint: com CI verde, tente uma vez. Se for negado, não insista: PR aberto com
   `revisao-responsavel` e resumo completo.
8. NÃO mescle na principal. PR sprint → principal com `revisao-responsavel` e resumo (o que mudou,
   critérios antes → depois, evidências, o que revisar), aberto.
9. Proibido: push direto na principal, force push (inclusive `--force-with-lease`), reescrever histórico;
   mexer em segredos, `.env`, hospedagem ou proteção de branch; mesclar Dependabot com versão maior;
   fechar issue sem evidência; escrever em nome do responsável sem destacar no PR; apagar branches remotas.
   Se uma ação for bloqueada por permissão, não contorne: registre e siga.
10. Todo "Atende" cita o comando, a data e o resultado.
11. Toda tarefa nova que você identificar e não fizer vira issue. Se depender do responsável:
    rótulo `depende-do-responsavel` e, nos critérios, o passo a passo (onde clicar ou qual comando).
12. Exceções aceitas pelo responsável (não remover nem propor troca): <lista>.

## Passos em cada repositório
Preparar → analisar → pesquisar (2 a 4 buscas, com fonte) → documentar → executar em fatias pequenas
(segurança; honestidade do `MVP.md`; falhas, acessibilidade e testes do fluxo principal; uma melhoria
da pesquisa) → verificar (lint, testes, build; depois um revisor independente que recebe só
`git diff <sprint>...<feature>` e a seção do plano e aponta só problemas de correção) → integrar →
issues → `MVP.md` e README.

<N2/N3: LCP com build de produção, Lighthouse móvel, 3 execuções válidas, `timeout 150`,
registrar LCP, TBT e elemento. Critério 7 só "Atende" medido no site publicado.>

Escopo enxuto: se o tempo apertar, termine o repositório atual com tudo enviado e vá para a resposta final.

## Resposta final
Para cada repositório:

    ▶ INÍCIO <repo> · nível · critérios <x>/<aplicáveis> · CI · link responde?
    Plano: <3 linhas>

    ■ FIM <repo> · critérios <antes> → <depois> · Finalizado sim/não
    PRs: <links> · Issues novas: <números> · Testes/build: <resumo da saída>
    Para revisão do responsável: <lista ou "nada">
    Depende do responsável: <issues>
    Desvios: <bloqueios, permissões negadas, o que não deu>

Depois, 2 a 3 aprendizados novos para o processo (não repita os registrados).
```

---

## Notas para quem escreve o brief

- Cite **arquivos**, não resuma o conteúdo deles: o agente lê.
- Diga o que já foi descartado, para o agente não repetir.
- Um ciclo seguinte pode ter brief curto: "leia o brief de <data>; o que muda: ...". Ver [`ciclo-curto.md`](ciclo-curto.md).
- Divida os repositórios em lotes de 1 a 3 por agente; agentes demais na mesma máquina disputam CPU e portas.
