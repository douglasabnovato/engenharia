"""Hook PreToolUse do Claude Code: recusa os comandos que o processo proíbe.

Lê o JSON do hook na entrada padrão e, se o comando for proibido, devolve
`permissionDecision: deny` com o motivo. Qualquer outro comando passa sem saída.

Regras (CLAUDE.md, regra 6, e processo/fluxo-git.md):
- force push, inclusive --force-with-lease e refspec com "+";
- --no-verify em qualquer comando git;
- push direto para main ou master;
- apagar branch remota (push --delete ou refspec ":branch");
- reescrever histórico (git filter-repo e git filter-branch).

Uso em .claude/settings.json: ver ia/hooks.md.
"""
import json
import shlex
import sys

PRINCIPAIS = {"main", "master"}
SEPARADORES = {";", "&&", "||", "|", "&", "\n"}
PREFIXOS = {"env", "sudo", "time", "command", "nohup"}


def comandos(texto):
    """Quebra a linha em comandos simples, respeitando aspas."""
    lexer = shlex.shlex(texto, posix=True, punctuation_chars=";&|")
    lexer.whitespace_split = True
    lexer.commenters = ""
    atual = []
    try:
        for token in lexer:
            if token in SEPARADORES:
                if atual:
                    yield atual
                atual = []
            else:
                atual.append(token)
    except ValueError:
        # aspas sem fechar: cai para a divisão simples, sem perder a checagem
        atual = texto.split()
    if atual:
        yield atual


def destino(refspec):
    alvo = refspec.lstrip("+").split(":")[-1]
    if alvo.startswith("refs/heads/"):
        alvo = alvo[len("refs/heads/"):]
    return alvo


def motivo_git(args):
    """args: o que vem depois de "git" (sem as opções globais como -C <dir>)."""
    if "--no-verify" in args:
        return "--no-verify é proibido: os hooks do repositório precisam rodar (CLAUDE.md, regra 6)."
    if not args:
        return None
    sub, resto = args[0], args[1:]
    if sub in ("filter-repo", "filter-branch"):
        return "Reescrever histórico é decisão e ação do responsável (padroes.md, seção 4)."
    if sub != "push":
        return None
    for a in resto:
        if a in ("-f", "--force", "--force-if-includes", "--mirror") or a.startswith("--force-with-lease"):
            return "Force push é proibido, inclusive --force-with-lease (CLAUDE.md, regra 6)."
        if a.startswith("-") and not a.startswith("--") and "f" in a[1:]:
            return "Force push é proibido (opção -f combinada)."
        if a in ("-d", "--delete"):
            return "Apagar branch remota fica com o responsável (ia/como-trabalhamos.md)."
    posicionais = [a for a in resto if not a.startswith("-")]
    for refspec in posicionais[1:]:  # o primeiro é o remoto
        if refspec.startswith("+"):
            return "Refspec com \"+\" é force push, proibido (CLAUDE.md, regra 6)."
        if refspec.startswith(":"):
            return "Refspec \":branch\" apaga a branch remota; fica com o responsável."
        if destino(refspec) in PRINCIPAIS:
            return "Push direto na principal é proibido: use PR (CLAUDE.md, regras 3 e 4)."
    return None


def sem_opcoes_globais(args):
    """Tira opções globais do git que vêm antes do subcomando: -C <dir>, -c <k=v>."""
    i = 0
    while i < len(args) and args[i].startswith("-"):
        i += 2 if args[i] in ("-C", "-c", "--git-dir", "--work-tree") else 1
    return args[i:]


def motivo(comando):
    for partes in comandos(comando):
        i = 0
        # pula prefixos que só preparam a execução: VAR=valor, env, sudo, time, command
        while i < len(partes) and (partes[i] in PREFIXOS or
                                   ("=" in partes[i] and not partes[i].startswith("-"))):
            i += 1
        if i >= len(partes):
            continue
        nome = partes[i].replace("\\", "/").rsplit("/", 1)[-1].lower()
        if nome in ("git", "git.exe"):
            m = motivo_git(sem_opcoes_globais(partes[i + 1:]))
            if m:
                return m
    return None


def main():
    try:
        entrada = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    comando = (entrada.get("tool_input") or {}).get("command") or ""
    m = motivo(comando)
    if m:
        json.dump({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": "Bloqueado pelo hook do portfólio: " + m,
        }}, sys.stdout)  # ASCII com escapes: não depende da página de código do Windows
    return 0


if __name__ == "__main__":
    sys.exit(main())
