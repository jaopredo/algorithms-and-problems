# Maior e Menor Elemento em um Array 🔍

Dado um array \( A \) com \( n \) elementos, o objetivo é **encontrar simultaneamente** o **maior** e o **menor** elemento realizando o **menor número possível de comparações**.

## Regras

- Considere um array
  $$
    A = \langle a_1, a_2, \dots, a_n \rangle
  $$
- O problema consiste em identificar:
  - O **maior** valor presente em \( A \).
  - O **menor** valor presente em \( A \).
- O objetivo é executar essa tarefa realizando **menos comparações** do que simplesmente testar cada elemento individualmente contra os candidatos a maior e menor.

Desenvolva um algoritmo que determine **simultaneamente** o maior e o menor elemento de \( A \) usando o menor número possível de comparações.

## Exemplos

| Array \(A\) | Menor | Maior |
|---|---|---|
| \([3, 8, 2, 5, 1, 9]\) | 1 | 9 |
| \([7]\) | 7 | 7 |
| \([-4, 2, 0, 11, -9]\) | -9 | 11 |
