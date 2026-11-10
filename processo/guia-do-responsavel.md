# Guia do responsável

O que só o dono do repositório pode fazer, em ordem de impacto, e como. Cada item aparece no repositório como issue com o rótulo `depende-do-responsavel` e o passo a passo nos critérios.

Para listar tudo: `https://github.com/issues?q=is%3Aopen+label%3Adepende-do-responsavel+user%3A<dono>`

## 1. Revisar e mesclar os PRs para a principal

Os agentes deixam um PR sprint → principal aberto, com CI verde e o rótulo `revisao-responsavel`. Lista: `https://github.com/pulls?q=is%3Aopen+label%3Arevisao-responsavel+user%3A<dono>`

Em cada PR:
1. Ler o resumo: o que mudou, critérios antes → depois, o que revisar.
2. Aba **Files changed**: conferir o `docs/MVP.md` (uma tabela só) e os itens marcados "para revisão" (troca de versão maior, mudança visível ao usuário, texto escrito em seu nome).
3. Conferir que o CI está verde.
4. **Merge pull request** (merge commit). Ou comentar o que mudar; o próximo ciclo ajusta.

## 2. Proteger a principal

Fecha o critério 10. Duas formas:
- **À mão:** Settings → Rules → Rulesets → New branch ruleset → alvo "Default branch" → marcar *Restrict deletions*, *Block force pushes*, *Require a pull request before merging* (0 aprovações) e, se quiser, *Require status checks to pass* com os jobs do CI → Create.
- **Por comando, vários repositórios:** `bash scripts/configurar-responsavel.sh proteger <repo> [<repo>...]` (leia antes).

Exemplo do ruleset em [`fluxo-git.md`](fluxo-git.md). Depois, comentar "feito" na issue.

## 3. Ligar o GitHub Pages

Para repositórios com workflow de publicação pronto:
- **À mão:** Settings → Pages → Source: **GitHub Actions**; depois Actions → último workflow da principal → *Re-run all jobs*.
- **Por comando:** `bash scripts/configurar-responsavel.sh pages <repo> [<repo>...]`.
- Se o workflow estiver travado por uma Variable: Settings → Secrets and variables → Actions → Variables → criar a variável indicada na issue (ex.: `PAGES_VIA_ACTIONS` = `true`).

Detalhes em [`arquitetura/deploy/pages-vercel-netlify.md`](../arquitetura/deploy/pages-vercel-netlify.md).

## 4. Hospedagem: publicar ou tirar o link

| Situação | O que fazer |
|---|---|
| No ar com versão antiga | Render: *Manual Deploy → Deploy latest commit*. Vercel: *Redeploy* e conferir o Root Directory |
| Fora do ar ou 404 | Criar ou religar o serviço, ou responder na issue "manter como estudo" |
| Nunca publicado | Decidir na issue: publicar (com nome de serviço próprio) ou "só estudo" |
| Serviço pausado (Supabase) | Restaurar o projeto no painel |
| App privado (Streamlit) | App → Settings → Sharing → público |

API com banco: [`arquitetura/deploy/render-atlas.md`](../arquitetura/deploy/render-atlas.md).

## 5. Segurança e dados no histórico

- **Credencial vazada:** revogar no serviço (no Atlas: Database Access → apagar o usuário). Apagar o arquivo não basta.
- **Bancos ou dados pessoais no histórico:** decidir na issue: aceitar (dados de teste) ou reescrever o histórico (você, com `git filter-repo`; os agentes não fazem).
- **Issues antigas com dados de terceiros:** editar ou apagar o texto.

## 6. Confirmar conteúdo

Só você sabe: metas das hipóteses, depoimentos e números publicados, links reais, cargo e selos, clientes citados, decisões de negócio. Responda na própria issue; o próximo ciclo aplica.

## 7. Medição e testes com pessoas

- **Medição de uso** (ex.: GoatCounter, sem dados pessoais): criar a conta e passar o código do site na issue de medição.
- **Testes com pessoas:** seguir o roteiro da issue (cerca de 5 minutos, 5 pessoas) e anotar o resultado nela.

## Como trabalhamos juntos

1. Os agentes trabalham nos repositórios e abrem PRs para a principal; nada entra na principal sem o seu merge.
2. Você faz os passos acima e comenta "feito" ou a decisão na issue.
3. A cada ciclo, o coordenador lê as issues comentadas, aplica as decisões, fecha o que tem evidência e atualiza o `MVP.md`.
4. Toda tarefa nova vira issue no repositório, no [modelo](modelo-issue.md).
