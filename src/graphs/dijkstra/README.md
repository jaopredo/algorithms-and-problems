## 💡 Exercício: Implementação do Algoritmo de Dijkstra para Caminho Mínimo

O objetivo é **implementar o algoritmo de Dijkstra** para encontrar o **caminho mais curto** entre um vértice de origem $s$ e todos os outros vértices alcançáveis em um grafo **ponderado** e **dirigido** (ou não-dirigido).

---

### 🗺️ Contexto do Grafo

* **Grafo:** $G = (V, E)$, ponderado.
* **Restrição Principal:** Os pesos das arestas $w(u, v)$ devem ser **não-negativos** ($w(u, v) \ge 0$).
* **Objetivo:** Para um vértice fonte $s$, determinar a distância $d[v]$ (soma mínima dos pesos das arestas) para todos os outros $v \in V$.

### 📚 Estrutura Central

O algoritmo de Dijkstra é tipicamente implementado utilizando uma **Fila de Prioridades** (Min-Priority Queue) para gerenciar eficientemente o conjunto de vértices que ainda não foram finalizados (relaxados).

#### 1. Relaxamento

O passo fundamental é a operação de **Relaxamento** de uma aresta $(u, v)$:

$$
\text{SE } d[u] + w(u, v) < d[v] \text{ ENTÃO:} \\
\quad d[v] = d[u] + w(u, v) \\
\quad \pi[v] = u
$$

#### 2. Ordem de Processamento

Os vértices são processados na ordem crescente de suas distâncias estimadas $d[v]$, garantindo que, quando um vértice é extraído da Fila de Prioridades, sua distância final $d[v]$ é a distância mínima real.

---

## ⏱️ Complexidade do Algoritmo

A complexidade de tempo do algoritmo de Dijkstra depende diretamente da implementação da Fila de Prioridades. Usando uma **Min-Heap de Fibonacci**, a complexidade é:

$$
O(|E| + |V| \log |V|)
$$

Onde:
* $|V|$ é o número de vértices.
* $|E|$ é o número de arestas.