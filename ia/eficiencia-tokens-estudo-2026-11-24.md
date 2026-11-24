# Estudo · eficiência de contexto e tokens no Claude Code (24/11/2026, 18h45)

Pedido do Líder de TODOS no pulso das 18h43. O estudo compara a documentação oficial com o nosso processo de 24/11 (`orquestrador/processo-eficiencia-tokens-2026-11-24.md`, que é local).

**Fontes** (lidas em 24/11/2026; as páginas não mostram data de atualização):
- [Manage costs effectively](https://code.claude.com/docs/en/costs)
- [Memory (CLAUDE.md e memória)](https://code.claude.com/docs/en/memory)
- [Prompt caching](https://code.claude.com/docs/en/prompt-caching)

## 1. O que a documentação recomenda

| Tema | Recomendação oficial | Fonte |
|---|---|---|
| Limpar o contexto | `/clear` entre tarefas sem relação. `/rename` e depois `/resume` para voltar | costs |
| Compactar | `/compact` com foco ("Focus on ...") nas pausas naturais, e não no meio da tarefa. O CLAUDE.md pode ter uma seção `# Compact instructions` | costs |
| Subagentes | delegar trabalho verboso (testes, logs, leitura ampla), para voltar só o resumo. Eles também gastam | costs |
| Modelo e esforço | o modelo leve para subagente simples (`model: haiku`); esforço menor com `/effort`. O pensamento é cobrado como saída | costs |
| MCP e ferramentas | preferir as CLI (`gh`) e desligar os servidores que não se usam (`/mcp`) | costs |
| Tamanho do CLAUDE.md | menos de **200 linhas por arquivo**. Regra só de uma parte vai para `.claude/rules/` com `paths:`. O `@import` **não** reduz o contexto | memory |
| Memória automática | só as **primeiras 200 linhas ou 25 KB** do `MEMORY.md` carregam no início | memory |
| Cache | o prefixo é guardado na ordem: sistema e ferramentas, depois o contexto do projeto, depois a conversa. Ele **quebra** ao trocar de modelo, ao ligar o modo rápido, com MCP novo, com `/compact`, com a atualização do Claude Code e com pausa além do TTL (5 min ou 1 h) | prompt-caching |
| Saída grande | cada resultado de ferramenta engorda o contexto e é reenviado a cada pedido. Um hook pode filtrar a saída, e um subagente pode ler o que é grande | costs |
| Medir | `/usage` mostra o custo estimado, os tokens por modelo e o **% de entrada vindo do cache**. `/context` mostra o que enche a janela | costs |

## 2. O nosso processo × a documentação

| O nosso processo diz | A documentação | Situação |
|---|---|---|
| ciclo PDCA de 1 a 3 itens por turno, em vez de muitos turnos pequenos | o contexto é reenviado a cada pedido | **confirma** |
| checkpoint acima de 60% e sessão nova barata, com o estado em arquivo | `/clear` entre tarefas, `/compact` nas pausas e `/resume` | **confirma**. Falta dizer **quando** usar `/compact` com foco, e não só o checkpoint |
| leitura ampla num subagente Explore; `gh --json` com só os campos | subagente para trabalho verboso; filtrar a saída | **confirma** |
| mensagem entre sessões aponta o arquivo, e não copia | não está na documentação | [HIPÓTESE]: ela reduz a entrada da sessão que recebe, mas não foi medida |
| pulso a cada 2 h, e não a cada hora | o cache vence com o TTL (5 min ou 1 h) | **confirma, com custo:** cada pulso depois do TTL relê tudo sem cache. Acordar menos vezes é o certo |
| indicador "% do plano ÷ entregas" | o `/usage` dá os tokens e o % de cache por sessão | **falta:** o indicador não usa o % de cache, que a documentação dá de graça |
| — | CLAUDE.md com menos de 200 linhas; `MEMORY.md` lido só até 200 linhas ou 25 KB | **falta no processo.** Hoje o `CLAUDE-raiz.md` tem 61 linhas, e o `MEMORY.md` desta sessão tem 10 linhas e 1,5 KB, então está ok |
| — | o modelo leve (`haiku`) para subagente simples | **falta no processo.** Os Esp e os subagentes herdam o modelo da sessão |

## 3. Até 5 ações medíveis

| # | Ação | Medida | Meta |
|---|---|---|---|
| 1 | Cada dona roda `/usage` no fim do ciclo e anota o **% de entrada vindo do cache** no resumo | % de cache por ciclo | [HIPÓTESE] acima de 70% nos ciclos dentro do TTL. Medir 1 semana antes de fixar a meta |
| 2 | Usar `/compact` com foco (por exemplo, "Focus on a fila local e os PRs abertos") ao fechar o ciclo, quando o contexto passa de 60% e a sessão continua | o % de contexto antes e depois (`/context`) | [HIPÓTESE] voltar a menos de 30% |
| 3 | Subagente de busca ou leitura simples com `model: haiku`, quando a dona pedir só um fato (web-fetch, Explore de 1 pergunta) | os tokens do subagente no `/usage` | [HIPÓTESE] menos da metade do custo com o modelo da sessão, para a mesma resposta |
| 4 | Conferir uma vez por semana se cada `CLAUDE.md` tem menos de 200 linhas e cada `MEMORY.md` menos de 200 linhas ou 25 KB | `wc -l` e `wc -c` | 100% dos arquivos dentro do limite |
| 5 | Não trocar de modelo nem de modo rápido no meio de um ciclo. Uma troca, só no começo do ciclo | trocas por ciclo (anotadas no resumo) | 0 no meio do ciclo |

## 4. O que fica de fora
- **Mudar a configuração** (modelo padrão, `/config`, servidores MCP): é do responsável (R12).
- **O comando `/cost`:** não aparece nas 3 páginas lidas, então não sei o que ele mostra hoje.
