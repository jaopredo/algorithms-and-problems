# Implementação de Busca em Largura (BFS) 🌐

A busca em largura (BFS – *Breadth-First Search*) é um algoritmo utilizado para explorar todos os vértices e arestas de um grafo por **camadas**, visitando primeiro todos os vértices a uma certa distância do vértice inicial antes de avançar para a próxima camada.

O objetivo é **percorrer o grafo** visitando seus vértices em níveis crescentes a partir de um vértice inicial, produzindo:

- **Níveis (ou distâncias):** distância mínima em número de arestas do vértice inicial até cada vértice
- **Ordem de visita:** ordem em que os vértices são retirados da fila e processados

## Regras

- Um grafo é definido por:  
  $G = (V, E)$  
  onde:
  - $V = \{v_1, v_2, \dots, v_n\}$ é o conjunto de vértices  
  - $E \subseteq V \times V$ é o conjunto de arestas  
- A BFS recebe como entrada:
  - Um grafo $G$
  - Um vértice inicial $s \in V$
- A BFS deve visitar os vértices na ordem em que são alcançados, seguindo o processo:
  1. Inserir o vértice inicial na fila  
  2. Repetir até a fila esvaziar:  
     - Remover o primeiro vértice da fila  
     - Visitar todos os vizinhos não visitados  
     - Inserir os vizinhos na fila em ordem de descoberta  

A função deve retornar:
- A ordem de visita dos vértices
- A lista de níveis de cada vértice (distâncias)

## Exemplos

| Grafo (arestas $u \rightarrow v$) | Ordem BFS a partir de 0 | Níveis |
|---|---|---|
| $\{(0,1),(1,2),(2,3)\}$ | $[0,1,2,3]$ | $[0,1,2,3]$ |
| $\{(0,1),(0,2),(1,3),(2,3)\}$ | $[0,1,2,3]$ | $[0,1,1,2]$ |
| $\{(0,2),(2,1),(1,3)\}$ | $[0,2,1,3]$ | $[0,1,2,3]$ |
| $\{(0,1),(1,0)\}$ | $[0,1]$ | $[0,1]$ |
| $\{(0,2),(0,1)\}$ | $[0,2,1]$ | $[0,1,1]$ |

### Explicações

- **Ordem BFS:**  
  Sequência dos vértices conforme saem da fila.

- **Níveis:**  
  Distância mínima (em número de arestas) do vértice inicial até cada vértice.

- **Exemplo 1:**  
  O grafo é uma cadeia simples, então a BFS avança camada por camada na ordem natural.

- **Exemplo 2:**  
  A BFS primeiro visita $1$ e $2$ (mesmo nível), depois $3$.
