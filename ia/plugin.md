# O engenharia como plugin do Claude Code (estudo e protótipo, 23/11/2026)

Issue: engenharia#54. **Situação:** protótipo numa branch, sem instalação. Instalar na máquina é do responsável (R12).

Documentação oficial consultada em 23/11/2026 (as páginas não mostram data de atualização):
- [Plugin manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference)
- [Plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [Plugins overview](https://code.claude.com/docs/en/plugins)

## Por que um plugin

- O Claude Code só lê o `.claude/` da pasta aberta e o `~/.claude/`. As skills e os agentes do `engenharia` ficam presos ao clone dele.
- As 4 pastas (`community`, `github`, `ia` e `learntech`) abrem fora do clone.
- Um plugin instala igual nas 4 pastas, tem versão e pode ser desligado.
- A junção de pastas da engenharia#16 usava um caminho do Samsung, que não existe no Acer.

## O que o protótipo traz

| Arquivo | O que faz |
|---|---|
| [`.claude-plugin/plugin.json`](../.claude-plugin/plugin.json) | O manifesto. O nome é `engenharia`, as skills são lidas de `./.claude/skills/`, e os agentes são listados um a um |
| [`.claude-plugin/marketplace.json`](../.claude-plugin/marketplace.json) | Um marketplace local com um plugin só, cuja fonte é a raiz do repositório (`"source": "./"`) |

Nada é copiado: o plugin aponta para os mesmos arquivos de `.claude/`, sem duplicar.

## O que entra e o que fica de fora

| Componente | Entra? | Por quê |
|---|---|---|
| As 7 skills de `.claude/skills/` | sim | O campo `skills` aceita uma pasta e soma à busca padrão |
| Os 3 agentes que já estão na sprint (`explorador`, `revisor-de-fatos`, `revisor-independente`) | sim | O campo `agents` aceita **só arquivos `.md`, não pastas**. Cada agente novo precisa de uma linha no manifesto |
| Os 11 agentes da cadeia #50 | depois | Eles entram no manifesto depois do merge da cadeia, num PR pequeno |
| O hook `bloquear_proibidos` | **não, por enquanto** | O hook roda em Python e falha aberto quando o Python não existe (achado 8 do Esp SecOps no engenharia#67). O Acer não tem Python. Um hook que não roda dá falsa segurança |

## Riscos

1. **`"source": "./"` não tem exemplo na documentação.** Os exemplos usam `./plugins/<nome>`. A documentação diz que o plugin pode ficar na raiz do marketplace, mas não mostra esse caso. [A CONFIRMAR] com `claude plugin validate .`, que precisa da CLI do Claude Code. A CLI não está instalada no Acer (`claude` não está no PATH em 23/11/2026).
2. **Pasta oculta.** A documentação exige que os caminhos comecem com `./` e fiquem dentro da raiz. Ela não fala de `.claude/`. Isso entra no mesmo teste do risco 1.
3. **Prefixo nos nomes.** As skills do plugin ganham o prefixo `engenharia:` (por exemplo, `engenharia:issue-no-modelo`). Os textos que chamam uma skill pelo nome curto precisam aceitar os dois nomes.
4. **Agente esquecido.** Como o campo `agents` é uma lista de arquivos, um agente novo sem linha no manifesto não aparece. Mitigação: um teste no CI que compara `.claude/agents/*.md` com o manifesto (passo 4 do plano).
5. **Versão.** Sem o campo `version`, quem instala acompanha os commits. Num marketplace local, o plugin recarrega os arquivos a cada sessão e ignora a versão. Isso é bom para nós: a `main` é a versão.
6. **Duplicata.** Uma sessão aberta dentro do próprio clone do `engenharia` leria o `.claude/` do projeto e também o plugin. As 4 pastas de trabalho não abrem dentro do clone, então o caso é raro.

## Plano

| # | Passo | Quem faz |
|---|---|---|
| 1 | Este protótipo e o estudo | a arquitetura de IA (feito) |
| 2 | Validar com `claude plugin validate .` (riscos 1 e 2) | quem tiver a CLI. Instalar a CLI é do responsável |
| 3 | Depois da cadeia #50, pôr os 11 agentes no manifesto | a arquitetura de IA |
| 4 | Teste no CI: todo `.claude/agents/*.md` está no `plugin.json` | a arquitetura de IA |
| 5 | Instalar nas 4 pastas e testar: uma skill e um agente aparecem numa sessão nova | o responsável (R12) |
| 6 | Pôr o hook no plugin, só depois do Python, das correções do #67 e do ruleset da `main` | a arquitetura de IA, com o ok dele |

## Como instalar (para o responsável, depois do merge na `main`)

Na sessão de qualquer uma das 4 pastas:

```
/plugin marketplace add C:/douglasabnovato-github/engenharia
/plugin install engenharia@engenharia-local
```

- **Atualizar:** `git pull` no clone. Num marketplace local, cada sessão nova já lê os arquivos atuais. Na sessão aberta, `/reload-plugins`.
- **Desligar:** `/plugin`, depois Installed, depois desligar o `engenharia`. Pela CLI, `claude plugin disable engenharia@engenharia-local`.
- **Tirar:** `claude plugin marketplace remove engenharia-local`. Isso também desinstala o plugin.
