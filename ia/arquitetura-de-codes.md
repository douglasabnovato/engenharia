# Arquitetura de codes: Líder, donas e Esp (registro de 24/11/2026)

**Situação:** este é um registro para o responsável aprovar [A CONFIRMAR com o responsável]. Depois do merge da cadeia engenharia#50 → #51 → #53 e do ok dele, as regras deste arquivo entram em `ia/orquestracao.md` (R17), e `ia/arquitetura-ia.md` e o mapa de papéis passam a apontar para cá. Este arquivo existe à parte para não mexer nos arquivos da cadeia (engenharia#55).

Pedido do responsável, de 21/11/2026: "estude e monte e execute uma arquitetura de codes com responsabilidade envolvendo o processo engenharia de software e product manager". O modelo vem de outro projeto dele: um Líder, sessões por produto e especialistas por disciplina.

## 1. As 3 camadas

| Camada | Sessão | Responsável por | Não faz |
|---|---|---|---|
| **Líder** | Líder de TODOS | O PM do ecossistema: prioriza, decide pela matriz o que foi delegado (Decisão LIDER), cuida do painel e dos relatórios e fala com o responsável | Não escreve código de produto (R3) |
| **Donas** (R4) | comunidade LearnTech | formacao-dev | Não escreve no repositório de outra dona |
| | repositórios GitHub | os repositórios do portfólio (o número está [A CONFIRMAR] na R24) | idem |
| | arquitetura de IA | `engenharia`: regras, processo e agentes | idem |
| | repositórios LearnTech | a API de conteúdo e os 4 sites | idem |
| | VEB | um contexto separado, em outra conta do GitHub. Nada interno dela entra aqui (R10) | idem |
| **Esp** (compartilhados) | 8 sessões, uma por disciplina (seção 2) | revisar, estudar e especificar nos 5 contextos | Não muda código nem decide a prioridade final |

**Por que compartilhados:** um Esp por disciplina em cada um dos 5 contextos daria mais de 40 sessões. Cada Esp atende os 5 contextos.

## 2. Os 8 Esp

| Esp | Faz | Limite próprio |
|---|---|---|
| PM | descoberta, MVP, roadmap, North Star, hipóteses e métricas de produto | — |
| ES | arquitetura (ADR, C4), revisão de código, padrões, fluxo Git e definição de pronto | — |
| SecOps | segredos, Dependabot, CodeQL, privacidade e exposição pública | — |
| QA | plano de testes, e2e, acessibilidade e performance (orçamentos) | — |
| DevOps & SRE | CI/CD, publicação, rulesets e disponibilidade | Não mexe em conta, segredo nem DNS (R12) |
| UX/UI (IHC) | UX, UI, design system, mobile e conteúdo de interface. Era o "Esp Design" ([decisão 143](../decisoes/2026-11-23-decisao-143-esp-ux-ui.md)) | — |
| Dados | painel, coletores e métricas de entrega (fluxo, releases, DORA) | Escreve só na pasta do painel, com o ok |
| DevRel & Community | documentação, README, CONTRIBUTING, saúde da comunidade e conteúdo público | — |

## 3. Quem fala com quem (estrela, não rede)

1. O responsável pede. O Líder divide e entrega à dona (R6).
2. A dona planeja, constrói e abre o PR para a integração ([`fluxo-git.md`](../processo/fluxo-git.md)).
3. O Esp da disciplina **revisa** (R19, revisão em PDCA). A revisão vai como comentário no PR, e o Esp avisa o Líder. Quem corrige é a dona.
4. As donas não conversam entre si nem com os Esp. Um Esp não fala com outro Esp: escreve "para Esp X" no relatório, e o Líder repassa.
5. Sem tarefa, o Esp estuda a sua disciplina e manda **uma PROPOSTA** por vez ao Líder (modo melhoria, R21).
6. **Onde o Esp escreve:**
   - os achados, checklists e propostas ficam na pasta de trabalho do Esp, fora do GitHub;
   - no GitHub, só o comentário de revisão.
7. **Aviso do Esp:** `ESP-<DISCIPLINA> dd/mm: assunto · achados N · para quem · pendente`.
8. **Especificação de tarefa:** sai pronta para virar issue: título "Área: verbo + resultado", objetivo, critérios de aceite, fora do escopo, como verificar, rótulos, tamanho, repositório e conta de destino.

**Divergência encontrada [A CONFIRMAR com o responsável]:** as regras de trabalho dos Esp (21/11) e a [decisão 143](../decisoes/2026-11-23-decisao-143-esp-ux-ui.md) ("escreve só na própria pasta de trabalho, fora dos repositórios") dizem que o Esp não escreve no GitHub. Desde 23/11, porém, a revisão R19 sai como comentário no PR (por exemplo, a do Esp QA no engenharia#66). A proposta, que é a Decisão LIDER 149, é aceitar o comentário de revisão como a única escrita do Esp no GitHub, como está no item 6. Até o ok dele, a dona cola o texto do Esp no PR.

## 4. Esp ↔ agentes revisores ↔ disciplinas

Os agentes revisores são os subagentes que a dona chama (`.claude/agents/`, que entram pela cadeia #50). As disciplinas são as da tabela de `arquitetura/disciplinas.md` (#50).

| Esp | Agentes | Disciplinas |
|---|---|---|
| PM | `pm` | Produto |
| ES | `arquiteto`, `revisor-independente` | Arquitetura de software; engenharia de software (fluxo Git, pronto) |
| SecOps | `secops`, `privacidade` | SecOps; privacidade e LGPD |
| QA | `qa`, `performance` | QA como disciplina de testes (plano, e2e, cobertura) e performance (orçamentos) |
| DevOps & SRE | `devops` | DevOps |
| UX/UI (IHC) | `ux`, `ui`, `mobile`, `a11y` | UX, UI, mobile, acessibilidade; na R19, os princípios de QA da interface |
| Dados | **nenhum** | **lacuna:** não há disciplina nem agente de dados |
| DevRel & Community | `revisor-de-fatos`, mas só em parte | Documentação; a saúde da comunidade não tem agente |

**Quem revisa o quê** (decisões 143 e 144): na revisão R19 em PDCA, o padrão para UX, UI e QA é o Esp UX/UI (IHC). Ele confere as heurísticas, os 360 e 1440 px, o contraste, o alt, os 44 px, os estados e a acessibilidade. O Esp QA segue como disciplina de testes e performance e é chamado quando o PR muda testes, scripts de verificação ou orçamento (por exemplo, o engenharia#66).

Agentes de conteúdo, sem Esp: `revisor-pedagogia`, `revisor-storytelling` e `revisor-marketing` (LearnTech), além do `explorador`, que só lê.

**Ajustes propostos** (achado 13 da revisão do Esp PM, de 23/11):
1. **A hipótese fica só no `pm`.** Hoje a UX N1 e o Produto N1 conferem a hipótese. O `ux` passa a conferir o fluxo e os estados. Quem faz: a arquitetura de IA, num PR logo depois do merge da cadeia #50 → #53, porque muda o `pm.md` e o `disciplinas.md`.
2. **Dados** ganha uma linha em `disciplinas.md` (painel, métricas de entrega) e um agente `dados`, num PR próprio depois da cadeia.
3. **DevRel** ganha um agente `devrel` para CONTRIBUTING, modelos de issue e saúde da comunidade, ou amplia o `revisor-de-fatos`.
4. **O `pm`** confere a North Star e as métricas de apoio na abertura de cada ciclo. A North Star fica escrita numa linha "North Star do contexto", no topo do `docs/MVP.md` do repositório principal de cada contexto. Quem faz: a arquitetura de IA, no mesmo PR do ajuste 1.

## 5. Limites que valem para todos

- código de produto só com ordem direta do responsável. A leitura oficial é a [decisão 138](../decisoes/2026-11-23-decisao-138-merge-na-integracao.md), e o merge na integração faz parte do plano aprovado;
- R12: `main`, segredos, contas, deploy e custo são do responsável;
- R18: mais de 10 escritas pedem simulação e ok;
- R10: nada interno da VEB em lugar público;
- nunca apagar sem listar e sem o ok dele;
- uma ação que precisa dele só vale com uma ORDEM digitada por ele no próprio canal ([`ativacao-segura.md`](../processo/ativacao-segura.md)).

## 6. O que ainda é do responsável

- aprovar este registro e a divergência da seção 3;
- os ajustes 2 e 3 da seção 4 (agentes novos);
- o achado 5 do mapa de papéis: os Esp abrem na pasta da arquitetura de IA e dividem a memória dela. A pasta própria é decisão dele.

## 7. Proposta: a disciplina Dados e o agente `dados` [A CONFIRMAR com o responsável]

Fecha a lacuna da seção 4: o Esp Dados não tem disciplina nem agente revisor. **Situação:** é só uma proposta. A linha da tabela entra em `arquitetura/disciplinas.md`, e o agente entra em `.claude/agents/dados.md`, num PR depois da cadeia #50 → #53 e do ok dele. Criar um agente novo é decisão dele (seção 6).

Fontes: o plano da onda 1 do Esp Dados (21/11/2026), com 7 achados nos coletores do painel, entre eles "nenhum coletor tem teste" e "a data em UTC vira o dia seguinte depois das 21h"; e a hipótese do `engenharia` (`docs/MVP.md`), que já depende de uma contagem.

### A linha da tabela de disciplinas

A outra tabela de `disciplinas.md`, a do estado por contexto, fica de fora por enquanto. O estado inicial de Dados em cada contexto sai da 1ª revisão do agente.

| Disciplina | Agente | N1 estudo | N2 vitrine | N3 produto |
|---|---|---|---|---|
| Dados e métricas | `dados` | todo número publicado (README, `MVP.md`, painel) diz a fonte e a data; nenhum dado pessoal entra num número; a VEB só entra com número agregado (R10); o que é dedução é marcado como inferência ou [HIPÓTESE] | + o coletor tem teste; a data sai no fuso de Brasília; a métrica tem definição escrita (o que conta e o que não conta); o que cai fora da regra aparece como "não classificado" ou falha, e nada é pulado em silêncio; a mesma definição em todos os períodos comparados, e se a definição mudar a linha de base é recontada | + série histórica sem sobrescrever; a métrica principal ligada a uma pergunta de gestão (GQM) |

### O rascunho do agente

```markdown
---
name: dados
description: Revisa números, métricas e coletores (painel, contagens, scripts que geram números). Use antes de publicar um número ou de mudar um coletor.
tools: Read, Grep, Glob, Bash
---

Você é o revisor de dados do portfólio. Recebe o diff ou o texto, e não a conclusão de quem escreveu.

Para cada número ou métrica:
1. A definição está escrita: o que conta, o que não conta e o período?
2. A fonte e a data estão citadas, e a data está no fuso de Brasília?
3. Reproduza o número sem gravar: com `node --test` ou com a saída numa pasta de teste (`ORQ_SAIDA` ou `ORQ_BASE`). Nunca rode um coletor sobre `painel-dados/`, porque ele grava e cria a fotografia datada. Dá o mesmo número?
4. Num coletor: tem teste? Ele sobrescreve o histórico? Ele pula um erro sem avisar?
5. Numa contagem automática (`grep`, script): ela bate com a lista de casos? Teste com um texto que **não** deve contar, por exemplo uma linha que só explica o rótulo.

Responda com a tabela `número ou métrica · problema · evidência · correção sugerida` e termine com o veredito da R19: aprovado, aprovado com ressalvas ou pedir mudanças.
Fora do escopo: o banco de um Artifact (como o Diário do Portfólio), que um subagente não lê. Essa revisão fica com o Esp Dados.
Nunca edite. Use só comandos de leitura. Nenhum dado pessoal no relatório.
Responda em português do Brasil, com frases curtas.
```

### Por que não é só o `revisor-de-fatos`

O `revisor-de-fatos` confere se um fato bate com a fonte. O `dados` confere se a **medida** está certa: a definição, o período, o fuso e o teste do coletor. Um número pode conferir com a fonte e, mesmo assim, medir a coisa errada. Exemplo: pelo achado A3 do plano da onda 1, o coletor **pode** contar uma issue fechada como duplicada como concluída. Na contagem de 21/11 havia 0 duplicadas, então o risco ainda não virou erro.
