# Brief · ciclo da faixa de 90%

Modelo de brief para levar um repositório a 90% ou 100% da régua. As decisões D1 a D7 estão em [`decisoes/2026-11-10-ciclo-faixa-90.md`](../../decisoes/2026-11-10-ciclo-faixa-90.md). Leia esse arquivo inteiro antes de começar.

## Leia antes
- `ia/processo-repositorio.md`, `arquitetura/padroes.md`, `processo/fluxo-git.md`, `processo/definicao-de-pronto.md`, `processo/modelo-issue.md`.
- Os temas de `ia/aprendizados.md` da pilha do repositório, sempre com "Windows e Git Bash", "CI" e "Permissões do agente".

## Limites
- Clone novo numa pasta própria do agente (`.../scratchpad/<lote>/<repo>`), nunca os clones da pasta do portfólio.
- Proibido: force push (nem `--force-with-lease`), reescrever histórico, push direto na principal, apagar branch remota, `--no-verify`, mudar Settings, Pages, rulesets, segredos, hospedagem ou contas.
- Negado por permissão: não contorne. Registre no relatório e na issue, e siga.
- Nenhum dado pessoal novo. Nunca imprima token.

## Por repositório
1. **Ler o estado.** A tabela atual do `docs/MVP.md` (ou `documentacao/MVP.md`) na branch `developer/sprint-2026-11-12`, as issues citadas nas linhas que não estão em "Atende" e os comentários delas.
2. **Branches.** `feature/<data>` a partir da sprint. O PR sprint → principal já existe: o trabalho entra nele.
3. **Aplicar as decisões, critério por critério:**
   - **D1 (2):** a meta proposta vira a meta do ciclo. Escreva "Atende: meta decidida pelo coordenador em <data> (decisão D1), revisável pelo responsável" e mantenha o texto da aposta.
   - **D2 (3):** existe teste Playwright do fluxo principal que roda no CI? Se não, crie um (Playwright + `@axe-core/playwright` quando couber), com o `webServer` do próprio build. Em N2 e N3, confira com `curl` que o site publicado responde e que o fluxo depende só do que está no ar. Se depender de backend fora do ar, o 3 continua "Parcial", com o motivo. A issue "pessoa de fora" ganha o rótulo `validacao` e o título "Validar com uma pessoa de fora"; não feche.
   - **D4 (9):** marque como "ilustrativo" na tela cada afirmação sem confirmação, com teste que confira o aviso. Banco no histórico: confira, sem imprimir valores, se nomes e e-mails são fictícios (domínios como `example.com`, nomes genéricos). Se forem, escreva uma ADR que aceita o risco. Se houver dado real, não mexa: registre. Issue com dado de terceiro: tente `gh issue edit`; se negar, registre.
   - **D5 (5), só em N2 e N3:** inclua o GoatCounter com `data-goatcounter="https://douglasabnovato.goatcounter.com/count"`, carregado só em produção, sem cookie, e um evento com o nome do fluxo principal (sem dado pessoal). Teste que o script não carrega no `dev` nem nos testes. O 5 fica "Parcial: código pronto; falta a conta (decisão D5)" até o responsável criar a conta.
   - **D6 (7):** se o site publicado já tem o código da principal, meça com Lighthouse móvel: 3 execuções válidas, mediana, TBT e elemento do LCP. Se o código novo ainda não está no ar, deixe "Parcial" com o motivo.
   - **10:** depois de D3, a principal exige os jobs do CI. Se o 10 estava "Parcial" só porque a Netlify ou a Vercel publica sem esperar o CI, vira "Atende" com a evidência `gh api repos/<dono>/<repo>/rules/branches/<principal>` (regra `required_status_checks`). Se o site sai de uma pasta versionada (`docs/`) ou de deploy manual, prepare um workflow de publicação por Actions, travado por uma Variable, como no `restaurante-churrascaria` (`aprendizados.md`, "Vercel, Netlify e Pages"), e deixe o passo a passo numa issue.
4. **Recalcule** `**Resumo:** X de Y aplicáveis atendidos` e `**Finalizado:**`. Atualize o README ("Estado e próximos passos").
5. **Issues.** Toda pendência do responsável tem issue com `depende-do-responsavel` e passo a passo. Toda tarefa nova vira issue no modelo. Não feche sem evidência.
6. **PR** feature → sprint com lint, testes e build verdes. Espere o run do Actions (`gh run list`), não só os checks externos. Com o CI verde, tente o merge uma vez. Depois, comente no PR sprint → principal o que entrou e os critérios antes → depois.

## Resposta final (até 250 palavras)
Uma linha por repositório: critérios antes → depois (com os números), PRs, issues criadas ou comentadas, o que ficou com o responsável e por quê, e desvios. Depois, lições novas para `aprendizados.md`.
