# Deploy: GitHub Pages, Vercel e Netlify

O que o processo já registrou sobre essas hospedagens. Configurar qualquer uma delas (ligar, trocar fonte, criar variável, mudar diretório) é do **responsável**; o agente prepara o workflow e o passo a passo.

## GitHub Pages

**Ligar (responsável).**
- Pelo painel: Settings → Pages → Source: **GitHub Actions**. Depois, Actions → último workflow da principal → *Re-run all jobs*.
- Por comando: `gh api -X POST repos/<dono>/<repo>/pages -f build_type=workflow` e rodar de novo o último workflow da principal. O script [`scripts/configurar-responsavel.sh`](../../scripts/configurar-responsavel.sh) faz isso para uma lista de repositórios.

**Workflow travado por variável.** Um workflow de publicação pode ficar desligado por uma Variable (ex.: `PAGES_VIA_ACTIONS=true`) até o responsável mudar a fonte do Pages. Assim a principal fica verde sem mexer em configuração.

**SPA com rotas.** O Pages serve arquivos. Com `BrowserRouter`, é preciso `base` no Vite, `basename` no roteador e um `404.html` que volte para o `index.html`. Alternativa: `HashRouter`.

**Caminho base no Windows.** No Git Bash, `PUBLIC_URL=/movies` vira `C:/Program Files/Git/movies`. Usar `MSYS_NO_PATHCONV=1`.

**Medir como o Pages serve.** O Pages comprime. Medir localmente com um servidor que comprime (`npx serve`). `http-server` sem `-g` inflou o JS de 61 para 181 KB e o LCP de ~2,3 para ~3,0 s.

**Publicado não quer dizer atualizado.** HTTP 200 pode servir um build antigo. Comparar o HTML publicado com o `index.html` da principal (ou o hash do bundle).

**README honesto.** Procurar no README frases que digam que o CI publica o site e conferir no workflow. Num repositório era falso.

## Vercel

- **Status vermelho por configuração.** Um status da Vercel pode ficar vermelho por meses por causa de configuração (ex.: *Root Directory* errado), sem relação com o código. Nesse caso decide o CI do GitHub; a correção é do responsável (Settings → Root Directory).
- **Sem WebSocket e sem disco** nas funções serverless: não serve para API com Socket.IO ou upload local.
- Versão antiga no ar: o responsável faz *Redeploy* da principal.

## Netlify

- Os status da Netlify chegam com `conclusion` nulo no `statusCheckRollup` do GitHub. Decidir pelo **código de saída** de `gh pr checks <n>`, não pelo campo.
- As mesmas limitações da Vercel para API com WebSocket.

## Outras hospedagens do portfólio

| Hospedagem | Situação típica | O que o responsável faz |
|---|---|---|
| Supabase | Projeto pausado por inatividade | Restaurar o projeto no painel |
| Streamlit Cloud | App privado | App → Settings → Sharing → público |
| Render | Versão antiga no ar | *Manual Deploy → Deploy latest commit* (ver [`render-atlas.md`](render-atlas.md)) |

## O que o agente não faz

- Ligar ou trocar a fonte do Pages, criar variáveis ou segredos, mudar configurações da Vercel ou da Netlify.
- Criar workflow agendado de publicação (foi negado pela permissão; vira issue).
- Nesses casos: issue com `depende-do-responsavel` e o passo a passo nos critérios de entrega.
