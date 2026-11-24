"""Testes do hook: python -m unittest discover -s scripts/hooks"""
import json
import os
import subprocess
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bloquear_proibidos as hook  # noqa: E402
from bloquear_proibidos import motivo  # noqa: E402

BLOQUEADOS = [
    # force push
    "git push --force",
    "git push -f origin feature/2026-11-12",
    "git push --force-with-lease origin feature/x",
    "git push --force-with-lease=feature/x:abc origin feature/x",
    "git push -uf origin feature/x",
    "git push origin +feature/x",
    "git push origin +main",
    # push na principal
    "git push origin main",
    "git push origin master",
    "git push origin HEAD:main",
    "git push origin main:main",
    "git push origin heads/main",
    "git push --set-upstream origin main",
    "git push origin feature/x:refs/heads/master",
    "git push --repo=origin main",
    "git push origin main 2>&1",
    # apagar branch remota
    "git push --delete origin feature/x",
    "git push origin :feature/x",
    "git push --prune origin 'refs/heads/*:refs/heads/*'",
    # hooks desligados
    "git commit --no-verify -m teste",
    "git commit -n -m teste",
    "git commit -nm teste",
    "git push --no-verify",
    "git -c core.hooksPath=/dev/null commit -m x",
    # reescrever histórico
    "git filter-repo --path segredo.env --invert-paths",
    "git-filter-repo --force",
    "git filter-branch --tree-filter 'rm x' HEAD",
    # o comando escondido em outra construção
    "cd repo && git push --force",
    "git -C C:/tmp/repo push --force",
    "git -c x=y push --force",
    "npm test; git push origin main",
    "git status\ngit push --force",
    "cd x\r\ngit push -f",
    "bash -c \"git push --force origin x\"",
    "powershell -Command \"git push --force\"",
    "cmd /c git push --force",
    "(git push --force)",
    "{ git push --force; }",
    "echo $(git push --force)",
    "echo `git push --force`",
    "if true; then git push --force; fi",
    "! git push --force",
    "xargs git push --force",
    "timeout 60 git push --force",
    "env -i git push --force",
    "GIT_TRACE=1 git push --force",
    "git add .; if ($?) { git push --force }",
    "& 'C:\\Program Files\\Git\\cmd\\git.exe' push --force",
    "C:\\Git\\cmd\\git.exe push --force",
]

PERMITIDOS = [
    "git push",
    "git push -u origin feature/2026-11-12",
    "git push -q",
    "git push origin developer/sprint-2026-11-19",
    "git push origin feature/main-menu",
    "git push origin feature/2026-11-12-ia-b",
    "git push -ofoo origin feature/x",
    "git push --follow-tags origin feature/x",
    "git push -u origin feature/x\ngit checkout main",
    "git commit -m \"docs: proibido usar --no-verify\"",
    "git commit -m \"--no-verify\"",
    "git commit -m \"git push --force\"",
    "git commit --amend -m x",
    "git branch -f x",
    "git log --oneline -3",
    "gh pr merge 45 --merge",
    "echo git push --force",
    "git fetch origin main",
    "git checkout main",
    "git merge -n origin/main",
    "npm run build",
    "",
]


class TestHook(unittest.TestCase):
    def setUp(self):
        # sem rede nos testes: todo PR consultado tem base de integração
        self.original = hook.consultar_base
        hook.consultar_base = lambda alvo, repo: "developer/sprint-2026-11-26"

    def tearDown(self):
        hook.consultar_base = self.original

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
        return subprocess.run([sys.executable, script], input=entrada, capture_output=True,
                              text=True, encoding="utf-8")

    def test_saida_json_de_recusa(self):
        r = self.rodar(json.dumps({"tool_name": "Bash", "tool_input": {"command": "git push --force"}}))
        self.assertEqual(r.returncode, 0)
        saida = json.loads(r.stdout)["hookSpecificOutput"]
        self.assertEqual(saida["hookEventName"], "PreToolUse")
        self.assertEqual(saida["permissionDecision"], "deny")
        self.assertIn("Force push", saida["permissionDecisionReason"])

    def test_comando_permitido_sem_saida(self):
        r = self.rodar(json.dumps({"tool_name": "Bash", "tool_input": {"command": "git status"}}))
        self.assertEqual((r.returncode, r.stdout), (0, ""))

    def test_entradas_estranhas_nao_travam(self):
        for entrada in ["isto não é json", "[]", json.dumps({"tool_input": "texto"}),
                        json.dumps({"tool_input": {"command": 5}})]:
            with self.subTest(entrada=entrada):
                r = self.rodar(entrada)
                self.assertEqual((r.returncode, r.stdout), (0, ""))

    def test_aspas_sem_fechar_ainda_confere(self):
        self.assertIsNotNone(motivo("echo 'x; git push -f"))


class TestMergeSoNaIntegracao(unittest.TestCase):
    """gh pr merge só passa com base de integração (P3, [A CONFIRMAR])."""

    def setUp(self):
        self.chamadas = []
        self.bases = {}

        def falsa(alvo, repo):
            self.chamadas.append((alvo, repo))
            return self.bases.get(alvo)
        self.original = hook.consultar_base
        hook.consultar_base = falsa

    def tearDown(self):
        hook.consultar_base = self.original

    def test_base_de_integracao_passa(self):
        self.bases = {"64": "developer/sprint-2026-11-26"}
        self.assertIsNone(motivo("gh pr merge 64 --merge"))
        self.assertEqual(self.chamadas, [("64", None)])

    def test_base_principal_e_recusada(self):
        self.bases = {"318": "main", "9": "master"}
        self.assertIn("principal", motivo("gh pr merge 318 --merge"))
        self.assertIn("principal", motivo("cd x && gh pr merge 9 --squash --delete-branch"))

    def test_sem_conferir_a_base_recusa(self):
        self.assertIn("conferir", motivo("gh pr merge 77 --merge"))

    def test_repo_e_opcoes_com_valor(self):
        self.bases = {"5": "developer"}
        self.assertIsNone(motivo('gh pr merge -R dono/repo --subject "t 9" 5 --merge'))
        self.assertEqual(self.chamadas, [("5", "dono/repo")])

    def test_merge_pela_api_e_recusado(self):
        self.assertIsNotNone(motivo("gh api -X PUT repos/dono/repo/pulls/12/merge"))
        self.assertEqual(self.chamadas, [])

    def test_outros_gh_passam_sem_consultar(self):
        for c in ["gh pr view 3", "gh pr list", "gh api repos/dono/repo/pulls/12", "gh issue merge"]:
            with self.subTest(c=c):
                self.assertIsNone(motivo(c))
        self.assertEqual(self.chamadas, [])


if __name__ == "__main__":
    unittest.main()
