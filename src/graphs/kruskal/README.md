## Exercício: Implementação do Algoritmo de Kruskal para MST

O objetivo é **implementar o algoritmo de Kruskal** para encontrar a **Árvore Geradora Mínima (Minimum Spanning Tree - MST)** de um grafo **não-dirigido, conectado e ponderado**.

---

### Contexto do Grafo

* **Grafo:** $G = (V, E)$, **não-dirigido**, **conectado** e **ponderado**.
* **Restrição:** Os pesos das arestas $w(u, v)$ são usados para definir a "mínima" da MST.
* **Objetivo:** Encontrar um subconjunto de arestas $E' \subset E$ tal que $G' = (V, E')$ seja uma árvore (conectada e acíclica) e a soma dos pesos das arestas em $E'$ seja a menor possível.

### Estrutura Central

O algoritmo de Kruskal é um algoritmo **"guloso" (greedy)** que constrói a MST adicionando arestas em ordem de peso crescente, **desde que não formem um ciclo**.

#### 1. Ordenação e Estrutura Disjunta

* **Ordenação:** Inicialmente, todas as arestas $E$ são **ordenadas** por peso em ordem não-decrescente.
* **Estrutura de Dados:** É essencial utilizar uma estrutura de dados de **Conjuntos Disjuntos (Disjoint Sets)**, frequentemente chamada de Union-Find, para rastrear a qual componente conectado cada vértice pertence.

#### 2. Processamento

O algoritmo percorre as arestas ordenadas:
* Para cada aresta $(u, v)$ de menor peso:
    * Se $u$ e $v$ pertencerem a **conjuntos disjuntos** (ou seja, a aresta não forma um ciclo), a aresta é adicionada à MST, e os conjuntos contendo $u$ e $v$ são **unidos**.
    * Se $u$ e $v$ já estiverem no mesmo conjunto, a aresta é descartada para evitar um ciclo.

---

## Complexidade do Algoritmo

A complexidade de tempo do algoritmo de Kruskal é dominada pela ordenação das arestas e pelas operações de Union-Find.

$$
O(|E| \log |E|) \quad \text{ou} \quad O(|E| \log |V|)
$$

* A ordenação das arestas leva $O(|E| \log |E|)$.
* As operações de Union-Find levam $O(|E| \alpha(|V|))$, onde $\alpha$ é a função inversa de Ackermann, que é quase constante.
* Como $|E| \le |V|^2$, $O(\log |E|)$ é assintoticamente o mesmo que $O(\log |V|)$.