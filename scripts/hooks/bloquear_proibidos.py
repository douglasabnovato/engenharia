"""Hook PreToolUse do Claude Code: recusa os comandos que o processo proíbe.

Lê o JSON do hook na entrada padrão e, se o comando for proibido, devolve
`permissionDecision: deny` com o motivo. Qualquer outro comando passa sem saída.

Regras (CLAUDE.md, regra 6, e processo/fluxo-git.md):
- force push, inclusive --force-with-lease e refspec com "+";
- --no-verify (e `git commit -n`), ou desligar os hooks com core.hooksPath;
- push direto para main ou master;
- apagar branch remota (push --delete, --prune ou refspec ":branch");
- reescrever histórico (git filter-repo e git filter-branch).

É uma camada a mais, não a única: ver ia/hooks.md, "O que ele não cobre".
"""
import json
import re
import shlex
import sys

PRINCIPAIS = {"main", "master"}
SEPARADORES = {";", "&&", "||", "|", "&", "\n", ";;", "|&"}
# palavras que podem vir antes do comando de verdade, na mesma parte
PREFIXOS = {"env", "sudo", "time", "command", "nohup", "exec", "xargs", "timeout", "nice",
            "if", "then", "else", "elif", "do", "while", "until", "!", "{", "}", "(", ")"}
# shells que recebem o comando como texto: o texto é conferido de novo
SHELLS = {"bash", "sh", "zsh", "dash", "powershell", "pwsh", "cmd"}
OPCOES_SHELL = {"-c", "-command", "/c", "/k", "-lc", "-ic"}
# opções do git commit que levam um valor (o valor não é opção)
COM_VALOR_COMMIT = {"-m", "--message", "-F", "--file", "-C", "-c", "--reuse-message",
                    "--reedit-message", "-t", "--template", "--author", "--date",
                    "--fixup", "--squash", "--trailer", "--cleanup"}
# opções curtas do git push que levam um valor colado (ex.: -ofoo)
CURTAS_COM_VALOR_PUSH = {"o"}


def nome_do_comando(token):
    token = token.lstrip("({!`$").rstrip(")};`")
    nome = token.replace("\\", "/").rsplit("/", 1)[-1].lower()
    return nome[:-4] if nome.endswith(".exe") else nome


def comandos(texto):
    """Quebra a linha em comandos simples, respeitando aspas. A quebra de linha separa."""
    lexer = shlex.shlex(texto, posix=True, punctuation_chars=";&|\n")
    lexer.whitespace = " \t\r"
    lexer.whitespace_split = True
    lexer.commenters = ""
    atual = []
    try:
        for token in lexer:
            if token in SEPARADORES or set(token) <= set(";&|\n"):
                if atual:
                    yield atual
                atual = []
            else:
                atual.append(token)
    except ValueError:
        # aspas sem fechar: confere cada linha pela divisão simples
        atual = []
        for linha in re.split(r"[;&|\n]+", texto):
            if linha.split():
                yield linha.split()
        return
    if atual:
        yield atual


def destino(refspec):
    alvo = refspec.lstrip("+").split(":")[-1]
    for prefixo in ("refs/heads/", "heads/"):
        if alvo.startswith(prefixo):
            alvo = alvo[len(prefixo):]
    return alvo


def motivo_commit(resto):
    i = 0
    while i < len(resto):
        a = resto[i]
        if a == "--":
            break
        if a in COM_VALOR_COMMIT:
            i += 2
            continue
        if a == "--no-verify":
            return "--no-verify é proibido: os hooks do repositório precisam rodar (CLAUDE.md, regra 6)."
        if a.startswith("-") and not a.startswith("--"):
            curtas = a[1:]
            for j, c in enumerate(curtas):
                if c == "n":
                    return "git commit -n é o mesmo que --no-verify, proibido (CLAUDE.md, regra 6)."
                if c in "mFCct":  # o resto do token é o valor
                    break
        i += 1
    return None


def motivo_push(resto):
    for a in resto:
        if a == "--no-verify":
            return "--no-verify é proibido: os hooks do repositório precisam rodar (CLAUDE.md, regra 6)."
        if a in ("--force", "--force-if-includes", "--mirror") or a.startswith("--force-with-lease"):
            return "Force push é proibido, inclusive --force-with-lease (CLAUDE.md, regra 6)."
        if a in ("-d", "--delete", "--prune"):
            return "Apagar branch remota fica com o responsável (ia/como-trabalhamos.md)."
        if a.startswith("-") and not a.startswith("--"):
            for c in a[1:]:
                if c in CURTAS_COM_VALOR_PUSH:
                    break
                if c == "f":
                    return "Force push é proibido (opção -f)."
                if c == "d":
                    return "Apagar branch remota fica com o responsável (opção -d)."
    remoto_por_opcao = any(a.startswith("--repo=") for a in resto)
    posicionais = [a for a in resto if not a.startswith("-")]
    refspecs = posicionais if remoto_por_opcao else posicionais[1:]
    for refspec in refspecs:
        if refspec.startswith("+"):
            return "Refspec com \"+\" é force push, proibido (CLAUDE.md, regra 6)."
        if refspec.startswith(":"):
            return "Refspec \":branch\" apaga a branch remota; fica com o responsável."
        if destino(refspec) in PRINCIPAIS:
            return "Push direto na principal é proibido: use PR (CLAUDE.md, regras 3 e 4)."
    return None


def motivo_git(args):
    """args: o que vem depois de "git", com as opções globais."""
    i = 0
    while i < len(args) and args[i].startswith("-"):
        opcao = args[i]
        valor = args[i + 1] if opcao in ("-c", "-C", "--git-dir", "--work-tree") and i + 1 < len(args) else ""
        if opcao == "-c" and valor.lower().startswith("core.hookspath"):
            return "Desligar os hooks com core.hooksPath é o mesmo que --no-verify, proibido."
        if opcao.lower().startswith("--config-env") and "hookspath" in opcao.lower():
            return "Desligar os hooks com core.hooksPath é o mesmo que --no-verify, proibido."
        i += 2 if valor or opcao in ("-c", "-C", "--git-dir", "--work-tree") else 1
    if i >= len(args):
        return None
    sub, resto = args[i], args[i + 1:]
    if sub in ("filter-repo", "filter-branch"):
        return "Reescrever histórico é decisão e ação do responsável (padroes.md, seção 4)."
    if sub == "commit":
        return motivo_commit(resto)
    if sub == "push":
        return motivo_push(resto)
    if "--no-verify" in resto and sub in ("merge", "rebase", "am", "cherry-pick", "revert"):
        return "--no-verify é proibido: os hooks do repositório precisam rodar (CLAUDE.md, regra 6)."
    return None


def motivo_partes(partes, profundidade):
    i = 0
    while i < len(partes):
        t = partes[i]
        n = nome_do_comando(t)
        if n in PREFIXOS or t in PREFIXOS or t.startswith("-") or re.fullmatch(r"[\w.]+=.*", t) \
                or re.fullmatch(r"\d+[smhd]?", t) or re.fullmatch(r"\(.*\)", t) or t in ("", "{", "}"):
            i += 1
            continue
        break
    if i >= len(partes):
        return None
    n = nome_do_comando(partes[i])
    if n in ("git-filter-repo", "git-filter-branch"):
        return "Reescrever histórico é decisão e ação do responsável (padroes.md, seção 4)."
    if n == "git":
        return motivo_git([p.rstrip(")};`") for p in partes[i + 1:]])
    if n in SHELLS and profundidade < 3:
        for j in range(i + 1, len(partes)):
            if partes[j].lower() in OPCOES_SHELL:
                return motivo(" ".join(partes[j + 1:]), profundidade + 1)
    return None


def motivo(comando, profundidade=0):
    if not comando:
        return None
    # caminhos do Windows sem aspas: confere também com "/" no lugar de "\"
    textos = [comando] + ([comando.replace("\\", "/")] if "\\" in comando else [])
    # o que está dentro de $( ) e de crases também roda
    for texto in list(textos):
        textos += re.findall(r"\$\(([^()]*)\)", texto) + re.findall(r"`([^`]*)`", texto)
    for texto in textos:
        for partes in comandos(texto):
            m = motivo_partes(partes, profundidade)
            if m:
                return m
    return None


def main():
    try:
        entrada = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    tool_input = entrada.get("tool_input") if isinstance(entrada, dict) else None
    comando = tool_input.get("command") if isinstance(tool_input, dict) else None
    m = motivo(comando if isinstance(comando, str) else "")
    if m:
        json.dump({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": "Bloqueado pelo hook do portfólio: " + m,
        }}, sys.stdout)  # ASCII com escapes: não depende da página de código do Windows
    return 0


if __name__ == "__main__":
    sys.exit(main())
