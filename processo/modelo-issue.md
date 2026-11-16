# Modelo de issue

No portfólio, 117 de 179 issues iniciais foram fechadas como não planejadas: não tinham objetivo nem critério. Toda issue nova segue este modelo.

## Corpo

```markdown
## Objetivo
Uma frase: o que muda para quem usa.

## Motivo
Por que agora. Evidência ou número (medição, defeito, critério do MVP.md).

## Critérios de entrega
- [ ] Verificável por quem não escreveu o código
- [ ] ...
- [ ] (3 a 5)

## Fora desta issue
O que fica para depois.
```

Regras:
- **3 a 5 critérios**, cada um conferível com um comando, uma tela ou um número ("axe sem violações na tela X", "LCP local abaixo de 2,5 s, 3 execuções").
- Issue que depende do responsável: os critérios são o **passo a passo** de como ele faz (onde clicar ou qual comando).
- Sem dados pessoais, contatos ou nomes de terceiros.
- Não duplicar: reaproveitar e completar a issue que já existe.

## Título

Verbo no infinitivo e o resultado: "Publicar a API no Render", "Tratar erro e vazio nas telas logadas", "Proteger a main".

## Rótulos

| Rótulo | Quando |
|---|---|
| `mvp` | Conta para os critérios de MVP |
| tipo (`tipo:funcionalidade`, `tipo:correcao`, `tipo:documentacao`, `tipo:qualidade`, `tipo:infraestrutura`, `tipo:conteudo`) | Sempre um |
| `depende-do-responsavel` | Só o responsável resolve |

Os rótulos podem não existir no repositório: criar antes (`gh label create <nome> --repo <dono>/<repo>`).

## Project

- Adicionar ao Project: `gh project item-add <n> --owner <dono> --url <url-da-issue>`.
- Milestone existente do repositório.
- **Não preencher os campos à mão.** Quem coordena roda o preenchimento em lote no fim de cada lote ([`scripts/preencher-project.py`](../scripts/preencher-project.py)).

Campos que o preenchimento em lote cuida: Status, Tipo, Frente (Estudo, Vitrine, Produto), Prioridade, Tamanho, Pontos, Início, Fim, Depende de, Objetivo, Resultado e Evidência.

## Fechar

- Só com os critérios cumpridos e **evidência** no comentário: PR, run do CI, comando e resultado.
- Se o trabalho está na sprint e ainda não foi para a principal: comentar a evidência e fechar só depois do merge.
- "Não planejada" só com motivo real, escrito no comentário.
- Nunca fechar issue que depende do responsável.
