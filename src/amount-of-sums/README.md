# Quantidade de somas $k$
Dado um inteiro $k$ e uma lista $A$ que contém $n$ inteiros, projete um algoritmo que retorne a quantidade de pares de inteiros em $A$ cuja soma seja $k$.
Mais especificamente, retorne a quantidade de pares $(i, j)$ com $i < j$, tal que
$A_i + A_j = k$.

## Restrições:
- $A_i \le 109$ para todo $1 \le i \le n$
- $k \le 2 \times 10^9$
- $A_i \le A_j \forall 1 \le i \lt j \le n$ nos itens (b) e (c)

## Exemplos

|    Entrada    |     Saída     |
|---------------|---------------|
| $A = [3, 2, 6]$ e $k = 7$ | $0$ |
| $A = [1, 4, 5, 1, 3, 2, 6]$ e $k = 7$ | $4$ |
| $A = [1, 4, 5, 1, 3, 2, 6]$ e $k = 5$ | $3$ |


**(a)** Projete o algoritmo com complexidade de execução $O(n)$
**(b)** Novamente assumindo que $A$ está ordenado, projeto o algoritmo com complexidade
de execução $O(n)$ e complexidade de espaço $O(1)$.
