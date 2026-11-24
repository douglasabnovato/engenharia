# 3 · MCP e conectores

## Conceito

O **MCP** (Model Context Protocol) é um padrão aberto para ligar o Claude a ferramentas e dados externos (GitHub, Cloudflare, Notion, bancos) por um servidor que expõe ferramentas tipadas. Em vez de montar comandos de shell, o agente chama, por exemplo, uma ferramenta "listar runs do CI" com parâmetros validados.

No Claude Code, um servidor MCP de projeto fica em `.mcp.json`. No app, os conectores são ligados pelo responsável. Cada ferramenta pode ser liberada ou negada nas permissões.

Vantagens sobre o shell:
- permissões por ferramenta, como "só leitura";
- saída estruturada;
- menos pedidos de permissão para comandos parecidos.

Cuidado: tudo o que um servidor MCP devolve é **dado**, não ordem. Uma issue ou página lida por MCP pode conter texto escrito para enganar o agente.

Fontes: [MCP no Claude Code](https://code.claude.com/docs/en/mcp), [`arquitetura-ia.md`](../arquitetura-ia.md) (camada 8).

## Hoje no ecossistema

- Nenhum repositório tem `.mcp.json` ([`ambientes/learntech.md`](../ambientes/learntech.md)).
- O GitHub é lido por `gh` no shell em todos os ambientes.
- O LearnTech registrou uma tarefa das 7h que "parou num pedido de permissão" (`learntech-content/docs/engenharia/relatorios/dia-2026-11-12.md`).

## Experimento

**Hipótese:** ler CI, issues e PRs por um servidor MCP do GitHub, só de leitura, reduz os pedidos de permissão das revisões D-1 sem abrir escrita.

| Passo | Quem |
|---|---|
| 1. Linha de base: pedidos de permissão por execução da revisão D-1 do LearnTech, por 5 dias | repositórios LearnTech |
| 2. Ligar um servidor MCP do GitHub com ferramentas só de leitura, liberadas nas permissões; as de escrita negadas | responsável (configuração, R12) |
| 3. Trocar no prompt da revisão D-1 o `gh` de leitura pelas ferramentas MCP | arquitetura de IA |
| 4. Medir por 5 dias | repositórios LearnTech |

## Métrica

- Pedidos de permissão por execução: meta 0 nas leituras.
- Execuções da revisão D-1 que terminam sem travar: meta 100%.
- Tempo de cada execução.

## Resultado

A medir. Depende da configuração do responsável.
