# Passagem Samsung → Acer · DG mundo (learnTECH) · 21/11/2026

Dados conferidos no GitHub e no disco às 13h35 de 21/11. Sessão dona: hoje "repositórios LearnTech", no Acer.

## 1. Papel

1. Abre em `C:\douglasabnovato-github\mundo-learn-tech`, no Samsung. Trabalha sempre em clone temporário.
2. Dona de 5 repositórios (R4): learntech-content (a API), learn-tech, tools, career e bootcamps. Cuida também da pasta `hd`, a fonte do conteúdo.
3. Faz: ciclo de MVP, conteúdo a partir do `hd` (triador e gabarito), issues no modelo e integração por `--ff-only` depois do CI verde. Branches de integração: `developer` (learntech-content, tools, bootcamps), `developer-mvp-2026` (learn-tech), `developer-mvp-2026-2` (career).
4. Não faz: tocar na `main`, deploy, configuração, segredos, contas, custo ou modelo de negócio, nem decidir sozinha sobre material de ex-empregador. Autonomia AU0: toda decisão de conteúdo vai ao responsável.

## 2. Estado por repositório

| Repositório | MVP na main → na integração | Finalizado | No ar (21/11) | CI da main |
|---|---|---|---|---|
| learntech-content | 7 → 7 de 12 | não | `https://learntech-content.douglasabnovato.workers.dev/v1/saude` 200 | verde 21/11 |
| learn-tech | 5 → 8 de 12 | não | `https://learn-tech-pied.vercel.app/` 200 | verde 19/11 |
| tools | 5 → 8 de 12 | não | `https://douglasabnovato.github.io/tools/` 200 | verde 19/11 |
| career | 5 → 9 de 12 | não | `https://douglasabnovato.github.io/career/` 200 | verde 19/11 |
| bootcamps | 5 → 8 de 12 | não | `https://bootcamps-dun.vercel.app/` 200 | verde 19/11 |

5. A integração foi para a main em 18 e 19/11: learntech-content#31, learn-tech#145, tools#65, career#40 e bootcamps#80.

## 3. Em andamento

6. learntech-content#33 (`feature/tasks-20-11-2026-f` → `developer`, 20/11, CI verde): um recurso por item no tools (ADR 13). Aberto por outra sessão; conferir a origem antes de mesclar.
7. Integrações à frente da main: learntech-content +7, learn-tech +3, tools +3, bootcamps +2, career +1.
8. `feature/2026-11-17-revisao-lote` (learntech-content, dc932d9): correções da revisão do lote de 15/11, CI verde, não integradas. Está 18 commits atrás da `developer`; reaplicar o commit numa branch nova.
9. O clone temporário de 17/11 tem o índice do git corrompido: descartar. O que importa está no GitHub.

## 4. Decisões do responsável (registro em `learntech-content/docs/processo/decisoes-do-autor.md`)

10. 15/11, "aprovo o plano": método de produção a partir do `hd` (ficha de análise, perfil do autor, níveis de autonomia, produtores, gabarito).
11. 15/11, "Sim, AU0 a AU2": escala de autonomia. Sair do AU0 pede 85% ou mais no gabarito em direitos e destinos, com 20 itens ou mais.
12. 15/11, "Sim, adote" (D-11): material de ex-empregador com conhecimento aproveitável é `sensivel-anonimizar`; `descartar` só para o que não tem uso.
13. 15/11: P-01 a P-09 confirmados ("Confirmo P-01 a P-07", "Confirmo o P-08", "Confirmo o P-09").
14. 16/11, sobre a learntech-content#12: "precisamos avaliar que são conteúdos já na API e exibidos nos projetos". Conferência no comentário da #12.
15. 16/11, política do Dependabot ("alertas que nao atrapalham a producao, pode passar..."): ainda não registrada como D-12, à espera da confirmação dele no chat.

## 5. Com o responsável

16. learntech-content#29: aprovar a triagem das 94 issues antigas (uma linha por grupo de A a F). Libera fechar 44 e rotular 25.
17. learntech-content#15: vídeos do `hd` (YouTube, armazenamento ou descarte). Libera o `hd` parado (D-07) e a rodada 5 do gabarito.
18. learntech-content#12: fechar como atendida ou marcar 1.746 arquivos como `bloqueado`.
19. learntech-content#23 e #24: hipótese do MVP e medição de uso. Destravam os critérios 2 e 5 nos 5 MVPs.
20. learntech-content#27: ligar os alertas do Dependabot (API dá 403 nos 5).
21. Gabarito: confirmar os rótulos do HD-0049 e do HD-0054. Perfil do autor: confirmar níveis e números. D-07: quais são as "4" de "Aprovo as 4".

## 6. Aprendizados novos

22. Gabarito de agente se revisa junto com a medição: erro concentrado num tipo pode ser da regra, não do agente. (learntech-content, 15/11/2026)
23. Número de testes citado em documento envelhece rápido: citar com data, ou não citar. (learntech-content, 17/11/2026)
24. Branch que espera integração por dias deixa de ser fast-forward: integrar no mesmo dia ou reaplicar numa branch nova. (learntech-content, 21/11/2026)

## 7. Só no Samsung

25. `C:\douglasabnovato-github\mundo-learn-tech\hd`: 6.386 arquivos, a fonte do learnTECH, com os caches `.hash-cache.json`, `.imagens-publicadas.json` e `.extraido/`. **Precisa ir para o Acer**, senão o `hd:uso`, o triador e o gabarito não rodam. É material privado: nunca vai para o GitHub. A cópia é do responsável (disco externo ou armazenamento privado), para `../hd` em relação ao clone do learntech-content.
26. `mundo-learn-tech\.claude\launch.json`: configuração de preview. Copiar junto.
27. Memória: `.claude\projects\C--douglasabnovato-github-mundo-learn-tech\memory\` (10 arquivos: fluxo do dia, hora local, ficha de ciclo, política do Dependabot, regras de negócio, logos). Sem segredo. Copiar para o caminho do projeto no Acer.
28. Tarefa agendada `abertura-do-dia-learntech` e `convites-learntech` (convites da organização learnTECH-community). Desligar no Samsung para não rodar em dobro, sobretudo os convites.
29. Rascunhos do scratchpad (rodada 4, textos das issues, conferência da #12): os resultados já estão nos relatórios e no GitHub. `e.txt` e `_tmp-claude`: temporários.

## 8. Próximos passos recomendados

30. Mesclar o learntech-content#33 depois de conferir a sessão de origem.
31. Reaplicar o dc932d9 numa branch nova a partir da `developer`, com CI e `--ff-only`.
32. Copiar o `hd` para o Acer e rodar `npm run hd:uso` para provar que está inteiro (3.631 arquivos e 2.683 únicos em 09/11).
33. Responsável: decidir a learntech-content#29 e a #15.
34. Responsável: decidir a learntech-content#23 e a #24, que travam o Finalizado nos 5 MVPs.
