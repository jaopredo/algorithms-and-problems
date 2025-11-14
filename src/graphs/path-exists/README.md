# Verificação de Existência de Caminho em um Grafo 🧭

Dado um grafo formado por um conjunto de vértices e arestas, o objetivo é determinar se existe um caminho entre dois nós específicos.  
Um caminho é uma sequência de vértices conectados por arestas que permite ir de um nó inicial até um nó final.

## Regras

- Um grafo é definido por:  
  $G = (V, E)$  
  onde:
  - $V = \{v_1, v_2, \dots, v_n\}$ é o conjunto de vértices  
  - $E \subseteq V \times V$ é o conjunto de arestas  
- Dados dois vértices:
  - Origem $s \in V$
  - Destino $t \in V$
- Um caminho de $s$ até $t$ é uma sequência  
  $\langle s = u_1, u_2, \dots, u_k = t \rangle$  
  tal que cada par consecutivo $(u_i, u_{i+1}) \in E$.

O objetivo é determinar se **existe ao menos um caminho** conectando $s$ a $t$.

## Exemplos

| Grafo (arestas $u \rightarrow v$) | Origem $s$ | Destino $t$ | Existe caminho? |
|---|---|---|---|
| $\{(0,1),(1,2),(2,3)\}$ | 0 | 3 | Sim |
| $\{(0,1),(1,2),(3,4)\}$ | 0 | 4 | Não |
| $\{(0,1),(1,3),(0,2),(2,3)\}$ | 0 | 3 | Sim |
| $\{(0,1)\}$ | 0 | 2 | Não |
| $\{(0,1),(1,2),(2,0)\}$ | 0 | 2 | Sim |

### Explicações

- **Exemplo 1:**  
  Arestas: $(0,1),(1,2),(2,3)$  
  Caminho: $0 \rightarrow 1 \rightarrow 2 \rightarrow 3$

- **Exemplo 3:**  
  Arestas: $(0,1),(1,3),(0,2),(2,3)$  
  Caminho: $0 \rightarrow 1 \rightarrow 3$
