---
name: relatorio-do-dia
description: Use para abrir ou fechar o dia de trabalho de uma sessão (líder ou de projeto). Revisa os repositórios, monta o relatório do dia no formato do portfólio e grava no repositório certo.
---

# Relatório do dia

Base: [`ia/arquitetura-ia.md`](../../../ia/arquitetura-ia.md), seção "Protocolo entre sessões".

## 1. Revisar (só leitura)
Para cada repositório do seu mundo, com o `gh`:
- commits das últimas 24 horas na integração e na principal;
- CI das duas branches;
- PRs abertos e issues fechadas nas últimas 24 horas;
- issues abertas de próximos passos;
- o `docs/MVP.md` (`X de Y aplicáveis atendidos`) e o último relatório.

## 2. Montar
Seções, nesta ordem:
- **Entregue desde ontem:** commits, PRs e issues, com links.
- **Estado:** CI e MVP de cada repositório.
- **Riscos e bloqueios:** CI vermelha, PR parado, site fora do ar, espera acima de 4 horas.
- **Plano de hoje:** de 3 a 5 entregas. Cada uma ligada a uma issue e com o início previsto.
- **Equipe:** uma tabela por sessão, com tarefa, início→fim e evidência.
- **Com o responsável:** o que só ele resolve, o mais importante primeiro.

## 3. Gravar
- Use um clone temporário, com `git clone -c core.longpaths=true`. Nunca use os clones de uso diário.
- Crie `feature/AAAA-MM-DD`, faça o commit `docs: relatório do dia AAAA-MM-DD` e o push.
- Com a CI verde, faça o `--ff-only` para a integração, ou o PR para a sprint, conforme o repositório.

## 4. Avisar
- Mostre o plano no chat do responsável.
- Mande o aviso de início às outras sessões, com a skill `aviso-entre-sessoes`.
- No fim do dia, acrescente as horas reais de cada tarefa.
