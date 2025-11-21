## Exercício: Implementação do Algoritmo de Ford-Fulkerson para Fluxo Máximo

O objetivo é **implementar o algoritmo de Ford-Fulkerson** para encontrar o **Fluxo Máximo** que pode ser enviado de um nó fonte $s$ para um nó sumidouro $t$ em uma rede de fluxo.

---

### Contexto da Rede de Fluxo

* **Rede:** $G = (V, E)$, um grafo **dirigido** com arestas que possuem uma **capacidade** $c(u, v) \ge 0$.
* **Nós Especiais:** Fonte $s$ e Sumidouro $t$.
* **Fluxo $f(u, v)$:** Deve satisfazer as seguintes propriedades:
    1. **Restrição de Capacidade:** $0 \le f(u, v) \le c(u, v)$ para toda aresta $(u, v) \in E$.
    2. **Conservação do Fluxo:** Para todo nó $u \neq s, t$, o fluxo total de entrada é igual ao fluxo total de saída.
* **Objetivo:** Encontrar um fluxo $f$ que maximize o fluxo líquido de $s$ para $t$.

### Estrutura Central

O algoritmo de Ford-Fulkerson utiliza o conceito de **Rede Residual** e **Caminhos Aumentantes**.

#### 1. Rede Residual ($G_f$)

* A rede residual representa a capacidade **restante** para enviar mais fluxo.
* Para cada aresta original $(u, v)$ com fluxo $f(u, v)$, cria-se uma aresta residual:
    * Uma aresta $(u, v)$ com capacidade residual $c_f(u, v) = c(u, v) - f(u, v)$.
    * Uma aresta de retorno $(v, u)$ com capacidade residual $c_f(v, u) = f(u, v)$ (permitindo "desfazer" o fluxo).

#### 2. Caminhos Aumentantes (Augmenting Paths)

* Um **Caminho Aumentante** é um caminho de $s$ para $t$ na **Rede Residual** $G_f$.
* O algoritmo busca repetidamente um caminho aumentante e, ao encontrá-lo, aumenta o fluxo total ao longo desse caminho pela sua **capacidade residual mínima**.

#### 3. Método

O algoritmo continua buscando e aumentando o fluxo até que **nenhum caminho** de $s$ para $t$ possa ser encontrado na Rede Residual $G_f$. Neste ponto, o fluxo total é o máximo.

---

## Relação Fundamental (Teorema Max-Flow Min-Cut)

O valor do fluxo máximo é **igual** à capacidade mínima de qualquer corte $(S, T)$ que separa $s$ de $t$.

$$
\text{Fluxo Máximo} = \text{Capacidade do Corte Mínimo}
$$

## Complexidade do Algoritmo

A complexidade do Ford-Fulkerson depende do método usado para encontrar o caminho aumentante e das capacidades na rede.

$$
O(f_{máx} \cdot |E|)
$$

Onde:
* $f_{máx}$ é o valor do fluxo máximo (pode ser grande).
* $|E|$ é o número de arestas.

**Nota:** Se as capacidades forem inteiras, o algoritmo é garantido de terminar. Para capacidades reais, o método pode não convergir, a menos que se use o algoritmo **Edmonds-Karp** (que usa BFS para encontrar o caminho aumentante, garantindo $O(|V| \cdot |E|^2)$).