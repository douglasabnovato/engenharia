# Processo por repositório

Os passos que um agente segue em cada repositório num ciclo. Armadilhas conhecidas estão em [`aprendizados.md`](aprendizados.md); leia antes.

Para um projeto **novo**, o caminho é outro: seis fases com portões (enquadrar, descobrir, fundar com esqueleto no ar, construir, validar, operar). O resumo está no fim deste arquivo.

## Decisões que valem em todo ciclo

| # | Decisão | Por quê |
|---|---|---|
| 1 | O `docs/MVP.md` é a fonte única do estado, com **uma tabela só**, a atual, no topo. As anteriores vão para "Histórico" | Documentos demais se contradizem |
| 2 | Régua por nível: em N1, critérios 5 e 7 são "Não se aplica (N1)" | Projeto de curso não tem usuário nem hospedagem obrigatória |
| 3 | Critério 10 só é "Atende" com a principal protegida | Sem proteção, um push direto publica sem CI |
| 4 | **Finalizado** = todos os critérios aplicáveis em "Atende", exceto os que dependem do responsável, e cada um destes tem issue com `depende-do-responsavel` | Separa o que o código entrega do que só uma conta ou uma pessoa resolve |
| 5 | Pelo menos 5 issues abertas de próximos passos por repositório, cada uma com 3 a 5 critérios verificáveis | Deixa o próximo passo pronto para quem vier |
| 6 | Conteúdo novo vem de pesquisa com fonte citada, escrito com palavras próprias | Evita afirmação sem origem e cópia |
| 7 | Merge na sprint só com CI verde; vermelho ou ausente bloqueia | Sem CI, colar no PR a saída do build e dos testes |
| 8 | **Nada é mesclado na principal pelo agente.** PR sprint → principal aberto com `revisao-responsavel` | Produção é decisão do responsável |
| 9 | Todo "Atende" cita comando, data e resultado | Sem evidência, não conta |

## Passos

**0. Preparar.**
- Clonar de `origin` numa pasta temporária: `git clone -c core.longpaths=true <url>`. Nunca trabalhar na cópia local de uso diário.
- Conferir `git config core.hooksPath`, `git ls-files | wc -l` contra `git ls-tree -r HEAD | wc -l` (índice completo) e `git ls-files --eol`.
- Branch de sprint `developer/sprint-<próxima quinta>`; se não existir, criar a partir da principal. Criar `feature/<data de hoje>` a partir dela (ver [`processo/fluxo-git.md`](../processo/fluxo-git.md)).
- Abrir o workflow de CI e conferir que ele dispara em PR para `developer/**`.

**1. Analisar.** Portão: dá para dizer o problema em uma frase?
- Tema, público, README, `docs/MVP.md`, demais documentos.
- Issues abertas **e os comentários**, PRs, Dependabot (pela API), último CI da principal.
- Link publicado com `curl`, e comparar o HTML com o repositório (versão e dono).
- Conferir se as ADRs foram cumpridas no código.

**2. Pesquisar.** 2 a 4 buscas sobre o tema: o que produtos parecidos têm, guias oficiais da tecnologia, boas práticas. Anotar a fonte de cada ideia.

**3. Documentar.** Portão: o plano cabe no tempo do ciclo?
Seção `## Ciclo de DD/MM/AAAA` no `docs/PLANO-DE-ACAO.md`:
- **Produto:** problema e público, hipótese e meta, o que a pesquisa trouxe (com fonte), backlog priorizado (impacto × esforço), fora do escopo.
- **Engenharia:** arquitetura em 3 a 5 linhas, riscos, qualidade (testes, acessibilidade, desempenho, segurança), definição de pronto.
- **Plano de ação:** o que este ciclo executa e o que vira issue.

**4. Executar.** Portão: CI verde. Fatias pequenas, cada uma testável, nesta ordem:
1. Segurança e dados pessoais.
2. Honestidade: resumo do `MVP.md` batendo com a tabela; régua do nível; critério 10 conforme a decisão 3.
3. Critérios que o código resolve: falhas tratadas (com teste), acessibilidade (foco, contraste, teclado), testes do fluxo principal, documentação.
4. Uma ou duas melhorias vindas da pesquisa, com teste.

Commits pequenos em português, push a cada commit. Lint, testes e build antes do push.

**5. Verificar e integrar.**
- Revisor independente com só o diff (ver [`como-trabalhamos.md`](como-trabalhamos.md)).
- PR `feature` → sprint; esperar o CI; tentar o merge uma vez se verde.
- PR sprint → principal com `revisao-responsavel` e resumo: o que mudou, critérios antes → depois, evidências, o que revisar. Deixar aberto.
- Conferir o número de arquivos do PR (número inesperado denuncia índice quebrado).

**6. Issues.** Pelo menos 5 abertas de próximos passos, no [modelo](../processo/modelo-issue.md), com rótulos e no Project. Toda tarefa identificada e não feita vira issue. Fechar com evidência só depois do merge na principal; antes, comentar a evidência.

**7. Atualizar o estado.**
- `docs/MVP.md`: tabela única com evidência e data, `**Resumo:** X de Y aplicáveis atendidos`, linha de nível e `**Finalizado:** sim|não`.
- README: seção "Estado e próximos passos" com o que foi feito (com PR), o que queremos fazer (issues) e onde está a documentação. Link publicado só se responder hoje.
- N2 e N3: LCP medido (3 execuções válidas, mediana, TBT e elemento do LCP).

**8. Registrar.** Pendências do responsável em issues com `depende-do-responsavel`. Lições novas voltam para [`aprendizados.md`](aprendizados.md) pelo coordenador.

## Limites

- Não alterar configurações (Pages, proteção, segredos, Vercel, Render, Netlify, Supabase), não criar contas, não digitar senhas ou tokens.
- Não reescrever histórico, não usar force push (nem `--force-with-lease`), não apagar branches remotas.
- Não mesclar Dependabot com troca de versão maior.
- Nenhum dado pessoal novo.
- Se uma ação for bloqueada por permissão: não contornar, registrar e seguir.

## Projeto novo: seis fases

| Fase | Nome | Duração | Portão |
|---|---|---|---|
| 0 | Enquadrar | 2 a 5 dias | Qualquer pessoa entende o problema em uma frase, e existe um número que diz se a aposta deu certo? |
| 1 | Descobrir | 1 a 2 semanas | 3 de 5 pessoas confirmaram o problema e concluíram o fluxo no protótipo? |
| 2 | Fundar: esqueleto no ar | 1 sprint | Um commit na principal chega ao site sem passo manual, e a medição já registra visitas? |
| 3 | Construir | sprints de 1 semana | O fluxo principal funciona no site publicado, e uma pessoa o conclui sem ajuda? |
| 4 | Validar e decidir | 1 a 2 semanas | A métrica atingiu a meta? Se não, a mudança de rumo está escrita? |
| 5 | Operar e evoluir | contínuo | Dependabot semanal, revisão mensal do backlog, métricas DORA |

Lições que geraram essas fases: critérios de MVP escritos depois do código; hospedagem e contas deixadas para o fim viraram o gargalo; dados pessoais em bancos versionados; issues sem objetivo nem critério foram fechadas como não planejadas. Por isso: `MVP.md` no primeiro dia, contas e esqueleto no ar na Fase 2, LGPD antes do primeiro commit, toda issue com critérios.

Referências usadas: Stage-Gate (Cooper, 1990), esqueleto ambulante (Cockburn, 2004), Lean UX (Gothelf; Seiden, 2013), descoberta contínua (Torres, 2021), Continuous Delivery (Humble; Farley, 2010), Accelerate/DORA (Forsgren; Humble; Kim, 2018), ISO/IEC 25010, LGPD (Lei 13.709/2018).
