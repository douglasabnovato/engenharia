# Ambientes de trabalho com IA

Os três ambientes do portfólio na máquina do responsável: o que cada um guarda, qual sessão trabalha nele e até onde a arquitetura de IA de [`arquitetura-ia.md`](../arquitetura-ia.md) chegou de fato em cada um.

Levantado em 18/11/2026 pela sessão "Análise de arquitetura de IA" (pasta `C:\douglasabnovato-ia`), a pedido do responsável. A leitura foi só de leitura nas três pastas, com três subagentes de leitura e conferência direta dos pontos citados.

## Mapa

| Ambiente | Pasta | Sessão no app | O que guarda | Detalhe |
|---|---|---|---|---|
| Comunidade | `C:\douglasabnovato-community` | "comunidade LearnTech" | `formacao-dev` (learnTECH Community): catálogo de 161 itens em 12 trilhas e o Painel de Formação | [`community.md`](community.md) |
| GitHub | `C:\douglasabnovato-github` | "repositórios GitHub" | 40 repositórios de portfólio, `figma-design` e a pasta `revisao/` | [`github.md`](github.md) |
| LearnTech | `C:\douglasabnovato-learntech` | "repositórios LearnTech" | learntech-content (API e conteúdo) e os sites learn-tech, bootcamps, career e tools | [`learntech.md`](learntech.md) |

Relação com a [`orquestracao.md`](../orquestracao.md): "repositórios LearnTech" faz o papel da DG mundo, e "repositórios GitHub" o da DG github. O ambiente Comunidade **não aparece** na tabela R4: não tem sessão dona registrada nem sigla (inferido · confirmar com o responsável).

## Maturidade da IA por ambiente

Contado em 18/11/2026 nas pastas locais. As camadas são as de [`arquitetura-ia.md`](../arquitetura-ia.md).

| Camada | Comunidade | GitHub | LearnTech |
|---|---|---|---|
| `CLAUDE.md` na pasta raiz (proposta [`CLAUDE-raiz.md`](../../CLAUDE-raiz.md)) | não | não | não |
| `engenharia/` clonado na pasta raiz | não | não | não |
| `CLAUDE.md` por repositório | 0 de 1 | 0 de 41 | 5 de 5 |
| Skills versionadas no repositório | 0 | 0 | 1 (`produzir-do-hd`) |
| Agentes versionados no repositório | 0 | 0 | 1 (`triador`) |
| `.claude/settings.json` do projeto (permissões, hooks) | 0 | 0 | 0 |
| Hook do portfólio ([`hooks.md`](../hooks.md)) ligado | não (#17) | não (#17) | não (#17) |
| Memória em arquivo | `docs/MVP.md`, 1 diário | `docs/MVP.md` em 40, `revisao/` | `ESTADO.md`, relatórios do dia, `conversas/` |
| Avaliação de saída do agente | régua do MVP | régua do MVP, `AVALIACAO.md` | régua do MVP, gabarito do triador (`npm run triador:gabarito`) |
| Commits com `Co-Authored-By: Claude` | 210 de 347 | 1.655 de 4.775 | não medido |

Leitura: a IA escreve boa parte do código nos três ambientes, mas a camada de instrução (camada 1) não está ligada em nenhum, e as proteções (camada 9) continuam sendo texto. O LearnTech é o único com regras por repositório e um agente medido.

## Achados que valem para os três

1. **O `CLAUDE.md` raiz não existe.** Nenhuma das três pastas tem o `CLAUDE.md` proposto em [`CLAUDE-raiz.md`](../../CLAUDE-raiz.md), e nenhuma tem o `engenharia/` clonado, que ele importa com `@engenharia/...`. Uma sessão aberta nessas pastas não carrega as regras 1 a 16. Ligar é do responsável (copiar o arquivo e clonar o `engenharia` em cada pasta raiz).
2. **Os hooks globais são do AmploPay.** O `~/.claude/settings.json` tem `deny` (leitura de `.env`, force push, `gh pr merge`) e hooks `UserPromptSubmit`, `PreToolUse`, `PostToolUse` e de compactação que apontam para `C:\amplopay\ferramentas\hooks\`. Eles rodam também nas sessões do portfólio. A frase "o `settings.json` do usuário não tem regras de permissão nem hooks", em [`arquitetura-ia.md`](../arquitetura-ia.md), estava certa em 12/11 e mudou depois.
3. **O hook do portfólio continua desligado.** [`scripts/hooks/bloquear_proibidos.py`](../../scripts/hooks/bloquear_proibidos.py) está pronto e testado, mas não aparece no `settings.json` (#17). A proposta é ligá-lo no `.claude/settings.json` de cada pasta raiz, e não no global, para não misturar com o AmploPay.
4. **As skills e os agentes do `engenharia` não chegam às sessões.** Eles só valem quando a sessão abre no `engenharia` (#16). As três sessões abrem em outras pastas.

## Processo: orientações de IA por ambiente

Pedido do responsável em 18/11/2026: "quando houver a oportunidade de aperfeiçoar o processo de arquitetura de ia, voce vai sugerir para cada um deles em um arquivo chamado orientacoes-ia e comunicará o chat do ambiente em questao".

1. A sessão de arquitetura de IA lê o ambiente, só leitura.
2. O que vale para todos vai para este repositório: esta pasta, [`arquitetura-ia.md`](../arquitetura-ia.md) ou [`aprendizados.md`](../aprendizados.md).
3. O que é do ambiente vira sugestão em `orientacoes-ia.md`, **na pasta raiz do ambiente**, fora de qualquer repositório. Assim a sessão de arquitetura não escreve em repositório que não é dela (R4).
4. Cada sugestão tem: evidência (arquivo ou comando), proposta, quem faz (Claude ou responsável) e tamanho.
5. A sessão manda ao chat do ambiente um aviso no formato da skill [`aviso-entre-sessoes`](../../.claude/skills/aviso-entre-sessoes/SKILL.md), com o caminho do arquivo e os três itens mais importantes.
6. A sugestão **não é ordem** (R1). A sessão do ambiente só executa com o ok do responsável, dado na própria sessão.
7. Na rodada seguinte, o arquivo ganha uma seção "Situação" com o que foi feito, recusado ou adiado. Recusa do responsável não volta como sugestão (regra 14).

| Ambiente | Arquivo de orientações |
|---|---|
| Comunidade | `C:\douglasabnovato-community\orientacoes-ia.md` |
| GitHub | `C:\douglasabnovato-github\orientacoes-ia.md` |
| LearnTech | `C:\douglasabnovato-learntech\orientacoes-ia.md` |

Sigla proposta para os avisos desta sessão: `IA`. Falta a confirmação do responsável e a entrada na R8.
