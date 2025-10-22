# Problema da Mochila 0/1 (Knapsack Problem)

## Descrição

Dado um conjunto de $n$ itens, onde cada item $i$ possui um peso $w_i$ e um valor $v_i$, e uma mochila com uma capacidade máxima de peso $W$.

O objetivo é selecionar um **subconjunto** de itens $S \subseteq I$ para colocar na mochila tal que:

1.  A soma dos pesos dos itens selecionados não exceda a capacidade da mochila ($W$):
    $$\sum_{i \in S} w_i \leq W$$
2.  A soma total dos valores dos itens selecionados seja maximizada:
    $$\max \sum_{i \in S} v_i$$

**Restrição 0/1:** Para cada item, a decisão é binária: ele é **incluído** na mochila (1) ou **excluído** (0). Não é permitido incluir frações de itens.

## Formalização

Encontrar $x_i \in \{0, 1\}$ para cada item $i \in \{1, 2, \dots, n\}$ que:

$$\text{Maximiza: } \sum_{i=1}^{n} v_i x_i$$
$$\text{Sujeito a: } \sum_{i=1}^{n} w_i x_i \leq W$$

## Exemplo

Considere a seguinte tabela de itens e uma capacidade de mochila $W = 11$:

| Item | Peso ($w_i$) | Valor ($v_i$) |
|:----:|:------------:|:-------------:|
| 1    | 1            | 1             |
| 2    | 2            | 6             |
| 3    | 5            | 18            |
| 4    | 6            | 22            |
| 5    | 7            | 28            |

| Escolha | Peso Total | Valor Total | Cabe na Mochila? |
|:-------:|:----------:|:-----------:|:----------------:|
| $\{1, 2, 4\}$ | 9 | 29 | Sim |
| $\{3, 5\}$ | 12 | 46 | Não |
| **Solução Ótima** | **11** | **37** (Itens: $\{3, 4\}$) | **Sim** |