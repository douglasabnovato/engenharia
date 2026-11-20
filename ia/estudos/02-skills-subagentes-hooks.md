# 2 · Skills, subagentes e hooks

## Conceito

Três formas de dar ao Claude Code um comportamento repetível, da mais flexível à mais rígida:

| Recurso | O que é | Onde fica | Quando usar |
|---|---|---|---|
| **Skill** | Um procedimento escrito uma vez e carregado só quando o pedido combina com a descrição | `.claude/skills/<nome>/SKILL.md` | Um processo que se repete ("abrir issue no modelo") |
| **Subagente** | Um papel com ferramentas, modelo e instruções próprias. Recebe um brief, trabalha num contexto separado e devolve só a conclusão | `.claude/agents/<nome>.md` | Leitura ampla, revisão sem viés, especialista por disciplina |
| **Hook** | Um comando que o próprio Claude Code roda num evento (antes de uma ferramenta, depois de gravar, ao iniciar) e que pode recusar a ação | `settings.json`, chave `hooks` | Uma regra que não pode depender da memória |

Regra de escolha: preferência vira skill, papel vira subagente, proibição vira hook.

Fontes: [skills](https://code.claude.com/docs/en/skills), [subagentes](https://code.claude.com/docs/en/sub-agents), [hooks](https://code.claude.com/docs/en/hooks), [`recursos.md`](../recursos.md).

## Hoje no ecossistema

- **Skills:** 7 no `engenharia`, que só valem quando a sessão abre nele (#16). Mais 1 no learntech-content (`produzir-do-hd`).
- **Subagentes:** 14 no `engenharia` (3 revisores e exploradores e 11 especialistas da F1). Mais o `triador` no learntech-content.
- **Hooks:**
  - o `bloquear_proibidos.py` está pronto e testado, mas desligado (#17);
  - os hooks que rodam hoje são do AmploPay, pelo `settings.json` global.

## Experimento

**Hipótese:** a revisão pelos especialistas (R19) encontra, antes do merge, defeitos que hoje só aparecem depois.

| Passo | Quem |
|---|---|
| 1. Linha de base: nos 10 últimos PRs mesclados de 5 repositórios N2, contar os commits `fix` nas 48 horas seguintes (falha de mudança) | arquitetura de IA |
| 2. Nos próximos 10 PRs desses repositórios, chamar `qa`, `a11y` e `performance` antes do merge na sprint | repositórios GitHub |
| 3. Registrar os achados de cada especialista e quantos eram reais | repositórios GitHub |
| 4. Comparar a falha de mudança | arquitetura de IA |

Experimento paralelo, de hook: depois da instalação, contar os comandos proibidos recusados por semana. Cada recusa é um erro que não aconteceu.

## Métrica

- Falha de mudança: meta ≤ 15% ([`ciclo-evolutivo.md`](../../processo/ciclo-evolutivo.md)).
- Precisão dos especialistas: achados reais sobre achados totais. Meta ≥ 70%.
- Comandos proibidos recusados pelo hook.

## Resultado

A medir.
