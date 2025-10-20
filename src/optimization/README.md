# Otimização

Dado um vetor $A$ com $n$ inteiros, seu desafio é projetar um algoritmo linear que retorna o menor valor $k$ que minimiza a soma:
$$
\sum_{i=1}^n|A_i − k|
$$

## Restrições
- $1 \le n \le 10^6$
- $|A_i| \le 10^18$ para todo $1 \le i \le n$

## Exemplos
| Entrada | Saída |
|---------|-------|
| $A = [3, 2, 6, 1]$ | $2$ |
| $A = [3, 2, 5, 8, 1, 3, 2, 3]$ | $3$ |
| $A = [33, 10]$ | $10$ |
