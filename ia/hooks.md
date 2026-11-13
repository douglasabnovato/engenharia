# Hooks de proteção

As proibições da regra 6 do `CLAUDE.md` (force push, reescrever histórico, `--no-verify`) e a regra "nada na principal sem o responsável" hoje são texto. Em 09/11/2026, um agente usou `--force-with-lease` por engano ([decisão de 09/11](../decisoes/2026-11-09-ciclo.md)). Um hook do Claude Code recusa o comando antes de ele rodar, sem depender da memória do agente.

Escrever o script é do Claude (issue #13). Ligar o hook na máquina é configuração do responsável (issue #17).

## O que o hook bloqueia

Script: [`scripts/hooks/bloquear_proibidos.py`](../scripts/hooks/bloquear_proibidos.py). Evento `PreToolUse`, ferramentas `Bash` e `PowerShell`.

| Bloqueia | Exemplos | Regra |
|---|---|---|
| Force push | `git push --force`, `-f`, `-uf`, `--force-with-lease`, refspec `+feature/x` | `CLAUDE.md`, regra 6 |
| `--no-verify` | `git commit --no-verify`, `git push --no-verify` | `CLAUDE.md`, regra 6 |
| Push direto na principal | `git push origin main`, `HEAD:master`, `x:refs/heads/main` | `CLAUDE.md`, regras 3 e 4 |
| Apagar branch remota | `git push --delete origin x`, `git push origin :x` | [`como-trabalhamos.md`](como-trabalhamos.md) |
| Reescrever histórico | `git filter-repo`, `git filter-branch` | [`padroes.md`](../arquitetura/padroes.md), seção 4 |

O hook lê o comando como o shell lê, com aspas. Por isso `git commit -m "proibido --no-verify"` passa, porque é texto de mensagem, e `echo git push --force` também passa. Ele confere cada parte de `a && b; c` e aceita prefixos como `VAR=1`, `env` e o caminho completo do `git.exe`.

Quando recusa, o hook devolve `permissionDecision: deny` com o motivo, e o agente vê a mensagem. Por exemplo: "Bloqueado pelo hook do portfólio: Push direto na principal é proibido: use PR (CLAUDE.md, regras 3 e 4)."

## O que ele não cobre

- `git push` sem destino enquanto a branch atual é a principal. Quem cobre é o ruleset `principal-protegida`.
- Ações pela API do GitHub (`gh api -X DELETE ...`). Quem cobre é o classificador de permissões e o ruleset.
- Comandos montados dentro de scripts (`python x.py` que chama `git`). O hook só vê a linha de comando.

Por isso o hook soma às outras camadas, não substitui: texto, classificador, hook e ruleset.

## Testes

```bash
python -m unittest discover -s scripts/hooks -v
```

O teste roda 22 comandos que devem ser bloqueados e 13 que devem passar. Ele confere também a saída JSON de recusa e que uma entrada inválida não trava a sessão.

## Como ligar (responsável, issue #17)

No `~/.claude/settings.json`, para valer em toda sessão, em qualquer pasta. Acrescente ao objeto que já existe:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash|PowerShell",
        "hooks": [
          {
            "type": "command",
            "command": "python C:/douglasabnovato-github/engenharia/scripts/hooks/bloquear_proibidos.py"
          }
        ]
      }
    ]
  }
}
```

Para conferir, abra uma sessão nova e peça `git push --force` num clone de teste. O comando deve ser recusado com a mensagem do hook.

A lista `permissions.deny` da issue #17 pode ficar junto: ela bloqueia por padrão de texto, e o hook pega as variações (`-uf`, `+refspec`, `HEAD:main`).

Referência: [Claude Code Docs, hooks](https://code.claude.com/docs/en/hooks).
