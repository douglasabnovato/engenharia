# Modelo do `docs/ANALISE.md`

O `ANALISE.md` diz o que o sistema deve fazer, o que estava quebrado e como se mediu. É a base para os critérios 3, 6, 9 e 11 do [`padroes.md`](padroes.md).

## 1. Especificação

Um parágrafo: quem usa, para quê, o que acontece no fluxo principal.

| Ator | Canal | Objetivo |
|---|---|---|
| Empresa | Web | Cadastrar e responder pedidos |
| Dev | App | Encontrar e pedir reserva |

### Requisitos funcionais

Cada requisito tem um **critério de aceite** que alguém que não escreveu o código consegue conferir.

| ID | Requisito | Critério de aceite | Estado antes |
|---|---|---|---|
| RF01 | Entrar por e-mail | Sessão com token assinado | ⚠️ id no armazenamento local, sem assinatura |
| RF02 | Cadastrar item | Imagem JPEG/PNG/WebP até 2 MB, campos obrigatórios | ⚠️ aceitava qualquer arquivo |
| RF03 | Buscar | Sem diferenciar maiúsculas | ⚠️ busca exata |
| RF04 | Pedir reserva | Data válida, não passada, sem duplicar | ❌ quebrava |

Legenda: ✅ funciona · ⚠️ funciona com falha · ❌ não funciona.

Requisitos não funcionais entram na mesma tabela com prefixo `RNF` (desempenho, acessibilidade, segurança), com número: "LCP até 2,5 s no celular", "axe sem violações".

## 2. Defeitos

| # | Severidade | Defeito | Referência |
|---|---|---|---|
| D1 | Crítica | Credencial do banco no código | OWASP A02/A07 |
| D2 | Crítica | Identidade sem assinatura: qualquer um age como outro | OWASP A01 |
| D3 | Alta | Rota de reserva quebrada (variável indefinida) | — |
| D4 | Média | Upload sem filtro de tipo e tamanho | OWASP A05 |
| D5 | Média | Contraste abaixo de AA; campo sem rótulo | WCAG 2.2 1.4.3, 1.3.1 |

Severidade:

| Nível | Quando usar |
|---|---|
| Crítica | Vazamento de segredo ou de dado pessoal; alguém age em nome de outro |
| Alta | O fluxo principal quebra |
| Média | Funciona com falha visível, risco moderado ou acessibilidade abaixo de AA |
| Baixa | Cosmético, sem impacto no fluxo |

Cada defeito resolvido aponta o PR e o teste que o cobre.

## 3. Linha de base automatizada

| Verificação | Antes | Depois |
|---|---|---|
| Fluxo principal roda | ❌ | ✅ (teste de ponta a ponta) |
| Testes | 0 | 13 API + 7 web |
| `npm audit --omit=dev` | vários | 0 |
| axe | não executável | 0 violações |

## 4. Limitações da análise

O que não foi possível verificar e por quê (sem banco real, sem aparelho, sem conta). Isso evita um "Atende" sem prova.
