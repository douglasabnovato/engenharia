# 12/11/2026 · Arquitetura de IA documentada, com skills e agentes no repositório

## Contexto

O responsável pediu: "precisamos revisar que esse claude dg mundo esteja com a arquitetura de ai documentada com skills, processos, regras, e mais detalhes de ia avancadas utilizadas". O plano foi aprovado no mesmo dia ("Aprovo os dois").

O levantamento achou:
- regras espalhadas entre o `CLAUDE.md`, a memória de cada sessão e o prompt das tarefas agendadas;
- nenhuma skill nem agente definido;
- `settings.json` sem regras de permissão nem hooks;
- três sessões trabalhando juntas sem papéis escritos.

## Decisões

| # | Decisão | Por quê |
|---|---|---|
| D1 | Um mapa único em [`ia/arquitetura-ia.md`](../ia/arquitetura-ia.md), que cita os outros documentos em vez de copiá-los | Cópias divergem: já existem duas cópias do prompt das 7h |
| D2 | Papéis: **líder**, **sessão de projeto** e **sessão de apoio** | Nomes curtos, iguais nos documentos de todas as sessões |
| D3 | Aviso entre sessões: `<SIGLA> dd/mm: tarefa · início→fim · evidência · quem faz` | Um formato só, que a líder consolida sem reescrever |
| D4 | Skills e agentes versionados neste repositório, em `.claude/` | Versionados, revisados por PR e iguais para todas as sessões |
| D5 | A ativação das skills e dos agentes nas sessões é do responsável | Mexe na configuração do Claude Code da máquina dele |
| D6 | Hooks de proteção são propostos numa issue, e não aplicados pelo agente | Configuração é do responsável (`CLAUDE.md`, regra 7) |
| D7 | Regra que vale para todas as sessões sai da memória e sobe para o `CLAUDE.md` ou para esta base | A memória de uma sessão não é lida pelas outras |

## Opções descartadas

- **Skills na pasta do usuário, sem repositório:** mais rápido, mas sem histórico nem revisão.
- **Um `CLAUDE.md` por sessão:** repete as regras e cria divergência. O `CLAUDE.md` da pasta dos clones continua único.

## Consequências

- Até o responsável ativar, as skills e os agentes servem como documento e como brief. As sessões podem lê-los pelo caminho.
- A sessão de projeto (VEB) documenta a sua parte no próprio repositório, usando D2 e D3.

## Confirmação

Em 12/11/2026 o responsável confirmou D2 (nomes dos papéis) e D3 (formato do aviso): "Confirmo os dois". Valem para todas as sessões.
