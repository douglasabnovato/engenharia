---
name: ciclo-repositorio
description: Use para fazer uma entrega (uma issue) num repositório do portfólio, do clone à integração, com evidência. Aplica o fluxo Git, os limites e a definição de pronto.
---

# Ciclo de uma entrega num repositório

Base: [`ia/processo-repositorio.md`](../../../ia/processo-repositorio.md), [`processo/fluxo-git.md`](../../../processo/fluxo-git.md) e o tema da pilha em [`ia/aprendizados.md`](../../../ia/aprendizados.md).

1. **Aviso de início:** use a skill `aviso-entre-sessoes`.
2. **Clone temporário:** `git clone -c core.longpaths=true <url>` no scratchpad. Nunca nos clones de uso diário.
3. **Branch:** `feature/AAAA-MM-DD` a partir da integração do repositório (sprint ou `developer*`).
4. **Antes de mudar:** leia a issue e os comentários, o `docs/MVP.md` e o código que vai mudar.
5. **Mudar em commits pequenos:**
   - cada commit leva `Refs #N` e a linha `Co-Authored-By` do agente;
   - faça o push logo depois de cada commit.
6. **Verificar:**
   - lint, testes e build verdes;
   - se houver tela, confira no navegador: console, rede e temas claro e escuro.
7. **Revisão independente:** quando a mudança tiver lógica, chame o agente `revisor-independente` com o diff e a issue.
8. **Integrar:**
   - com a CI verde, faça o `--ff-only` para a integração ou o merge do PR para a sprint, em **uma tentativa**;
   - espere no máximo 4 horas, com `timeout` no `gh run watch`.
9. **Registrar:**
   - a evidência na issue, com a skill `evidencia-atende`;
   - a linha do `docs/MVP.md`;
   - a issue só fecha depois de conferida em produção.
10. **Aviso de fim:** diga o que falta e de quem.

Nunca toque na principal. Nunca use force push nem `--no-verify`. Não mexa em configuração, segredos ou repositório de terceiros.

Se algo for bloqueado, não contorne: registre e siga.
