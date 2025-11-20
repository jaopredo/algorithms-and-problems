## Problema: Determinar a Presença de Ciclos em um Grafo 🔄

O objetivo é **determinar se um grafo** $G = (V, E)$ **possui pelo menos um ciclo**.

Um ciclo é um caminho no grafo que se inicia e termina no mesmo vértice.

---

## Definição

Um grafo é definido por:
$$
G = (V, E)
$$
onde:
* $V$ é o conjunto de **vértices** (nós).
* $E$ é o conjunto de **arestas** (conexões entre os vértices).

### Ciclo

Um **ciclo** é um caminho $v_0, e_1, v_1, e_2, v_2, \dots, e_k, v_k$ tal que:
* $k \ge 1$ (o ciclo possui pelo menos uma aresta).
* $v_0 = v_k$ (o caminho começa e termina no mesmo vértice).
* Se o grafo for **simples** (sem arestas paralelas), todos os vértices intermediários $v_1, \dots, v_{k-1}$ são distintos, e todas as arestas $e_1, \dots, e_k$ são distintas.

---

## Estruturas de Grafos

| Estrutura | Possibilidade de Ciclos | Característica |
| :--- | :--- | :--- |
| **Grafo Acíclico** | Não possui ciclos | Uma árvore (se for conexo) é um exemplo de grafo acíclico. |
| **Grafo Cíclico** | Possui um ou mais ciclos | Todo grafo que contém um caminho que retorna ao ponto de partida. |

---

## Problema

Dada a representação de um grafo $G$, a tarefa é **desenvolver um método** que retorne:
* **VERDADEIRO** se $G$ contém pelo menos um ciclo.
* **FALSO** se $G$ é acíclico.