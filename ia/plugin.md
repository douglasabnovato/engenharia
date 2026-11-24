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
| O hook `bloquear_proibidos` | **não, por enquanto** | No Acer, `python` é só o atalho da Microsoft Store e não roda. Sem Python, o hook ou some sem aviso (falha aberta, achado 8 do Esp SecOps no engenharia#67), ou trava todo comando (`onFailure: block`, de `ia/hooks.md`; o campo está [A CONFIRMAR] na documentação). Ele entra no plugin só depois do Python e do teste do `ia/hooks.md` |

## Riscos

1. **`"source": "./"` sem exemplo na documentação: resolvido.** O `claude plugin validate` (Claude Code 2.1.330, a CLI que vem com o app) rodou sem erro em 23/11/2026, conferido pelo Esp ES. Saída 0, com 7 skills e 3 agentes.
2. **Pasta oculta `.claude/`: resolvido.** No mesmo `validate`, os caminhos dentro de `.claude/` foram aceitos.
3. **Prefixo nos nomes (confirmado pelo `validate`).** As skills e os agentes do plugin ganham o prefixo `engenharia:` (por exemplo, `engenharia:issue-no-modelo`). Os textos que chamam uma skill pelo nome curto precisam aceitar os dois nomes.
4. **Agente esquecido.** Como o campo `agents` é uma lista de arquivos, um agente novo sem linha no manifesto não aparece. Mitigação: um teste no CI que compara `.claude/agents/*.md` com o manifesto (passo 4 do plano).
5. **Versão.** Sem o campo `version`, quem instala acompanha os commits. Num marketplace local, o plugin recarrega os arquivos a cada sessão e ignora a versão. Isso é bom para nós: a `main` é a versão.
6. **Duplicata.** No Acer, a pasta `ia` (`C:/douglasabnovato-ia`) é a pasta-mãe do clone, e as sessões da arquitetura de IA e dos Esp trabalham ali. [A CONFIRMAR] se o Claude Code descobre o `.claude/skills/` de uma subpasta lida na sessão. Se descobrir, a skill aparece duas vezes: com o nome curto e com `engenharia:`. O teste do passo 5 começa pela pasta `ia`, e o resultado é anotado aqui.

## Plano

| # | Passo | Quem faz |
|---|---|---|
| 1 | Este protótipo e o estudo | a arquitetura de IA (feito) |
| 2 | Validar com `claude plugin validate .` (riscos 1 e 2) | feito em 23/11/2026 pelo Esp ES: sem erro, com 7 skills e 3 agentes |
| 3 | Depois da cadeia #50, pôr os 11 agentes no manifesto | a arquitetura de IA |
| 4 | Teste no CI: todo `.claude/agents/*.md` está no `plugin.json` | a arquitetura de IA |
| 5 | Instalar **uma vez, no escopo `user`** (vale para as 4 pastas), e testar nas 4, começando pela `ia` (risco 6): uma skill e um agente aparecem numa sessão nova | o responsável (R12) |
| 6 | Pôr o hook no plugin, só depois do Python, das correções do #67 e do ruleset da `main` | a arquitetura de IA, com o ok dele |

## Como instalar (para o responsável, depois do merge na `main`)

Uma vez só, no escopo `user`. O escopo `project` criaria um `.claude/settings.json` em cada pasta, e isso é configuração (R12). Troque `<pasta do clone>` pelo caminho do clone na máquina:
- **Acer:** `C:/douglasabnovato-ia/engenharia` (conferido em 23/11/2026);
- **Samsung:** o caminho do clone de lá [A CONFIRMAR].

```
claude plugin marketplace add <pasta do clone>
claude plugin install engenharia@engenharia-local --scope user
```

- **Atualizar:** `git pull` no clone. Num marketplace local, cada sessão nova já lê os arquivos atuais. Na sessão aberta, `/reload-plugins`.
- **Desligar:** `/plugin`, depois Installed, depois desligar o `engenharia`. Pela CLI, `claude plugin disable engenharia@engenharia-local`.
- **Tirar**, nesta ordem:
  1. `claude plugin uninstall engenharia@engenharia-local --scope user`
  2. `claude plugin marketplace remove engenharia-local`
  3. `claude plugin list`, que não deve mostrar mais o `engenharia`.

  Nada disso apaga arquivo do repositório, porque o marketplace local só aponta para o clone. Se o `marketplace remove` também desinstala sozinho, isso fica [A CONFIRMAR]: o `--help` não diz.
