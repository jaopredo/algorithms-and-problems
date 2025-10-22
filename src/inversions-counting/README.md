# Contagem de Inversões

Você recebeu uma sequência de $n$ números e deve determinar **quantas inversões existem nela**.  
Uma **inversão** ocorre quando dois elementos estão fora de ordem, ou seja, para índices $i < j$, temos $A[i] > A[j]$.

O número total de inversões indica **quão distante a sequência está de estar ordenada**.  
Quanto maior o número de inversões, mais “desordenada” é a sequência.

## Regras

- Dada uma sequência $A = [a_1, a_2, \ldots, a_n]$, uma inversão é um par $(a_i, a_j)$ tal que:
  - $i < j$ e
  - $a_i > a_j$
- O objetivo é **contar todas as inversões** presentes em $A$.
- Um algoritmo ingênuo executa em $O(n^2)$, mas existe uma solução eficiente baseada no **Merge Sort**, que roda em **$O(n \log n)$**.

## Exemplo

Considere a sequência:

$$A = [3, 7, 2, 9, 5]$$

O número total de inversões é **4**, correspondentes aos pares:

$$(7, 2), (3, 2), (9, 5), (7, 5)$$
