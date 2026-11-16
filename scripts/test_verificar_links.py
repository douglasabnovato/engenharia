"""Testes do verificar_links.py (engenharia#21)."""
import os
import tempfile
import unittest

from verificar_links import links_quebrados


class TestVerificarLinks(unittest.TestCase):
    def montar(self, arquivos):
        raiz = tempfile.mkdtemp()
        for nome, texto in arquivos.items():
            caminho = os.path.join(raiz, nome)
            os.makedirs(os.path.dirname(caminho), exist_ok=True)
            with open(caminho, "w", encoding="utf-8") as f:
                f.write(texto)
        return raiz

    def test_link_valido_passa(self):
        raiz = self.montar({"a.md": "[b](pasta/b.md)", "pasta/b.md": "[a](../a.md#secao)"})
        self.assertEqual(links_quebrados(raiz), [])

    def test_link_quebrado_aparece(self):
        raiz = self.montar({"a.md": "[x](nao-existe.md)"})
        self.assertEqual(links_quebrados(raiz), [("a.md", "nao-existe.md")])

    def test_externo_ancora_e_bloco_de_codigo_sao_ignorados(self):
        texto = "[s](https://exemplo.org) [t](#topo)\n```\n[c](falso.md)\n```\n"
        raiz = self.montar({"a.md": texto})
        self.assertEqual(links_quebrados(raiz), [])

    def test_pasta_como_destino_vale(self):
        raiz = self.montar({"a.md": "[p](pasta/)", "pasta/b.md": ""})
        self.assertEqual(links_quebrados(raiz), [])


if __name__ == "__main__":
    unittest.main()
