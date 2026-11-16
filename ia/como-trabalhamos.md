# Como trabalhamos com IA (Claude Code)

O modelo que levou 39 repositórios a MVP entre outubro e novembro de 2026: uma pessoa decide, um coordenador organiza e agentes executam em lotes.

## Papéis

| Papel | Quem | Faz | Não faz |
|---|---|---|---|
| **Responsável** | O dono do portfólio | Decide problema, metas e prioridades; cria contas e segredos; configura hospedagem e proteção; revisa e mescla na principal | — |
| **Coordenador** | Sessão principal do Claude Code | Escreve os briefs; distribui repositórios em lotes; lê os relatórios; consolida aprendizados no processo; roda os scripts de estado e de Project; registra decisões | Código nos repositórios (delega) |
| **Agente** | Subagente com um brief | Executa o processo em 1 a 3 repositórios, um depois do outro, até o fim | Mexer em configuração, segredos ou principal |
| **Revisor independente** | Subagente que não viu o código | Lê só o diff e a seção do plano e aponta problemas de correção | Sugerir estilo ou reescrever |

## O ciclo

1. **Pedido do responsável** em uma ou duas frases (ex.: "levar cada repositório a MVP, com 5 issues de próximos passos").
2. **Decisões** do coordenador, com justificativa, num documento datado (ver [`decisoes/`](../decisoes/)).
3. **Piloto** num repositório. O que der errado vira aprendizado antes do lote.
4. **Brief** comum para os agentes (modelos em [`briefs/`](briefs/)).
5. **Lotes** de 2 a 5 agentes em paralelo, 1 a 3 repositórios cada.
6. **Relatório** de cada agente no formato ▶ INÍCIO / ■ FIM.
7. **Consolidação:** aprendizados novos entram em [`aprendizados.md`](aprendizados.md); pendências do responsável viram issues com `depende-do-responsavel`.
8. **Revisão do responsável:** PRs sprint → principal com o rótulo `revisao-responsavel`.

## Briefs

O brief é o único contexto do agente. Ele diz:
- o que ler antes (processo, aprendizados, decisão que motivou o ciclo);
- ferramentas e onde clonar (sempre numa pasta temporária, nunca na cópia local de trabalho);
- regras do responsável que valem acima do processo;
- os passos em cada repositório;
- o formato exato da resposta final.

Briefs de ciclos seguintes herdam o anterior e listam só o que muda.

## Revisor independente

Depois de lint, testes e build verdes, o agente lança um subagente que **não viu o código**:
- entrada: só `git diff <sprint>...<feature>` e a seção do plano do ciclo;
- pedido: só problemas de correção (bug, regressão, teste que não testa);
- se não houver ferramenta para isso, o PR diz que a revisão independente não foi feita.

Um revisor que conhece a intenção tende a confirmá-la. Por isso ele recebe o diff, não a conclusão.

## Acompanhamento: ▶ INÍCIO e ■ FIM

Cada repositório gera dois blocos na resposta do agente:

```
▶ INÍCIO <repo> · nível · critérios <x>/<aplicáveis> · CI · link responde?
Plano: <3 linhas>

■ FIM <repo> · critérios <antes> → <depois> · Finalizado sim/não
PRs: <links> · Issues novas: <números> · Testes/build: <resumo da saída>
Para revisão do responsável: <lista ou "nada">
Depende do responsável: <issues>
Desvios: <bloqueios, permissões negadas, o que não deu>
```

Depois, 2 a 3 aprendizados novos (sem repetir os registrados). O coordenador lê só isso; o que não está no bloco não existe.

## O que fica com o responsável

- Merge na principal (os PRs sprint → principal ficam abertos com `revisao-responsavel`).
- Proteção da principal (ruleset) e configurações do repositório.
- Contas, senhas, tokens e segredos; hospedagem (Pages, Render, Vercel, Netlify, Supabase, Streamlit).
- Revogar credenciais vazadas e reescrever histórico.
- Conteúdo que só ele sabe: metas, depoimentos, números publicados, clientes, cargo.
- Medição de uso (criar a conta) e testes com pessoas.

Tudo isso vira issue com `depende-do-responsavel` e, nos critérios de entrega, o passo a passo (onde clicar ou qual comando).

## Limites e permissões

O agente roda com um classificador de permissões. Algumas ações foram negadas e assim ficam:

| Ação | O que aconteceu | Como se registra |
|---|---|---|
| Merge feature → sprint | Negado em parte dos repositórios ("Merge Without Review"); passou em outros | Tentar **uma vez**. Se negar, PR aberto com `revisao-responsavel` e issue "Mesclar o ciclo" com o passo a passo |
| Merge de PR do Dependabot | Negado | Citar na issue de manutenção |
| Apagar branch remota (`git push --delete`) | Negado | Fica com o responsável; não insistir |
| Criar workflow agendado de publicação | Negado | Vira issue |
| Force push, inclusive `--force-with-lease` | Proibido pelo processo | Nunca usar. Um uso por engano foi registrado como desvio |

Regra geral: **se uma ação for bloqueada, não contornar.** Registrar no relatório, abrir issue se for o caso e seguir para o próximo repositório.

Outras regras fixas:
- Nunca imprimir nem digitar tokens ou senhas.
- Push a cada commit: nada fica só no clone (uma queda de sessão já deixou 5 agentes com trabalho apenas local).
- Nenhum dado pessoal novo.
- Não fechar issue sem evidência; não fechar issue que depende do responsável.
- Não escrever em nome do responsável (depoimentos, textos de venda) sem destacar no PR.

## Medir o progresso

Índice do ciclo (0 a 100), por exemplo:
- 60% critérios aplicáveis atendidos (sem os "Não se aplica");
- 20% repositórios com pelo menos 5 issues abertas de próximos passos, com 3 ou mais critérios;
- 20% repositórios com o ciclo integrado.

Medir resultado, não volume: um índice antigo que contava issues e campos marcou 90; com os critérios de MVP, caiu para 74.
