# Hooks de proteção

As proibições da regra 6 do `CLAUDE.md` (force push, reescrever histórico, `--no-verify`) e a regra "nada na principal sem o responsável" hoje são texto. Em 09/11/2026, um agente usou `--force-with-lease` por engano ([decisão de 09/11](../decisoes/2026-11-09-ciclo.md)). Um hook do Claude Code recusa o comando antes de ele rodar, sem depender da memória do agente.

Escrever o script é do Claude (issue #13). Ligar o hook na máquina é configuração do responsável (issue #17).

## O que o hook bloqueia

Script: [`scripts/hooks/bloquear_proibidos.py`](../scripts/hooks/bloquear_proibidos.py). Evento `PreToolUse`, ferramentas `Bash` e `PowerShell`.

| Bloqueia | Exemplos | Regra |
|---|---|---|
| Force push | `git push --force`, `-f`, `-uf`, `--force-with-lease`, refspec `+feature/x` | `CLAUDE.md`, regra 6 |
| Hooks do repositório desligados | `--no-verify`, `git commit -n`, `git -c core.hooksPath=... commit` | `CLAUDE.md`, regra 6 |
| Push direto na principal | `git push origin main`, `HEAD:master`, `heads/main`, `x:refs/heads/main`, `--repo=origin main` | `CLAUDE.md`, regras 3 e 4 |
| Apagar branch remota | `git push --delete origin x`, `git push origin :x`, `git push --prune` | [`como-trabalhamos.md`](como-trabalhamos.md) |
| Reescrever histórico | `git filter-repo`, `git-filter-repo`, `git filter-branch` | [`padroes.md`](../arquitetura/padroes.md), seção 4 |

Como ele lê o comando:
- Respeita as aspas. Por isso `git commit -m "proibido --no-verify"` e `echo git push --force` passam: são texto, não comando.
- Separa as partes por `;`, `&&`, `||`, `|`, `&` e quebra de linha, e confere cada uma.
- Pula o que vem antes do comando de verdade: `VAR=1`, `env`, `sudo`, `timeout 60`, `xargs`, `if`, `then`, `(`, `{`, `!` e o `if ($?) {` do PowerShell.
- Confere de novo o texto passado a `bash -c`, `sh -c`, `powershell -Command` e `cmd /c`, e o que está dentro de `$( )` e de crases.
- Aceita o caminho completo do `git.exe`, com ou sem aspas.

Quando recusa, o hook devolve `permissionDecision: deny` com o motivo, e o agente vê a mensagem. Por exemplo: "Bloqueado pelo hook do portfólio: Push direto na principal é proibido: use PR (CLAUDE.md, regras 3 e 4)."

## O que ele não cobre

- `git push` sem destino enquanto a branch atual é a principal. Quem cobre é o ruleset `principal-protegida`.
- Ações pela API do GitHub (`gh api -X DELETE ...`). Quem cobre é o classificador de permissões e o ruleset.
- Comandos montados dentro de scripts (`python x.py` que chama `git`), aliases do git e variáveis que guardam o comando (`$c = "push"; git $c --force`). O hook só vê a linha de comando.

Por isso o hook soma às outras camadas, não substitui: texto, classificador, hook e ruleset.

## Testes

```bash
python -m unittest discover -s scripts/hooks -v
```

São 6 testes:
- 49 comandos que devem ser bloqueados, inclusive as burlas achadas pela revisão independente (quebra de linha, `bash -c`, `commit -n`, `--prune`);
- 22 comandos que devem passar;
- a saída JSON de recusa;
- entradas estranhas que não podem travar a sessão;
- aspas sem fechar.

## Como ligar (responsável, issue #17)

1. Depois do merge desta sprint na `main`, atualize o clone de uso diário: `git -C C:/douglasabnovato-github/engenharia pull`. O script só existe ali depois disso.
2. No `~/.claude/settings.json`, para valer em toda sessão, em qualquer pasta, acrescente ao objeto que já existe:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash|PowerShell",
        "hooks": [
          {
            "type": "command",
            "command": "python C:/douglasabnovato-github/engenharia/scripts/hooks/bloquear_proibidos.py",
            "onFailure": "block"
          }
        ]
      }
    ]
  }
}
```

O `"onFailure": "block"` faz o comando parar se o hook não rodar (por exemplo, `python` fora do `PATH` ou o caminho errado). Sem ele, a proteção some sem aviso. O campo exige o Claude Code 2.1.295 ou mais novo.

3. Para conferir, abra uma sessão nova e peça `git status`. Se aparecer o aviso `hook error`, o caminho ou o `python` está errado. Depois, peça `git push --force` num clone de teste: o comando deve ser recusado com a mensagem do hook.

A lista `permissions.deny` da issue #17 pode ficar junto: ela bloqueia por padrão de texto, e o hook pega as variações (`-uf`, `+refspec`, `HEAD:main`, `bash -c`).

Referência: [Claude Code Docs, hooks](https://code.claude.com/docs/en/hooks) (campos `matcher`, `permissionDecision` e `onFailure`).
