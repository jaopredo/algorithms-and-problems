## Exercício: Implementação do Algoritmo de Prim para MST

O objetivo é **implementar o algoritmo de Prim** para encontrar a **Árvore Geradora Mínima (Minimum Spanning Tree - MST)** de um grafo **não-dirigido, conectado e ponderado**.

---

### Contexto do Grafo

* **Grafo:** $G = (V, E)$, **não-dirigido**, **conectado** e **ponderado**.
* **Restrição:** Os pesos das arestas $w(u, v)$ são tipicamente **não-negativos** e usados para definir a "mínima" da MST.
* **Objetivo:** Encontrar um subconjunto de arestas $E' \subset E$ tal que $G' = (V, E')$ seja uma árvore (conectada e acíclica) e a soma dos pesos das arestas em $E'$ seja a menor possível.

### Estrutura Central

O algoritmo de Prim é um algoritmo **"guloso" (greedy)** que constrói a MST em etapas, crescendo-a a partir de um vértice inicial arbitrário $s$.

#### 1. Crescimento da Árvore

* A MST é construída adicionando, a cada passo, a **aresta de peso mínimo** que conecta um vértice já na árvore a um vértice fora dela.
* O algoritmo mantém o controle de qual é a aresta mais barata que conecta cada nó **fora** da MST à própria MST.

#### 2. Relaxamento e Fila de Prioridades

* A implementação eficiente do Prim utiliza uma **Fila de Prioridades** (Min-Priority Queue) para armazenar os vértices que ainda não estão na MST.
* A chave de prioridade de cada vértice $v$ é o peso da **aresta mais leve** que o conecta a um vértice na MST.

---

## ⏱️ Complexidade do Algoritmo

A complexidade de tempo do algoritmo de Prim depende diretamente da implementação da Fila de Prioridades. Usando uma **Min-Heap de Fibonacci**, a complexidade é:

$$
O(|E| + |V| \log |V|)
$$

Onde:
* $|V|$ é o número de vértices.
* $|E|$ é o número de arestas.