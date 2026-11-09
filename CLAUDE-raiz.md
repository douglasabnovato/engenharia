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

## Exceções aceitas pelo responsável

Contas de demonstração públicas e chaves marcadas como risco aceito estão registradas nas ADRs de cada repositório. Não remova nem proponha troca.

## Fim de cada tarefa

- Diga o que foi feito, o que falta e de quem.
- Se aprendeu algo que não está em `engenharia/ia/aprendizados.md`, proponha o item (regra em 1 a 2 linhas + repositório e data) para o coordenador consolidar.
