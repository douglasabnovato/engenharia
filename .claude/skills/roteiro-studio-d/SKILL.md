---
name: roteiro-studio-d
description: Use para escrever ou revisar um roteiro de vídeo do Studio D a partir de um repositório do portfólio, do estudo do repositório ao PR na sprint com a revisão de fatos.
---

# Roteiro do Studio D

Base: `docs/como-escrever-um-roteiro.md` do repositório `douglasabnovato/studio-d` (passos, "Do repositório ao roteiro" e "Regras de fato"). Leia esse guia inteiro antes; esta skill só dá a ordem.

1. **Issues:** confira a issue do roteiro no Studio D e a issue "Pronto para o vídeo N" no repositório de origem (rótulo `roteiro`). Se faltar uma, abra no modelo (skill `issue-no-modelo`).
2. **Clone temporário** do Studio D e do repositório de origem (skill `ciclo-repositorio`, passos de clone e branch).
3. **Estudar a origem:** README, `docs/MVP.md`, plano, testes, PRs mesclados e issues abertas. Ache um antes e depois real (commit ou PR) e uma issue aberta para a "Melhoria".
4. **Escrever** a partir de `roteiros/_modelo.md`: blocos `## Nome · m:ss–m:ss`, contínuos, com `### Fala`, `### Tela` e `### Comandos`; capítulos iguais aos inícios. Toda afirmação com fonte `https` no frontmatter. Texto com `: ` no frontmatter vai entre aspas.
5. **Na Tela, nada pessoal nem segredo:** nada de `git show` ou `git log` que mostre e-mail de autor; não abrir diff de commit que mostre credencial; não mostrar dono de site de terceiro.
6. **Validar:** `npx vitest run` e `npm run build`. Tire o episódio de `planejados` no `roteiros/series.yml`.
7. **Revisão de fatos:** delegue ao agente `revisor-de-fatos` com o caminho do roteiro e das fontes, sem a sua conclusão. Trate cada achado e liste no PR.
8. **PR para a sprint**, com CI verde e uma tentativa de merge. Comente a evidência nas duas issues e no PR sprint → principal.
9. **Aviso de fim:** skill `aviso-entre-sessoes`.
