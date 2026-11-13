"""Confere os links internos dos arquivos Markdown do repositório (engenharia#21).

Uso: python scripts/verificar_links.py [pasta]
Sai com código 1 se algum link relativo apontar para um arquivo que não existe.
Links externos (http, https, mailto) e âncoras puras (#secao) não são conferidos.
"""
import os
import re
import sys

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
IGNORAR_PASTAS = {".git", "node_modules"}
EXTERNO = ("http://", "https://", "mailto:")


def links_quebrados(raiz):
    """Devolve a lista de (arquivo, link) cujo destino não existe."""
    quebrados = []
    for pasta, subpastas, arquivos in os.walk(raiz):
        subpastas[:] = [p for p in subpastas if p not in IGNORAR_PASTAS]
        for nome in arquivos:
            if not nome.endswith(".md"):
                continue
            caminho = os.path.join(pasta, nome)
            with open(caminho, encoding="utf-8") as f:
                texto = f.read()
            # Blocos de código não têm links de verdade.
            texto = re.sub(r"```.*?```", "", texto, flags=re.S)
            for alvo in LINK.findall(texto):
                if alvo.startswith(EXTERNO) or alvo.startswith("#"):
                    continue
                arquivo_alvo = alvo.split("#", 1)[0]
                destino = os.path.normpath(os.path.join(pasta, arquivo_alvo))
                if not os.path.exists(destino):
                    quebrados.append((os.path.relpath(caminho, raiz), alvo))
    return quebrados


def main(argv):
    raiz = argv[1] if len(argv) > 1 else "."
    quebrados = links_quebrados(raiz)
    for arquivo, alvo in quebrados:
        print(f"QUEBRADO {arquivo}: {alvo}")
    print(f"Links internos quebrados: {len(quebrados)}")
    return 1 if quebrados else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
