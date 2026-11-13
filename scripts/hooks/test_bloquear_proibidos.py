"""Testes do hook: python -m unittest discover -s scripts/hooks"""
import io
import json
import os
import subprocess
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bloquear_proibidos import motivo  # noqa: E402

BLOQUEADOS = [
    "git push --force",
    "git push -f origin feature/2026-11-12",
    "git push --force-with-lease origin feature/x",
    "git push --force-with-lease=feature/x:abc origin feature/x",
    "git push -uf origin feature/x",
    "git push origin +feature/x",
    "git push origin main",
    "git push origin master",
    "git push origin HEAD:main",
    "git push origin feature/x:refs/heads/master",
    "git push --delete origin feature/x",
    "git push origin :feature/x",
    "git commit --no-verify -m teste",
    "git push --no-verify",
    "cd repo && git push --force",
    "git -C C:/tmp/repo push --force",
    "npm test; git push origin main",
    "git filter-repo --path segredo.env --invert-paths",
    "git filter-branch --tree-filter 'rm x' HEAD",
    "& 'C:\\Program Files\\Git\\cmd\\git.exe' push --force",
    "GIT_TRACE=1 git push --force",
    "env git push origin main",
]

PERMITIDOS = [
    "git push",
    "git push -u origin feature/2026-11-12",
    "git push -q",
    "git push origin developer/sprint-2026-11-19",
    "git push origin feature/main-menu",
    "git commit -m \"docs: proibido usar --no-verify\"",
    "git log --oneline -3",
    "gh pr merge 45 --merge",
    "echo git push --force",
    "git fetch origin main",
    "git checkout main",
    "npm run build",
    "",
]


class TestHook(unittest.TestCase):
    def test_bloqueados(self):
        for c in BLOQUEADOS:
            with self.subTest(c=c):
                self.assertIsNotNone(motivo(c), c)

    def test_permitidos(self):
        for c in PERMITIDOS:
            with self.subTest(c=c):
                self.assertIsNone(motivo(c), c)

    def rodar(self, entrada):
        script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bloquear_proibidos.py")
        r = subprocess.run([sys.executable, script], input=entrada, capture_output=True,
                           text=True, encoding="utf-8")
        return r

    def test_saida_json_de_recusa(self):
        r = self.rodar(json.dumps({"tool_name": "Bash", "tool_input": {"command": "git push --force"}}))
        self.assertEqual(r.returncode, 0)
        saida = json.loads(r.stdout)["hookSpecificOutput"]
        self.assertEqual(saida["permissionDecision"], "deny")
        self.assertIn("Force push", saida["permissionDecisionReason"])

    def test_comando_permitido_sem_saida(self):
        r = self.rodar(json.dumps({"tool_name": "Bash", "tool_input": {"command": "git status"}}))
        self.assertEqual((r.returncode, r.stdout), (0, ""))

    def test_entrada_invalida_nao_trava(self):
        r = self.rodar("isto não é json")
        self.assertEqual((r.returncode, r.stdout), (0, ""))


if __name__ == "__main__":
    unittest.main()
