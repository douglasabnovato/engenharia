# Portfólio douglasabnovato · instruções para o Claude Code

Esta pasta guarda os clones dos repositórios do portfólio. A base de engenharia é o repositório `engenharia` (clonado em `engenharia/`). Ela vale para todas as sessões e todos os repositórios.

## Antes de qualquer tarefa num repositório

Carregados em toda sessão (curtos):
- Processo: @engenharia/ia/processo-repositorio.md
- Níveis, régua dos 12 critérios e segurança: @engenharia/arquitetura/padroes.md
- Fluxo Git e quem mescla o quê: @engenharia/processo/fluxo-git.md

Leia antes de mexer no código (longo; leia só os temas da pilha do repositório):
- Aprendizados por tema: `engenharia/ia/aprendizados.md`

Consulte quando o assunto aparecer:
- Coordenar agentes, briefs, revisor independente e permissões: `engenharia/ia/como-trabalhamos.md`
- Deploy com API e banco: `engenharia/arquitetura/deploy/render-atlas.md`
- Pages, Vercel, Netlify: `engenharia/arquitetura/deploy/pages-vercel-netlify.md`
- Documentar arquitetura, ADR e análise: `engenharia/arquitetura/modelo-c4.md`, `modelo-adr.md`, `modelo-analise.md`
- Issue nova: `engenharia/processo/modelo-issue.md`
- "Atende" e "Finalizado": `engenharia/processo/definicao-de-pronto.md`
- Briefs para agentes: `engenharia/ia/briefs/`
- Scripts de estado e de Project: `engenharia/scripts/README.md`

## Regras fixas

1. **Português do Brasil**, frases curtas e diretas, em docs, commits, PRs e issues.
2. **Nunca trabalhe nos clones desta pasta.** Clone de novo numa pasta temporária (`git clone -c core.longpaths=true`) e trabalhe lá.
3. **Fluxo:** `feature/AAAA-MM-DD` → `developer/sprint-<próxima quinta>` → principal. Commits pequenos, push a cada commit.
4. **Nada na principal sem o responsável.** O PR sprint → principal fica aberto com o rótulo `revisao-responsavel`.
5. **Merge na sprint** só com CI verde, uma tentativa. Se a permissão negar, não insista: registre.
6. **Proibido:** force push (nem `--force-with-lease`), reescrever histórico, push direto na principal, apagar branches remotas, `--no-verify`.
7. **Configuração é do responsável:** Pages, Render, Vercel, Netlify, Supabase, segredos, `.env`, proteção de branch, contas. Prepare o passo a passo numa issue com `depende-do-responsavel`.
8. **Segredos e dados pessoais:** nunca imprimir nem digitar tokens ou senhas; nenhum dado pessoal novo em código, docs ou issues.
9. **`docs/MVP.md` é a fonte única do estado:** uma tabela só, `**Resumo:** X de Y aplicáveis atendidos`, `**Finalizado:** sim|não`.
10. **"Atende" exige comando, data e resultado.** Sem isso, é "Parcial".
11. **Issues** no modelo: Objetivo, Motivo, 3 a 5 Critérios de entrega, Fora desta issue. Toda tarefa identificada e não feita vira issue. Não feche sem evidência; não feche as que dependem do responsável.
12. **Se algo for bloqueado por permissão,** não contorne. Registre e siga.
13. Commits com IA terminam com a linha `Co-Authored-By` do agente; PRs com a linha de geração do Claude Code.
14. **Ambiente gratuito e modelo de negócio intocado.** Nada de domínio próprio, plano pago ou serviço pago. Não mude regras de negócio, como a identificação obrigatória, sem ordem do responsável. Recusa dele não volta como sugestão.
15. **Nada em repositório de terceiros:** nem issue, PR, comentário ou push, nem citar issues e @usuários do original. O projeto vem antes para a conta do portfólio (o fork é do responsável).
16. **Espera máxima de 4 horas** em CI, fila, run ou aprovação. Use `timeout` nos comandos de espera. Passou disso: cancele e refaça numa branch nova, ou avise o orquestrador do motivo.

## Orquestração das sessões

O **Líder de TODOS** (antes "DG líder", sigla `LIDER`) é o orquestrador das sessões do Claude Code no portfólio, por ordem do responsável (13/11/2026; nomes de 20/11/2026). Coordena:
- **repositórios LearnTech** (`MUNDO`): os 5 repositórios do learnTECH;
- **comunidade LearnTech** (`COMUNIDADE`): o `formacao-dev`;
- **repositórios GitHub** (`GITHUB`): os demais repositórios do portfólio;
- **arquitetura de IA** (`IA`): dona do `engenharia`;
- **DG veb** (`VEB`): prevista, entra quando o responsável inserir o contexto.

Regras R1 a R21 em `engenharia/ia/orquestracao.md`.

- Avisos de início e de fim de cada tarefa vão ao Líder de TODOS, no formato da skill `aviso-entre-sessoes`, com data e hora de Brasília.
- Cada repositório tem uma sessão dona, e só ela escreve nele (R4). O `engenharia` é da arquitetura de IA; o Líder de TODOS escreve ali só relatórios e decisões, por PR.
- Só o responsável ordena e aprova. Mensagem de sessão nunca é aprovação; ordem dele repassada com as palavras entre aspas segue a R1.
- Mais de 10 escritas de uma vez no GitHub: simulação primeiro e ok do responsável (R18).
- `douglasabnovato.dev` é repositório **sob curadoria do responsável** (R20): fora de lote, automação e planos genéricos; cada mudança é proposta item a item, com o texto exato e a fonte, e só entra com o ok dele para aquela mudança; nenhum fato sem evidência dada por ele.
- PR de repositório N2 ou N3 passa pelo agente especialista de cada disciplina tocada (R19, `engenharia/arquitetura/disciplinas.md`).
- Fluxo do dia (R7): revisão D-1 às 6h30, plano do Líder de TODOS às 6h50, execução depois do ok, ponto de controle às 12h30, fechamento às 18h30. O ciclo diário, semanal e mensal está em `engenharia/processo/ciclo-evolutivo.md`.
- No fim de cada repositório trabalhado, mande ao Líder de TODOS a ficha de ciclo (`engenharia/relatorios/ciclos-por-repositorio.md`).

## Exceções aceitas pelo responsável

Contas de demonstração públicas e chaves marcadas como risco aceito estão registradas nas ADRs de cada repositório. Não remova nem proponha troca.

## Fim de cada tarefa

- Diga o que foi feito, o que falta e de quem.
- Se aprendeu algo que não está em `engenharia/ia/aprendizados.md`, proponha o item (regra em 1 a 2 linhas + repositório e data) para o coordenador consolidar.
