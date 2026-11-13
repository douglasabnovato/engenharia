# engenharia

Base central de engenharia do portfólio de `douglasabnovato`: arquitetura de software, processo e trabalho com IA (Claude Code). Vale para todos os repositórios do portfólio.

Ela nasceu dos ciclos de outubro e novembro de 2026, em que 39 repositórios foram levados a MVP por um responsável, um coordenador e agentes do Claude Code trabalhando em lotes. Tudo o que deu certo virou regra; tudo o que deu errado virou aprendizado.

## Como consultar

| Quero... | Leia |
|---|---|
| Saber o que se cobra de um projeto (níveis, 12 critérios, segurança) | [`arquitetura/padroes.md`](arquitetura/padroes.md) |
| Trabalhar num repositório do começo ao fim | [`ia/processo-repositorio.md`](ia/processo-repositorio.md) |
| Evitar uma armadilha já conhecida (Windows, Playwright, Lighthouse, Render...) | [`ia/aprendizados.md`](ia/aprendizados.md) |
| Publicar uma API com banco | [`arquitetura/deploy/render-atlas.md`](arquitetura/deploy/render-atlas.md) |
| Publicar um site estático | [`arquitetura/deploy/pages-vercel-netlify.md`](arquitetura/deploy/pages-vercel-netlify.md) |
| Abrir uma issue | [`processo/modelo-issue.md`](processo/modelo-issue.md) |
| Saber se algo está pronto | [`processo/definicao-de-pronto.md`](processo/definicao-de-pronto.md) |
| Entender branches e quem mescla | [`processo/fluxo-git.md`](processo/fluxo-git.md) |
| Fazer o que só o dono do repositório faz | [`processo/guia-do-responsavel.md`](processo/guia-do-responsavel.md) |
| Coordenar agentes | [`ia/como-trabalhamos.md`](ia/como-trabalhamos.md) e [`ia/briefs/`](ia/briefs/) |
| Saber quem coordena as sessões e quem é dono de cada repositório | [`ia/orquestracao.md`](ia/orquestracao.md) |
| Ver a arquitetura de IA inteira (sessões, memória, skills, agentes, proteções) | [`ia/arquitetura-ia.md`](ia/arquitetura-ia.md) |
| Escolher entre sessão, subagente, agendamento ou skill | [`ia/recursos.md`](ia/recursos.md) |
| Bloquear as ações proibidas com hook | [`ia/hooks.md`](ia/hooks.md) |

## Mapa das pastas

```
README.md              este índice
CLAUDE-raiz.md         proposta de CLAUDE.md para a pasta que guarda os clones do portfólio
arquitetura/
  padroes.md           níveis N1/N2/N3, régua dos 12 critérios, pilhas de referência, segurança
  modelo-c4.md         como documentar C4 em Mermaid (exemplo: aircnc)
  modelo-adr.md        formato de ADR e exemplos
  modelo-analise.md    especificação, requisitos com critério de aceite, defeitos com severidade
  deploy/              Render + Atlas; Pages, Vercel e Netlify
ia/
  orquestracao.md      orquestrador, sessões donas e regras R1 a R17
  prompts/dg-lider.md  prompt para criar a sessão orquestradora
  arquitetura-ia.md    mapa da IA: camadas, sessões, protocolo, regras, skills, agentes, técnicas
  recursos.md          quando usar cada recurso avançado, custo e armadilhas
  hooks.md             hook que recusa force push, --no-verify e push na principal
  como-trabalhamos.md  responsável, coordenador, agentes, revisor independente, permissões
  processo-repositorio.md  passos 0 a 8, decisões, limites, fases de um projeto novo
  aprendizados.md      todas as lições, por tema
  briefs/              modelos de brief para agentes (ciclo completo e ciclo curto)
processo/
  fluxo-git.md         feature → sprint → principal; ruleset da principal
  modelo-issue.md      Objetivo, Motivo, Critérios, Fora desta issue; rótulos; Project
  definicao-de-pronto.md  "Atende" com evidência; "Finalizado"
  guia-do-responsavel.md  o que só o dono faz, passo a passo
decisoes/              decisões datadas, com opções e justificativa
.claude/
  skills/              relatorio-do-dia, ciclo-repositorio, evidencia-atende, revisao-de-fatos, aviso-entre-sessoes
  agents/              revisor-independente, revisor-de-fatos, explorador
scripts/               estado, relatório, Project e configuração (ver scripts/README.md)
```

## Como as sessões do Claude Code usam

1. Na pasta que guarda os clones do portfólio, um `CLAUDE.md` (proposta em [`CLAUDE-raiz.md`](CLAUDE-raiz.md)) importa os documentos principais com `@engenharia/...`. Toda sessão aberta ali já começa com o processo, os padrões e os aprendizados.
2. O coordenador escreve o brief de cada lote a partir de [`ia/briefs/`](ia/briefs/), citando os arquivos daqui em vez de copiá-los.
3. Cada agente lê o processo e o tema dos aprendizados da sua pilha antes de mexer no repositório.
4. No fim de cada lote, o coordenador traz as lições novas para [`ia/aprendizados.md`](ia/aprendizados.md) e registra a decisão em [`decisoes/`](decisoes/).

## Como mudar esta base

- Pelo mesmo fluxo dos outros repositórios: `feature/AAAA-MM-DD` → `developer/sprint-<quinta>` → `main`, com revisão do responsável.
- Aprendizado novo: no tema certo, sem repetir; se for variação, melhore o item que já existe.
- Repositório público: nada de senhas, tokens, URIs com credencial, e-mails, telefones, nomes de pessoas de fora ou dados pessoais.
