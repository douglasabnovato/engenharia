# Padrões de arquitetura e qualidade

O que todo repositório do portfólio segue: o nível do projeto, a régua de 12 critérios, as pilhas de referência e as regras de segurança.

## 1. Níveis

Cada repositório declara o nível no topo do `docs/MVP.md`. O nível muda o que se cobra.

| Nível | Nome | O que é | Exemplos |
|---|---|---|---|
| N1 | Estudo | Projeto de curso ou exercício. Não tem usuário real nem hospedagem obrigatória | `aircnc`, `proffy`, `be-the-hero`, `jobs-calc`, `niky` |
| N2 | Vitrine | Mostra trabalho a quem visita o portfólio. Precisa estar no ar e rápido | `movies`, `headset`, `e-commerce-t-shirt`, `restaurante-churrascaria` |
| N3 | Produto | Tem público e regra de negócio próprios | `components`, `facil-admin-plataforma`, `douglasabnovato.dev` |

Regras:
- Em N1, os critérios 5 (medição de uso) e 7 (desempenho no ar) ficam "Não se aplica (N1)" e saem do denominador.
- Em N2 e N3, os 12 critérios valem.
- Não simular produto em projeto de curso: a meta de um N1 é o fluxo rodar na tela e nos testes.

## 2. Régua dos 12 critérios

Cada critério recebe uma situação: **Atende**, **Parcial**, **Não atende** ou **Não se aplica (N1)**.
"Atende" exige evidência com **comando, data e resultado** (ver [`processo/definicao-de-pronto.md`](../processo/definicao-de-pronto.md)).

| # | Critério | Como verificar | O que conta como evidência |
|---|---|---|---|
| 1 | Problema e público claros | Dá para explicar em uma frase | Frase no README ou no `MVP.md` |
| 2 | Hipótese a validar | Aposta escrita, com meta | "Acreditamos que X fará Y; saberemos quando Z" no `MVP.md` |
| 3 | Fluxo principal completo | Uma pessoa conclui sem ajuda | Teste de ponta a ponta no navegador (Playwright) passando no CI. Teste só de API não basta: um POST real pelo navegador pega erros de origem e de CORS |
| 4 | Escopo enxuto | O que não entra está registrado | Seção "Fora do MVP" |
| 5 | Medição de uso | A métrica principal é coletada | Painel da ferramenta (ex.: GoatCounter) com visitas. Depende de conta do responsável |
| 6 | Falhas tratadas | Erro, vazio e carregamento têm resposta | Testes que simulam falha de rede, lista vazia e espera |
| 7 | Desempenho aceitável | LCP até 2,5 s no celular | Lighthouse móvel no **site publicado**, 3 execuções válidas, mediana, com TBT e elemento do LCP. Medição local deixa o critério em "Parcial" |
| 8 | Acessibilidade básica | axe e teclado | axe sem violações (claro e escuro, largura de desktop, dados reais) e teste de teclado (Tab, Esc, foco visível) |
| 9 | Segurança e conformidade | Riscos decididos | `npm audit --omit=dev` (ou `pnpm audit --prod`) e alertas do Dependabot pela API; sem segredo no código; dados pessoais decididos |
| 10 | Entrega confiável | CI verde antes de entrar na principal | CI nos PRs **e** principal protegida (ruleset). Sem proteção, fica "Parcial" |
| 11 | Testes dos fluxos críticos | Testes automatizados no CI | Log do CI sem `# skipped` nos testes do fluxo principal |
| 12 | Documentação honesta | Qualquer pessoa roda o projeto | README com comandos conferidos contra o `package.json`; link publicado só se responder hoje |

**Resumo** no topo do `MVP.md`: `**Resumo:** X de Y aplicáveis atendidos` e `**Finalizado:** sim|não`.

## 3. Pilhas de referência do portfólio

Não são obrigatórias. São o que já foi testado e tem armadilhas conhecidas em [`ia/aprendizados.md`](../ia/aprendizados.md).

| Camada | Pilha | Onde aparece |
|---|---|---|
| Web (SPA) | React 18/19 + Vite, Vitest, Testing Library | maioria dos repositórios web |
| Web (Vue) | Vue 3 + Vite | `cm-quiz-app` |
| Monorepo | pnpm workspaces com catálogo | `components` |
| API | Node 22+ com Express 5, `zod`, `helmet` | `aircnc`, `proffy`, `be-the-hero` |
| Banco | MongoDB Atlas M0 com Mongoose 8; SQLite (`better-sqlite3`) em estudos; Supabase; Firestore | vários |
| Tempo real | Socket.IO com token no handshake | `aircnc` |
| Mobile | Expo SDK 57 + React Navigation 7 | `aircnc`, `be-the-hero`, `dev-radar` |
| Dados e painéis | Python + Streamlit | `biblioteca` |
| PHP | Composer, `composer audit` | `e-commerce-t-shirt` |
| SAP | UI5 / Fiori | `learning-portal-fiori-sap` |
| Testes de interface | Playwright + `@axe-core/playwright` | quase todos |
| Desempenho | Lighthouse móvel (`npx lighthouse`) | N2 e N3 |
| Hospedagem | GitHub Pages, Render, Vercel, Netlify, Supabase, Streamlit Cloud | ver [`deploy/`](deploy/) |

Padrões de código que se repetiram e funcionaram:
- **Repositório injetado** (Mongo em produção, memória nos testes): a API se testa sem banco.
- **Validação só no servidor**, uma regra para web e mobile.
- **Cliente HTTP único** (`lib/api.js`) por app, com a URL base vinda de variável (`VITE_API_URL`, `EXPO_PUBLIC_API_URL`).
- **`/health`** em toda API. Mas `/health` que não toca o banco não prova a conexão: ter também uma rota ou um log que leia o banco.

## 4. Segurança

### Segredos
- Nunca no código, nos docs nem nas issues. Só em variáveis de ambiente da hospedagem ou do Actions.
- Versionar só `.env.example`, com os **nomes** das variáveis.
- Apagar um arquivo com senha **não** revoga a senha: ela segue no histórico. Revogar (apagar o usuário ou trocar a chave) é do responsável.
- Ao achar um vazamento, procurar também o nome do usuário da credencial e frases como "senha removida" nos docs, que podem afirmar algo falso.
- Reescrever histórico (`git filter-repo`) é decisão e ação do responsável. Agentes não fazem.

### Usuários de banco por app
- Um usuário por app, com `readWrite` **só no banco daquele app**. Uma senha vazada afeta um app só.
- Nunca usar usuário administrador do cluster numa aplicação.
- Senha só com letras e números (`@`, `:` e `/` quebram a URI se não forem codificados).
- Detalhes do Atlas em [`deploy/render-atlas.md`](deploy/render-atlas.md).

### Dados pessoais (LGPD)
- Decidir na Fase 0: o que se coleta, onde fica, quem vê.
- Nenhum dado pessoal novo em código, documentos, issues ou dados de teste. Usar e-mails e nomes fictícios.
- Banco versionado com dados no histórico: aceitar (dados de teste) ou reescrever o histórico é decisão do responsável.
- Contas de demonstração públicas, quando intencionais, ficam registradas em ADR para que ninguém as remova sem saber.
