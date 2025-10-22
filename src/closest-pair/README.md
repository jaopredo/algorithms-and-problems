# Problema do Par Mais Próximo (Closest Pair Problem)

## Descrição

**Dado** uma sequência de $n$ pontos em um plano bidimensional (ou seja, um conjunto de coordenadas $(x_i, y_i)$ para $i=1, \dots, n$), **encontre** o par de pontos distintos cuja distância euclidiana entre eles é a menor possível.

## Objetivo

Determinar o valor de:

$$\min_{1 \le i < j \le n} \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}$$

E identificar o par de pontos $(P_i, P_j)$ que realiza esse mínimo.

## Complexidade Algorítmica

O algoritmo ingênuo que calcula a distância entre todos os pares é $O(n^2)$. Seu desafio é projetar um algoritmo mais eficiente, tipicamente utilizando a estratégia de **Divisão e Conquista**, que resolva o problema em $O(n \log n)$.

## Estrutura de Entrada e Saída

| Tipo | Descrição |
|---|---|
| **Entrada** | O número de pontos $n$, seguido por $n$ pares de coordenadas $(x_i, y_i)$. |
| **Saída** | A menor distância euclidiana encontrada. Opcionalmente, o par de pontos que gerou essa distância. |

## Exemplo

| Entrada (Pontos) | Saída (Menor Distância) |
|---|---|
| $(0, 0), (1, 1), (0, 2), (2, 0)$ | $\sqrt{2} \approx 1.414$ (entre $(0, 2)$ e $(1, 1)$, ou $(1, 1)$ e $(2, 0)$, etc.) |
| $(10, 5), (12, 5), (10, 15)$ | $2$ (entre $(10, 5)$ e $(12, 5)$) |