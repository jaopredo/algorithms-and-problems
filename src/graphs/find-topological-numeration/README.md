# Encontrar uma Numeração Topológica em um Grafo 🔢

Dado um grafo dirigido representado por um conjunto de vértices e arestas, o objetivo é **encontrar uma numeração topológica** — isto é, uma ordenação dos vértices que respeite a direção das arestas.

Uma numeração topológica garante que **toda aresta aponta de um vértice com número menor para outro com número maior**.

## Definição

- Um grafo é definido por:  
  $G = (V, E)$  
  onde:
  - $V = \{v_1, v_2, \dots, v_n\}$ é o conjunto de vértices  
  - $E \subseteq V \times V$ é o conjunto de arestas dirigidas  
- Uma **numeração topológica** é uma função:  
  $$
  num: V \rightarrow \{1, 2, \dots, |V|\}
  $$
  que satisfaz, para toda aresta $(u, v) \in E$:
  $$
  num(u) < num(v)
  $$

O objetivo é **encontrar uma ordem topológica** que satisfaça essa condição.

## Observações

- Somente grafos **acíclicos** possuem numerações topológicas.  
- Se houver um ciclo, não existe nenhuma ordenação possível que respeite todas as arestas.

## Exemplo de Execução

Considere o grafo cujas arestas são:

$$
E = \{(0,1), (0,2), (1,3), (2,3)\}
$$

Uma possível numeração topológica é:

- $num(0) = 1$  
- $num(1) = 2$  
- $num(2) = 3$  
- $num(3) = 4$

Ou, como ordem:

$$
[0,\ 1,\ 2,\ 3]
$$

Outras ordens também seriam válidas, como:

$$
[0,\ 2,\ 1,\ 3]
$$

## Exemplos

| Grafo (arestas $u \rightarrow v$) | Possível numeração topológica |
|---|---|
| $\{(0,1),(1,2),(2,3)\}$ | $[0,1,2,3]$ |
| $\{(0,2),(0,1),(1,3),(2,3)\}$ | $[0,1,2,3]$ ou $[0,2,1,3]$ |
| $\{(1,3),(0,2),(2,3)\}$ | $[0,1,2,3]$ ou $[0,2,1,3]$ |
| $\{(0,1),(1,0)\}$ | Não existe (ciclo) |
