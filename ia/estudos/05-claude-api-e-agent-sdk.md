# 5 · Claude API e Agent SDK

## Conceito

Há quatro jeitos de pôr o Claude dentro de um produto, do mais simples ao mais completo:

| Jeito | O que é | Quando usar |
|---|---|---|
| **Messages API**, uma chamada | `POST /v1/messages`: uma pergunta, uma resposta. Com **saída estruturada** (`output_config.format`), a resposta segue um esquema JSON | Classificar, extrair, resumir |
| **Messages API com ferramentas** | O código define ferramentas, o modelo pede para usá-las, o código executa e devolve. O *tool runner* do SDK faz esse laço | Fluxo com várias etapas controlado pelo código |
| **Managed Agents** (beta) | A Anthropic roda o laço do agente e um contêiner por sessão, com agente versionado | Agente de longa duração sem hospedar nada |
| **Claude Agent SDK** | O próprio Claude Code como biblioteca (`claude-agent-sdk` / `@anthropic-ai/claude-agent-sdk`), com Read, Edit, Bash, subagentes e hooks | Agente de código ou de arquivos rodando na nossa máquina ou na CI |

### Modelos atuais

Tabela em cache de 03/11/2026, preço por milhão de tokens:

| Modelo | Id | Entrada / saída | Para quê |
|---|---|---|---|
| Claude Opus 5.5 | `claude-opus-5-5` | US$ 4 / US$ 20 | Padrão: código, agentes, revisão |
| Claude Sonnet 5.5 | `claude-sonnet-5-5` | US$ 2 / US$ 10 | Trabalho do dia a dia com mais volume |
| Claude Haiku 5.5 | `claude-haiku-5-5` | US$ 0,10 / US$ 0,50 | Classificação e extração em volume, subagentes de varredura |
| Claude Fable 5.2 | `claude-fable-5-2` | US$ 8 / US$ 40 | O mais capaz, para raciocínio longo e difícil |

Para conferir antes de usar, consulte `GET /v1/models`.

### O que reduz custo sem perder qualidade

- **Cache de prompt:** o prefixo estável (ferramentas, sistema) é cobrado bem mais barato na releitura.
- **Message Batches:** cobra 50% do preço, para o que não tem pressa.
- **Esforço** (`output_config.effort`, de `low` a `max`): controla quanto o modelo pensa. No Opus 5.5, o padrão é `medium`.
- **Contagem de tokens** (`/v1/messages/count_tokens`): mede antes de mandar.

Fontes: [documentação da API](https://platform.claude.com/docs), [Agent SDK](https://code.claude.com/docs/en/agent-sdk).

## Hoje no ecossistema

- O `triador` do learntech-content roda como subagente do Claude Code e é medido por `npm run triador:gabarito` (76% em direitos, 67% em destinos).
- O `controle-financas` lê cupom fiscal com um LLM de outro provedor (`server/src/services/receiptExtractor.js`). A issue #29 trata dos erros de leitura.

## Experimentos

**A. Triador fora da conversa.** Hipótese: rodar o gabarito do triador pelo Agent SDK, sem a sessão do app, torna a medição repetível na CI e mais barata.

| Passo | Quem |
|---|---|
| 1. Script que roda o triador pelo Agent SDK sobre o gabarito e grava a nota | repositórios LearnTech, com o desenho daqui |
| 2. Comparar a nota com a da sessão, e o custo em tokens por rodada | arquitetura de IA |

**B. Extração de cupom com saída estruturada.** É só uma proposta, porque troca de provedor é decisão do responsável e tem custo. Hipótese: com saída estruturada e um gabarito de 15 cupons sintéticos (sem dado pessoal), dá para medir o acerto por campo e escolher pelo número.

## Métrica

- A: a mesma nota (±2 pontos) e o custo por rodada.
- B: acerto por campo (data, total, CNPJ fictício, itens) e custo por cupom.

## Resultado

A medir. O B depende do ok do responsável (custo e provedor).
