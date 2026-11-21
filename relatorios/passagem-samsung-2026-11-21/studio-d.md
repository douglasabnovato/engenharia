# Passagem Samsung → Acer · Roteiros do Studio D e catálogo do formacao-dev · 21/11/2026

Sessão "Roteiro 13 e roteiros dos vídeos 6 a 9 no Studio D", aberta no Samsung como filha da DG github (hoje aparece como "DG community"). Estado conferido em 21/11 com `gh` e `curl`.

## 1. Papel

1. Abre em `C:\douglasabnovato-github`. Recebeu da DG github, por handoff, duas tarefas pontuais.
2. Não é dona de repositório. Escreveu no studio-d (roteiros), no formacao-dev (issues do catálogo, sem código) e no engenharia (só comentários em engenharia#5 a #8).
3. Faz: roteiros de vídeo com revisão de fatos; relatório e cobertura do catálogo do formacao-dev frente ao roadmap.sh.
4. Não faz: código de app, merge na principal, configuração, atividade em repositório de terceiros.

## 2. Estado por repositório

| Repositório | Nível | MVP | Finalizado | No ar | CI da principal |
|---|---|---|---|---|---|
| studio-d | N2 | 10 de 12 (5 e 10 dependem do responsável) | sim | https://douglasabnovato.github.io/studio-d/ (200 em 21/11) | verde em 19/11 |
| formacao-dev | N1 | 8 de 10 | não | Pages desligado | Disponibilidade verde em 21/11 |

## 3. Em andamento

5. Nada desta sessão está aberto. studio-d#50 (roteiro 13) e studio-d#51 (roteiros 6 a 9) entraram na sprint-19, e studio-d#27 levou essa sprint para a principal em 16/11.
6. PRs abertos de outras sessões, depois de 16/11: studio-d#73 e formacao-dev#317 (feature/2026-11-20 → developer/sprint-2026-11-26).
7. Nada sem commit. Os clones temporários estão limpos e podem ser descartados.

## 4. Decisões do responsável

8. 15/11: "Sim, siga". Roteiro 13 (Painel de Formação) e roteiros dos vídeos 6 a 9 (studio-d).
9. 15/11: "Sim, feche". Fechar com evidência as 64 issues de itens já feitos (formacao-dev). Feito.
10. 16/11: "faça". Publicar 16 issues "Novo item" (formacao-dev#285 a #300) e os comentários de cobertura em formacao-dev#4, #11 e #14. Feito.

## 5. Com o responsável

11. formacao-dev: 7 Dependabot de versão maior abertos.
12. formacao-dev#38: proteger a principal (destrava o critério 10).
13. formacao-dev#230: publicar a API e ligar o login com o GitHub.
14. formacao-dev#246: aviso privado de falhas e varredura de segredos.
15. formacao-dev#271: conferir a decisão de dados pessoais.
16. formacao-dev#206: apagar as branches mescladas.
17. formacao-dev#35: Public Sponsor. Tem custo; sugestão: arquivar.
18. formacao-dev: ligar o Pages e criar a variável `PAGES_ATIVO` (painel no ar, primeira barreira à ativação).
19. formacao-dev#194 a #201: destino dos 77 PRs em 7 repositórios de terceiros, de 10/11. Em 16/11 o responsável disse "os de terceiros, pode ficar lá".
20. formacao-dev: decidir se T11.1, T11.2 e T8.4 contam o PR aberto ou só o mesclado pelo dono.
21. engenharia#5 a #8: evidências comentadas; fechar depois do merge do engenharia na principal.

## 6. Aprendizados novos

22. Depois do merge da sprint na principal, fechar no mesmo ciclo as issues dos itens que entraram, com evidência; senão elas escondem as abertas de verdade. (formacao-dev, 15/11/2026: eram 64 de 171)
23. Antes de pôr na tela um aviso de "tem dado pessoal", conferir com `grep` se o arquivo tem mesmo o dado. (engenharia, roteiro do vídeo 8, 15/11/2026)

## 7. Só no Samsung

24. Pacote de cobertura de 16/11 (`formacao-dev-cobertura-2026-11-16.md`, nas notas da sessão). Já está publicado nas issues; não precisa ir para o Acer.
25. Memória `formacao-dev-roadmap-sh.md`: o roadmap.sh entra só por link (ADR 001). Precisa ir para o Acer, como item do engenharia ou cópia da memória.
26. Nenhuma tarefa agendada, script, vídeo ou rascunho fora do GitHub.

## 8. Próximos passos recomendados

27. Cobertura por tópico nas 9 trilhas restantes: formacao-dev#3, #5 a #10, #12 e #13, pela árvore do developer-roadmap.
28. PR no `CATALOGO.md` que soma o roadmap DevRel à T11 (formacao-dev#14).
29. Rever as 84 seções "fora do escopo por agora" (formacao-dev#3 a #14).
30. Pedir o Pages do formacao-dev (formacao-dev#38 e `PAGES_ATIVO`) antes de gravar o vídeo 13 (formacao-dev#284).
31. Medir a ativação: formacao-dev#293 (T11.11), com o prazo de formacao-dev#290 (T8.14).
