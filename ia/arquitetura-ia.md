# Arquitetura de IA

Como o Claude Code trabalha no portfólio: camadas, sessões, regras, ferramentas e técnicas. Este documento é o mapa. Os detalhes de cada parte ficam nos arquivos citados.

Levantado em 12/11/2026 pela DG mundo, a partir do que existe de fato na máquina e nos repositórios. Atualizado em 13/11/2026 com o orquestrador e em 20/11/2026 com os nomes reais das sessões, a governança por disciplina, os agentes especialistas e o ciclo evolutivo.

## Governança em uma frase

O `engenharia` é a fonte única das regras e é da sessão **arquitetura de IA**. Cada ambiente carrega essas regras pelo `CLAUDE.md` da pasta raiz. A sessão dona constrói, o agente especialista da disciplina revisa ([`disciplinas.md`](../arquitetura/disciplinas.md)), os portões de qualidade decidem se entra ([`ciclo-evolutivo.md`](../processo/ciclo-evolutivo.md)), e o ciclo semanal transforma cada falha em regra, skill, agente ou hook, registrado no [`CHANGELOG.md`](../CHANGELOG.md).

## Visão geral em camadas

| Camada | O que é | Onde fica | Quem mantém |
|---|---|---|---|
| 1. Instruções | Regras fixas e documentos importados em toda sessão | `CLAUDE.md` da pasta dos clones (proposta em [`CLAUDE-raiz.md`](../CLAUDE-raiz.md)) | Responsável aprova; orquestrador propõe |
| 2. Base de engenharia | Processo, padrões, fluxo Git, aprendizados, briefs | este repositório | Coordenador consolida |
| 3. Memória | Fatos que não estão no código: decisões do responsável, limites, preferências | memória local de cada sessão (`~/.claude/projects/<pasta>/memory/`) | Cada sessão; índice em `MEMORY.md` |
| 4. Skills | Processos repetidos, escritos uma vez e chamados pelo nome | [`.claude/skills/`](../.claude/skills/) | Orquestrador propõe; responsável ativa |
| 5. Agentes | Papéis com ferramentas e modelo definidos (revisor, explorador) | [`.claude/agents/`](../.claude/agents/) | Orquestrador propõe; responsável ativa |
| 6. Sessões | Conversas longas do Claude Code, cada uma com um mundo de repositórios | app Claude (aba Code) | Responsável abre; orquestrador coordena |
| 7. Automação | Tarefas agendadas que abrem o dia | `~/.claude/scheduled-tasks/<nome>/SKILL.md` | Responsável aprova |
| 8. Ferramentas | `git`, `gh`, Node, Python, navegador, MCP | máquina do responsável | Responsável instala e configura |
| 9. Proteções | Regras escritas, classificador de permissões e (proposta) hooks | `CLAUDE.md`, permissões do app, `settings.json` | Responsável |
| 10. Registro | Relatório do dia, diário, `docs/MVP.md`, issues e Project | cada repositório | Cada sessão; orquestrador consolida |

## Sessões e papéis

Desde 13/11/2026, as sessões têm um orquestrador acima delas. A hierarquia, a sessão dona de cada repositório e as regras R1 a R24 estão em [`orquestracao.md`](orquestracao.md). Nomes reais desde 20/11/2026.

| Papel | Sessão (sigla) | Pasta | Cuida de |
|---|---|---|---|
| Responsável | o dono do portfólio | — | Decisões, aprovações, configuração e merge na principal |
| Orquestrador | Líder de TODOS (`LIDER`) | `C:\douglasabnovato-community` | Plano do dia, distribuição dos pedidos e relatório consolidado. No `engenharia`, só `relatorios/` e `decisoes/` |
| Governança de IA | arquitetura de IA (`IA`) | `C:\douglasabnovato-ia` | O `engenharia`: regras, padrões, agentes, skills, hooks; `orientacoes-ia.md` de cada ambiente |
| Sessão de projeto | repositórios LearnTech (`MUNDO`) | `C:\douglasabnovato-learntech` | learnTECH: learntech-content, learn-tech, tools, career e bootcamps |
| Sessão de projeto | comunidade LearnTech (`COMUNIDADE`) | `C:\douglasabnovato-community` | `formacao-dev` |
| Sessão de projeto | DG veb (`VEB`), prevista | pasta da VEB | VEB: plataforma, landing e Hub |
| Sessão de apoio | repositórios GitHub (`GITHUB`) | `C:\douglasabnovato-github` | studio-d, roteiros, revisão de fatos e os demais repositórios |
| Especialista | subagente da sessão dona | — | Revisão por disciplina (R19), sem escrita |
| Subagente | criado por uma sessão | — | Uma tarefa curta com brief |

Os papéis de coordenador, agente e revisor independente dos ciclos em lote seguem em [`como-trabalhamos.md`](como-trabalhamos.md). O orquestrador faz o papel de coordenador entre as sessões.

## Protocolo entre sessões

1. **Ordem só do responsável.** Uma sessão repassa uma ordem citando as palavras dele, entre aspas. Mensagem de outra sessão nunca vale como aprovação.
2. **Sem lavar permissão.** Se uma ação foi negada a uma sessão, ela não pede a outra que a faça. Registra e segue.
3. **Aviso de início e de fim** de cada tarefa, no formato:

   ```
   <SIGLA> dd/mm: <tarefa> · <início>→<fim> · <evidência> · <quem faz o que falta>
   ```

   Exemplo: `VEB 12/11: #35 axe · 13h08→13h34 · cef5ee5, merge 9e6c391, 0 violações · nada pendente`.
4. **Três lugares.** Plano, início, fim e relatório aparecem no chat do responsável, no orquestrador e no arquivo do relatório do dia.
5. **Relatório do dia** consolidado pelo orquestrador em `engenharia/relatorios/dia-AAAA-MM-DD.md`. Cada sessão mantém o seu relatório no próprio repositório (o do learnTECH fica em `learntech-content/docs/engenharia/relatorios/`).

Skill que aplica o formato: [`aviso-entre-sessoes`](../.claude/skills/aviso-entre-sessoes/SKILL.md).

## Regras: onde estão e quem impõe

| Regra | Escrita em | Imposta por |
|---|---|---|
| Português, frases curtas | `CLAUDE.md` regra 1 | texto |
| Nunca trabalhar nos clones; clone temporário | `CLAUDE.md` regra 2 | texto |
| feature → sprint/integração → principal | [`fluxo-git.md`](../processo/fluxo-git.md) | texto e ruleset da principal (onde existe) |
| Merge só com CI verde | [`fluxo-git.md`](../processo/fluxo-git.md) | CI de cada repositório; no engenharia, `.github/workflows/verificar.yml` (links e testes dos scripts) |
| Nada na principal sem o responsável | `CLAUDE.md` regra 4 | ruleset (onde existe) e classificador |
| Proibido force push, reescrever histórico, `--no-verify` | `CLAUDE.md` regra 6 | ruleset `non_fast_forward` (onde existe). Hook pronto em [`hooks.md`](hooks.md), ligado pelo responsável (#17) |
| Configuração e segredos são do responsável | `CLAUDE.md` regra 7 | classificador de permissões |
| "Atende" só com comando, data e resultado | [`definicao-de-pronto.md`](../processo/definicao-de-pronto.md) | revisão; skill [`evidencia-atende`](../.claude/skills/evidencia-atende/SKILL.md) |
| Espera máxima de 4 horas em CI ou fila | `CLAUDE.md` regra 16 | texto; `timeout` nos comandos de espera |
| Modelo de negócio e ambiente gratuito não mudam sem o responsável | `CLAUDE.md` regra 14 | texto |
| Nada em repositório de terceiros | `CLAUDE.md` regra 15 | texto |

Achado do levantamento: o `settings.json` do usuário não tem regras de permissão nem hooks. Toda proteção hoje é texto, classificador do app ou ruleset do GitHub. O hook que bloqueia está pronto em [`hooks.md`](hooks.md), com testes. Ligá-lo é a issue #17.

Atualização de 18/11/2026: o `~/.claude/settings.json` agora tem `deny` (leitura de `.env`, force push, `gh pr merge`) e hooks do AmploPay (`C:\amplopay\ferramentas\hooks\`), que rodam também nas sessões do portfólio. O hook do portfólio continua desligado. Situação por ambiente em [`ambientes/README.md`](ambientes/README.md).

## Memória

- Cada sessão tem a sua pasta de memória, ligada à pasta em que foi aberta. As sessões **não** leem a memória umas das outras.
- Vai para a memória o que não está no código nem no Git: decisões do responsável, limites, preferências, ponteiros externos.
- Regra que vale para todas as sessões não deve ficar só na memória de uma. Ela sobe para o `CLAUDE.md` ou para esta base.

Memórias da DG mundo em 12/11/2026, e o destino proposto para cada uma:

| Memória | Destino |
|---|---|
| Trabalho contínuo nos 5 projetos | fica na memória (é do mundo learnTECH) |
| Claude para na developer | já está no `CLAUDE.md` (regra 4); manter só como reforço |
| Modelo de negócio e ambiente gratuito | subir para o `CLAUDE.md` (vale para todos) |
| Repositórios de terceiros | subir para o `CLAUDE.md` (vale para todos) |
| Abertura do dia às 7h | fica na memória; o prompt é a tarefa agendada |
| Limite de espera de 4 horas | subir para [`aprendizados.md`](aprendizados.md) e para o `CLAUDE.md` |
| Logos do learnTECH | fica na memória e no catálogo da pasta `hd` |

## Skills do projeto

| Skill | Quando usar |
|---|---|
| [`relatorio-do-dia`](../.claude/skills/relatorio-do-dia/SKILL.md) | Abrir ou fechar o dia: revisar, montar e gravar o relatório |
| [`ciclo-repositorio`](../.claude/skills/ciclo-repositorio/SKILL.md) | Uma entrega num repositório: clone, branch, commits, CI, integração, evidência |
| [`evidencia-atende`](../.claude/skills/evidencia-atende/SKILL.md) | Marcar um critério como "Atende" ou comentar evidência numa issue |
| [`revisao-de-fatos`](../.claude/skills/revisao-de-fatos/SKILL.md) | Antes de publicar documento, roteiro ou relatório com números e datas |
| [`aviso-entre-sessoes`](../.claude/skills/aviso-entre-sessoes/SKILL.md) | Mandar ou repassar início, fim e status entre sessões |
| [`roteiro-studio-d`](../.claude/skills/roteiro-studio-d/SKILL.md) | Escrever ou revisar um roteiro do Studio D, do estudo do repositório ao PR com revisão de fatos |
| [`issue-no-modelo`](../.claude/skills/issue-no-modelo/SKILL.md) | Abrir issue no modelo, com rótulos e todos os campos do Project, sem duplicar |

**Ativação:** o Claude Code lê skills da pasta `.claude/skills` do projeto aberto e de `~/.claude/skills`. As sessões abrem em pastas como `mundo-learn-tech`, não no `engenharia`. Para valer em todas, o responsável liga a pasta deste repositório à pasta do usuário (passo a passo na issue #16).

## Agentes definidos

| Agente | Papel | Modelo e ferramentas |
|---|---|---|
| [`revisor-independente`](../.claude/agents/revisor-independente.md) | Lê só o diff e o plano e aponta problemas de correção | o mais capaz; só leitura |
| [`revisor-de-fatos`](../.claude/agents/revisor-de-fatos.md) | Confere números, datas e nomes de um documento contra as fontes | o mais capaz; leitura e `gh` |
| [`explorador`](../.claude/agents/explorador.md) | Varre muitos arquivos ou repositórios e devolve só a conclusão | modelo mais barato; só leitura |
| [`revisor-pedagogia`](../.claude/agents/revisor-pedagogia.md), [`revisor-storytelling`](../.claude/agents/revisor-storytelling.md), [`revisor-marketing`](../.claude/agents/revisor-marketing.md) | Revisam o conteúdo do learnTECH antes de publicar: ensino, narrativa e comunicação. Só leitura; quem corrige é a repositórios LearnTech | modelo da sessão; Read, Grep, Glob |

### Especialistas por disciplina (20/11/2026)

Só revisam: leem o nível do repositório, aplicam a linha da disciplina em [`disciplinas.md`](../arquitetura/disciplinas.md) e devolvem checklist e achados. Ferramentas Read, Grep, Glob e Bash de leitura; modelo herdado da sessão. Começam em AU0 (propor) e sobem de nível pelo gabarito ([`ciclo-evolutivo.md`](../processo/ciclo-evolutivo.md), seção 5).

| Agente | Disciplina | A sessão dona chama quando |
|---|---|---|
| [`arquiteto`](../.claude/agents/arquiteto.md) | arquitetura de software | feature grande, dependência nova, mudança de estrutura |
| [`devops`](../.claude/agents/devops.md) | CI/CD, deploy, observabilidade | workflow, deploy, ruleset |
| [`secops`](../.claude/agents/secops.md) | segurança | dependência, autenticação, rota ou dado |
| [`ux`](../.claude/agents/ux.md) | experiência | tela ou fluxo novo |
| [`ui`](../.claude/agents/ui.md) | interface e tokens | componente ou CSS novo |
| [`mobile`](../.claude/agents/mobile.md) | celular, 375 px, Expo | toda tela |
| [`qa`](../.claude/agents/qa.md) | testes | todo PR |
| [`performance`](../.claude/agents/performance.md) | LCP, bundle, Lighthouse | build, dependência, imagem, tela inicial |
| [`a11y`](../.claude/agents/a11y.md) | WCAG 2.2 AA | toda tela |
| [`privacidade`](../.claude/agents/privacidade.md) | LGPD | formulário, analytics, imagem nova |
| [`pm`](../.claude/agents/pm.md) | produto | abertura de ciclo, issue nova |

## Automação

| Tarefa agendada | Horário | Faz |
|---|---|---|
| `abertura-do-dia-learntech` | 6h30 | Revisão D-1 dos 5 repositórios do learnTECH, relatório no learntech-content e aviso ao orquestrador. Não começa entrega |
| `abertura-do-dia-veb` | 6h30 | Revisão D-1 da VEB pela skill `veb-abertura-do-dia`, diário local e aviso ao orquestrador. Não começa entrega |
| `revisao-d1-github` | 6h30 | Revisão D-1 dos demais repositórios do portfólio, só leitura, com o pacote de merge, e aviso ao orquestrador |
| `abertura-do-dia-lider` | 6h50 | Chama o orquestrador para montar o plano do dia |
| `checkpoint-lider` | 12h30 | Chama o orquestrador para o ponto de controle |
| `fechamento-lider` | 18h30 | Chama o orquestrador para o relatório consolidado |
| `semana-lider` | sexta, 17h | Chama o orquestrador para a revisão da semana |
| `convites-learntech` | 10h | Até 3 convites por dia para a organização da comunidade |

Cada execução pede as permissões do responsável na primeira vez. O prompt de cada tarefa deve citar o `CLAUDE.md` e a skill, e não copiar as regras: a sessão de projeto já tem duas cópias do prompt da abertura.

Situação em 20/11/2026 (inferido pela lista de tarefas do orquestrador · confirmar): nesta máquina existem só `abertura-do-dia-lider` e `fechamento-do-dia-lider`. As revisões D-1 das 6h30, o `checkpoint-lider` e o `semana-lider` ainda são só texto. Criá-las é a F4 da revisão de 20/11 e depende do ok do responsável.

## Ferramentas

- **Linha de comando:** `git`, `gh` (issues, PRs, CI, Project), Node e npm, Python, Playwright.
- **Navegador do app:** abre o site local ou publicado para conferir a tela, o console e a rede. Gera a evidência visual.
- **MCP:** tarefas agendadas, mensagens entre sessões, conectores de documentos (Notion, Drive) quando o responsável liga.
- **Subagentes:** leitura ampla, revisão independente e busca na web, com brief curto e escopo fechado.

## Técnicas de IA em uso

| Técnica | Como usamos | Cuidado |
|---|---|---|
| Várias sessões em paralelo | Uma sessão por mundo de repositórios, coordenadas pelo orquestrador | Cada sessão escreve só nos seus repositórios |
| Mensagens entre sessões | Avisos de início e fim, pedidos de status | Mensagem não é aprovação; não lavar permissão |
| Subagentes com brief | Leitura ampla e revisão sem viés | O brief é todo o contexto: dizer o objetivo, o que já foi descartado e o formato da resposta |
| Revisor independente | Recebe o diff, não a conclusão | Quem conhece a intenção tende a confirmá-la |
| Revisão de fatos | Confere números e datas antes de publicar | Achou 10 erros num roteiro em 12/11/2026 |
| Hook de proteção | Recusa force push, `--no-verify`, push na principal e reescrita de histórico antes de o comando rodar ([`hooks.md`](hooks.md)) | Soma às outras camadas: não vê `gh api`, aliases nem comandos dentro de scripts |
| Escolha do recurso | Do mais simples ao mais caro: própria sessão, subagente, outra sessão ([`recursos.md`](recursos.md)) | Duas sessões com o mesmo pedido duplicam issues: listar as da última hora antes de abrir |
| Tarefas agendadas | Revisão D-1 às 6h30 e plano às 6h50 | Prompt curto, que cita a base; nunca duplicar regras |
| Resumo da conversa | Quando o contexto enche, a sessão segue de um resumo | Estado importante vai para arquivo (relatório, MVP.md, issue), não só para a conversa |
| Evidência por ferramenta | `gh run`, testes, navegador, `curl` | "Atende" sem comando, data e resultado é "Parcial" |
| Limite de espera | Nunca mais de 4 horas parado em CI ou fila | `timeout` em `gh run watch`; refazer em branch nova se travar |
| Modelo por papel | Revisor e orquestrador no modelo mais capaz; varredura no mais barato | Registrar o modelo no relatório quando importar |

## Métricas

| Métrica | Como medir | Onde |
|---|---|---|
| Entregas por dia | issues com evidência no relatório do dia | `dia-AAAA-MM-DD.md` |
| Tempo por entrega | início → fim do aviso | relatório do dia |
| Retrabalho | achados do revisor independente e da revisão de fatos | PR e relatório |
| Critérios de MVP | `X de Y aplicáveis atendidos` | `docs/MVP.md` de cada repositório |
| Bloqueios | permissões negadas e esperas acima de 4 horas | relatório do dia e [`aprendizados.md`](aprendizados.md) |

## Lacunas e próximos passos

1. Ativar as skills e os agentes para todas as sessões (responsável, issue #16).
2. Bloquear force push, push na principal e `--no-verify` na configuração (responsável, issue #17).
3. ~~Subir para o `CLAUDE.md` as regras que hoje estão só na memória da DG mundo.~~ Feito em 14/11/2026 (regras 14 a 16), com o ok do responsável: "Aprovo as 4".
4. Trocar o texto das tarefas agendadas por uma chamada à skill `relatorio-do-dia`.
5. A sessão de projeto (VEB) documenta a sua parte no próprio repositório, com os mesmos papéis e o mesmo formato de aviso.
6. ~~Criar a sessão DG líder com o prompt de [`prompts/dg-lider.md`](prompts/dg-lider.md) (responsável).~~ Feito: a sessão é a "Líder de TODOS".
7. **F2 da revisão de 20/11:** gerar o `CLAUDE.md` na raiz das 4 pastas e um `.claude/` com os agentes, as skills e um `settings.json` com o hook. A arquitetura de IA prepara; instalar é do responsável (R12).
8. **Gabaritos** dos 11 especialistas (20 casos cada) antes de subir qualquer um de AU0.
9. Opção `--somente <repos>` no `scripts/preencher-project.py`, para a sessão dona não depender de `--excluir` com todos os outros.

Decisões que registram esta arquitetura: [`decisoes/2026-11-12-arquitetura-ia.md`](../decisoes/2026-11-12-arquitetura-ia.md), [`decisoes/2026-11-13-orquestrador.md`](../decisoes/2026-11-13-orquestrador.md) e [`decisoes/2026-11-20-governanca-ia.md`](../decisoes/2026-11-20-governanca-ia.md).
