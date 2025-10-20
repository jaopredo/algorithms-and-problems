# Sistema Planetário

O famoso astrônomo Typler precisa de sua ajuda para avançar em sua pesquisa sobre
um sistema planetário distante. O problema é o seguinte: encontrar o menor número
inteiro de anos, $T$, no qual a soma total de órbitas completadas por todos os $n$ planetas
do sistema seja maior ou igual a um valor $k$.

Dado um conjunto de períodos orbitais $A_1, A_2, . . . , A_n$ (o tempo que cada planeta leva
para completar uma volta) e um número alvo de voltas $k$, desenvolva um algoritmo que
encontre o valor $T$. A complexidade esperada é de $O(n · log(M))$, onde $M$ é a maior
resposta possível.

## Restrições
- $1 \le A_i \le 10^9$ para todo $1 \le i \le n$
- $1 \le k \le 10^9$
- Consequentemente, $M \le 10^18$

## Exemplos
| Entrada | Saída |
|---------|-------|
| $A = [3, 2, 6] e k = 7$ | $8$ |
| $A = [3, 2, 6, 5, 8, 2, 1] e k = 1234$ | $438$ |