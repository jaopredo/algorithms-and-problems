# Implementação de Busca em Profundidade (DFS) 🌲

A busca em profundidade (DFS – *Depth-First Search*) é um algoritmo utilizado para explorar todos os vértices e arestas de um grafo, avançando sempre o mais fundo possível antes de retroceder.

O objetivo é **percorrer o grafo** visitando seus vértices em profundidade a partir de um vértice inicial.

## Regras

- Um grafo é definido por:  
  $G = (V, E)$  
  onde:
  - $V = \{v_1, v_2, \dots, v_n\}$ é o conjunto de vértices  
  - $E \subseteq V \times V$ é o conjunto de arestas  
- A DFS recebe como entrada:
  - Um grafo $G$
  - Um vértice inicial $s \in V$
- A DFS deve visitar todos os vértices que são alcançáveis a partir de $s$, seguindo o processo:
  1. Visitar o vértice atual  
  2. Para cada vizinho ainda não visitado, chamar recursivamente a DFS  
  3. Retroceder quando não houver mais vizinhos disponíveis

O algoritmo retorna a **ordem de visita** dos vértices.

## Exemplos

| Grafo (arestas $u \rightarrow v$) | Vértice inicial $s$ | Ordem DFS possível |
|---|---|---|
| $\{(0,1),(1,2),(2,3)\}$ | 0 | $[0, 1, 2, 3]$ |
| $\{(0,1),(0,2),(1,3),(2,3)\}$ | 0 | $[0, 1, 3, 2]$ |
| $\{(1,2),(2,0),(0,3)\}$ | 1 | $[1, 2, 0, 3]$ |
| $\{(0,1),(1,0)\}$ | 0 | $[0, 1]$ |
| $\{(2,0),(2,1)\}$ | 2 | $[2, 0, 1]$ |

### Explicações

- **Exemplo 1:**  
  O percurso segue diretamente até o vértice mais profundo:  
  $0 \rightarrow 1 \rightarrow 2 \rightarrow 3$

- **Exemplo 2:**  
  Após visitar $0$ e $1$, segue para $3$, depois retorna para explorar $2$.
