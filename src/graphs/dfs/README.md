# Implementação de Busca em Profundidade (DFS) com Preorder e Posorder 🌲

A busca em profundidade (DFS – *Depth-First Search*) é um algoritmo utilizado para explorar todos os vértices e arestas de um grafo, avançando sempre o mais fundo possível antes de retroceder.

O objetivo é **percorrer o grafo** visitando seus vértices em profundidade a partir de um vértice inicial, produzindo duas listas importantes:

- **Preorder:** ordem em que cada vértice é visitado pela primeira vez  
- **Posorder:** ordem em que cada vértice é concluído (quando todos os vizinhos já foram processados)

## Regras

- Um grafo é definido por:  
  $G = (V, E)$  
  onde:
  - $V = \{v_1, v_2, \dots, v_n\}$ é o conjunto de vértices  
  - $E \subseteq V \times V$ é o conjunto de arestas  
- A DFS recebe como entrada:
  - Um grafo $G$
  - Um vértice inicial $s \in V$
- A DFS deve visitar todos os vértices alcançáveis a partir de $s$, seguindo o processo:
  1. Registrar o vértice atual no **preorder**  
  2. Para cada vizinho não visitado, chamar recursivamente a DFS  
  3. Após explorar todos os vizinhos, registrar o vértice no **posorder**

A função retorna **duas listas**:  
- A ordem de visita (*preorder*)  
- A ordem de término (*posorder*)

## Exemplos

| Grafo (arestas $u \rightarrow v$) | Preorder | Posorder |
|---|---|---|
| $\{(0,1),(1,2),(2,3)\}$ | $[0,1,2,3]$ | $[3,2,1,0]$ |
| $\{(0,1),(0,2),(1,3),(2,3)\}$ | $[0,1,3,2]$ | $[3,1,2,0]$ |
| $\{(0,2),(2,1),(1,3)\}$ | $[0,2,1,3]$ | $[3,1,2,0]$ |
| $\{(0,1),(1,0)\}$ | $[0,1]$ | $[1,0]$ |
| $\{(0,2),(0,1)\}$ | $[0,2,1]$ | $[2,1,0]$ |

### Explicações

- **Preorder:**  
  A ordem em que os vértices são descobertos pela DFS.

- **Posorder:**  
  A ordem em que os vértices são finalizados, isto é, quando a chamada recursiva daquele vértice termina.

- **Exemplo 1:**  
  A DFS avança direto até o final, produzindo preorder crescente e posorder decrescente.

- **Exemplo 2:**  
  Depois de visitar $0$, explora-se completamente o subgrafo de $1$ (incluindo $3$), antes de retornar e explorar o ramo que começa em $2$.
