# Deploy: API + site no Render com MongoDB Atlas M0

Guia genérico para publicar, sem custo, uma API Node (Express) e um site estático (Vite) no Render, com banco no MongoDB Atlas M0. Baseado no deploy do `aircnc` em 09/11/2026.

Quem faz: contas, senhas e cliques nos painéis são do **responsável**. O agente prepara o `render.yaml`, o `.env.example`, o README e este passo a passo, e confere o resultado de fora (`curl`, navegador).

## 1. Quando usar

| Opção | Serve para |
|---|---|
| **Render (web service Free) + Render Static + Atlas M0** | API com WebSocket (Socket.IO) ou upload, e site no mesmo Blueprint |
| Site no Pages + API no Render | Funciona, mas SPA com rotas exige `base`, `basename` e `404.html` no Pages |
| Funções serverless (Vercel, Netlify) | API sem WebSocket e sem disco |
| VPS | Fora da regra do portfólio (só hospedagem gratuita) |

## 2. Blueprint (`render.yaml`)

Um arquivo na raiz cria a API e o site a partir de pastas do mesmo repositório (`rootDir`).

```yaml
services:
  - type: web
    name: <app>-api
    runtime: node
    plan: free
    rootDir: backend
    buildCommand: npm ci
    startCommand: npm start
    healthCheckPath: /health
    autoDeployTrigger: commit
    envVars:
      - key: NODE_VERSION
        value: "22"
      - key: MONGODB_URI
        sync: false            # o Render pede o valor no painel; nunca no arquivo
      - key: AUTH_SECRET
        generateValue: true    # o Render gera
      - key: CORS_ORIGINS
        value: https://<app>-web.onrender.com
      - key: PUBLIC_URL
        value: https://<app>-api.onrender.com
  - type: web
    name: <app>-web
    runtime: static
    rootDir: frontend
    buildCommand: npm ci && npm run build
    staticPublishPath: dist
    routes:
      - type: rewrite
        source: /*
        destination: /index.html   # F5 numa rota da SPA não dá 404
    envVars:
      - key: VITE_API_URL
        value: https://<app>-api.onrender.com
```

- `sync: false` para tudo o que é segredo. O valor vai só no painel.
- `VITE_API_URL` entra no build: mudar o valor exige novo deploy do site.

## 3. Banco no Atlas M0

1. **Um projeto do Atlas aceita um só cluster M0.** Para vários apps, usar um cluster e **um banco por app**.
2. **Cluster pausado com versão antiga não volta.** Criar um cluster novo.
3. Ao criar o cluster, **desmarcar** "Automate security setup" e "Preload sample dataset". O Quickstart cria usuários com papel Atlas Admin, que não devem ir para uma aplicação.
4. **Database Access → Add New Database User**, um usuário por app:
   - autenticação por senha gerada (só letras e números);
   - **Specific Privileges** → `readWrite` com **Database = nome do banco** e **Collection vazia**. O papel certo aparece como `readWrite@<banco>` (ex.: `readWrite@aircnc`), e não `readWrite@database.<banco>`.
5. **Network Access → Allow Access from Anywhere** (`0.0.0.0/0`). O Render Free não tem IP fixo. A regra só fica **Active** com o cluster ativo.
6. URI com o nome do banco antes do `?`:
   `mongodb+srv://<usuario>:<senha>@<cluster>.<id>.mongodb.net/<banco>?retryWrites=true&w=majority`

### Erros e o que significam

| Mensagem | Causa | O que fazer |
|---|---|---|
| `bad auth` | Senha errada (ou caractere especial sem codificar) | Gerar outra senha, só letras e números, e atualizar `MONGODB_URI` |
| `user is not allowed to do action [find]` | Permissão: o usuário não tem `readWrite` no banco da URI | Conferir o papel (`readWrite@<banco>`) e o nome do banco na URI |
| Tempo esgotado na conexão | Network Access sem `0.0.0.0/0` ativo, ou cluster pausado | Conferir que a regra está Active e o cluster rodando |

## 4. Criar os serviços

1. Render → **New → Blueprint** → escolher o repositório e a branch principal.
2. Preencher os valores com `sync: false` (`MONGODB_URI`).
3. **Apply** e acompanhar os logs da API.

## 5. Conferir o endereço real (passo que mais falha)

O nome `<app>-api.onrender.com` pode já pertencer a **outra conta**. Nesse caso o Render acrescenta um sufixo (ex.: `aircnc-api-45yf.onrender.com`) e nada avisa no Blueprint.

1. Copiar do painel o endereço real de cada serviço.
2. Corrigir no `render.yaml` (por PR): `VITE_API_URL` (site), `PUBLIC_URL` e `CORS_ORIGINS` (API).
3. Novo deploy do site, para o build levar a URL nova.
4. **Testar o JS publicado:** baixar o bundle do site e procurar o endereço da API que ele chama.
   ```bash
   curl -s https://<app>-web.onrender.com/ | grep -o 'assets/[^"]*\.js' | head -1
   curl -s https://<app>-web.onrender.com/assets/<arquivo>.js | grep -o 'https://[a-z0-9-]*\.onrender\.com' | sort -u
   ```
5. Abrir o endereço "esperado" também: se responder, ver de quem é. HTTP 200 não prova que o site é nosso; comparar `title`, `theme-color` e caminhos com o repositório.

## 6. Conferir no ar

1. `GET /health` responde 200. **Mas `/health` que não toca o banco não prova a conexão.**
2. Chamar uma rota que lê o banco (ex.: `GET /spots?tech=x`) e ver a resposta; ou fazer login e cadastrar um item.
3. Abrir o site, fazer o fluxo principal, recarregar uma rota interna (rewrite).
4. DevTools → Network: chamadas e WebSocket vão para a API certa, sem erro de CORS.
5. Registrar no `MVP.md` o comando, a data e o resultado; medir LCP no endereço publicado.

## 7. Limites do plano gratuito

- Disco temporário: uploads somem a cada deploy e quando a API dorme. Imagens persistentes exigem serviço externo (decisão do responsável).
- A API dorme após cerca de 15 min sem acesso e leva cerca de 1 min para acordar.
- As horas gratuitas são da conta inteira; o site estático não consome.
- Serviço acima de 512 MB de memória cai.
- M0: 512 MB de armazenamento, divididos entre os bancos do cluster.

## 8. Segurança

- Nunca versionar `.env`. No README, só o `.env.example`.
- Se uma URI com credencial já foi versionada: o responsável apaga aquele usuário no Atlas (Database Access → Delete). Apagar o arquivo não basta.
- Para quem testar o site publicado: e-mails e imagens fictícios.
