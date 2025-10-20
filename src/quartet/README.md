# Quadra

Dado um vetor $A$ com $n$ inteiros e um valor alvo $k$, seu desafio é projetar um algoritmo
que encontre quatro índices distintos cuja soma dos elementos seja igual a $k$.
O algoritmo deve ter uma complexidade de tempo de $O(n^2 log n)$ e retornar uma tupla
com os quatro índices em ordem crescente, $(a, b, c, d)$ com $a \lt b \lt c \lt d$, que satisfaça
a condição $A_a + A_b + A_c + A_d = k$.
Caso existam múltiplas soluções, retornar qualquer uma delas é suficiente. Se nenhuma
combinação válida for encontrada, o algoritmo deve retornar $(−1, −1, −1, −1)$.

## Restrições
- $1 \le n \le 103$
- $1 \le Ai \le 109$ para todo $1 \le i \le n$
- $1 \le k \le 4 · 10^9$

## Exemplos
| Entrada | Saída |
|---------|-------|
| $A = [3, 2, 6, 1]$ e $k = 7$ | $(−1, −1, −1, −1)$ |
| $A = [3, 2, 6, 1]$ e $k = 12$ | $(1, 2, 3, 4)$ |
| $A = [3, 2, 5, 8, 1, 3, 2, 3]$ e $k = 15$ | $(2, 4, 6, 7)$ |
