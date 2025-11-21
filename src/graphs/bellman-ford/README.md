## Exercício: Implementação do Algoritmo de Bellman-Ford

O objetivo é **implementar o algoritmo de Bellman-Ford** para encontrar o **caminho mais curto** entre um vértice de origem $s$ e todos os outros vértices alcançáveis em um grafo **ponderado** que **pode conter pesos de aresta negativos**.

---

### Contexto do Grafo

* **Grafo:** $G = (V, E)$, ponderado.
* **Vantagem Principal:** O algoritmo funciona corretamente mesmo com pesos de aresta **negativos**.
* **Objetivo:** Para um vértice fonte $s$, determinar a distância $d[v]$ (soma mínima dos pesos das arestas) para todos os outros $v \in V$, e **detectar ciclos de peso negativo**.

### Estrutura Central

O algoritmo Bellman-Ford opera relaxando repetidamente todas as arestas do grafo $|V| - 1$ vezes.

#### 1. Relaxamento Repetitivo

O algoritmo itera $|V| - 1$ vezes sobre todas as arestas $(u, v) \in E$, aplicando a operação de **Relaxamento**:

$$
\text{SE } d[u] + w(u, v) < d[v] \text{ ENTÃO:} \\
\quad d[v] = d[u] + w(u, v) \\
\quad \pi[v] = u
$$

Após $|V| - 1$ iterações, se o grafo **não tiver ciclos negativos**, todas as distâncias $d[v]$ serão as distâncias mínimas reais.

#### 2. Detecção de Ciclos Negativos

Uma iteração extra (a $|V|$-ésima) é executada para **verificar a estabilidade**.

* Se, durante a $|V|$-ésima iteração, o relaxamento de **qualquer aresta** $(u, v)$ for bem-sucedido (ou seja, $d[u] + w(u, v) < d[v]$), então **existe um ciclo de peso negativo** acessível a partir da fonte $s$.

---

## ⏱️ Complexidade do Algoritmo

A complexidade de tempo do algoritmo de Bellman-Ford é:

$$
O(|V| \cdot |E|)
$$

Onde:
* $|V|$ é o número de vértices.
* $|E|$ é o número de arestas.