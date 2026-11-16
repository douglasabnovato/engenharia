# ADR: registro de decisão de arquitetura

Uma ADR registra uma decisão que alguém poderia desfazer sem saber por que ela existe. No portfólio, uma mudança removeu um acesso de demonstração que era intencional e precisou ser revertida. Com ADR, isso não acontece.

Formato baseado em Nygard (2011), "Documenting Architecture Decisions".

## Quando escrever

- Escolha de pilha ou de hospedagem (a primeira ADR de todo projeto).
- Algo que parece erro mas é intencional (conta de demonstração pública, chave aceita como risco).
- Troca de biblioteca, de banco ou de forma de autenticação.
- Decisão que custa caro para voltar atrás.

## Onde fica

- Projeto pequeno: tabela na seção "ADRs" do `docs/ARQUITETURA.md`.
- Projeto com muitas decisões: um arquivo por ADR em `docs/adr/NNNN-titulo.md`.
- ADR não se apaga. Se mudar, escrever outra e marcar a anterior como "Substituída por ADR-NN".

## Formato completo

```markdown
# ADR-NN · Título curto

- **Data:** AAAA-MM-DD
- **Situação:** proposta | aceita | substituída por ADR-NN

## Contexto
O problema e as forças em jogo. 3 a 5 linhas.

## Decisão
O que foi decidido, em uma ou duas frases.

## Alternativas
- Opção A: por que não.
- Opção B: por que não.

## Consequências
O que fica mais fácil, o que fica mais difícil e o que precisa ser conferido no código.
```

## Formato curto (tabela)

| # | Decisão | Motivo | Alternativa |
|---|---|---|---|
| ADR-01 | Token JWT após login | Identidade assinada, sem mudar a experiência | Senha ou link mágico (decisão do responsável) |
| ADR-02 | Repositórios injetados (Mongo ou memória) | Testar sem banco | ORM direto nos controllers |
| ADR-03 | Validação de data só no servidor | Uma regra para web e mobile | Validar em cada cliente |
| ADR-04 | Uploads em disco com nome aleatório | Simples | Serviço de imagens externo; no Render Free o disco é apagado a cada deploy |

## Exemplos curtos

**Conta de demonstração intencional.** Contexto: o site precisa ser testado por quem visita o portfólio. Decisão: manter contas de teste com senha pública, sem dados reais. Consequência: não remover nem propor troca; a revisão de segurança cita esta ADR.

**Hospedagem da API.** Contexto: API com WebSocket e upload. Decisão: Render (web service) + Atlas M0. Alternativas: funções serverless (não mantêm WebSocket nem disco); VPS (fora da regra de hospedagem gratuita).

**Conferir no código.** Antes de confiar numa ADR, ver se ela foi cumprida. Num repositório, uma ADR mandava remover 547 KB de dados raspados, e o arquivo continuava lá.
