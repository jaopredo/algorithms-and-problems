# Sisi e a Sorveteria: Parte 2
Sisi ganhou um cupom que permite pegar uma quantidade “ilimitada” de sorvete, desde que siga algumas regras.  
Na sorveteria existem $n$ sabores de sorvete, e para cada sabor $i$ (de $1$ a $n$) há um estoque $a_i$.

Sisi definirá uma quantidade $q_i$ para pegar de cada sabor $i$, seguindo as seguintes regras:

- **Estoque:**  
  A quantidade de cada sabor não pode exceder o estoque disponível:  
  $0 \leq q_i \leq a_i$.

- **Regra da Sequência:**  
  Ao decidir as quantidades $q_1, q_2, \ldots, q_n$, Sisi deve obedecer a uma regra crescente.  
  Para qualquer sabor $i$ (de $1$ a $n - 1$):
  - Se $q_i = 0$, a quantidade $q_{i+1}$ pode ser qualquer valor (desde que $0 \leq q_{i+1} \leq a_{i+1}$).
  - Se $q_i > 0$, a quantidade $q_{i+1}$ deve ser estritamente maior que $q_i$ (ou seja, $q_{i+1} > q_i$).

Em outras palavras, a sequência de quantidades $q$ deve ser não-decrescente, e assim que incluir um número positivo, ela deve se tornar estritamente crescente a partir dali  
(exemplo: `[0, 0, 2, 5, 8]` é válido, mas `[0, 2, 5, 5]` não é).

Ajude Sisi a maximizar a quantidade total de sorvete  
$Q = \sum_{i=1}^{n} q_i$.  
Desenvolva um algoritmo com complexidade de tempo $O(n)$ que resolva este problema.

## Entrada
A entrada consiste em uma lista de $n$ inteiros  
$A = [a_1, a_2, \ldots, a_n]$, onde $a_i$ é o estoque do $i$-ésimo sabor.

## Saída
Retorne um único inteiro $Q$, a quantidade máxima total de sorvete que Sisi pode obter.

## Restrições
- $1 \leq n \leq 2 \times 10^5$  
- $1 \leq a_i \leq 10^9$ para todo $1 \leq i \leq n$

## Exemplos

| Entrada | Saída |
|----------|--------|
| $n = 5, A = [1, 2, 1, 3, 6]$ | $10$ |
| $n = 5, A = [3, 2, 5, 4, 10]$ | $20$ |
| $n = 4, A = [4, 3, 2, 1]$ | $2$ |
