from typing import List, Tuple
import heapq
import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

from modules.graphs import GraphAdjacencyList


def min_path_discounted(n: int, m: int, rotas: List[Tuple[int, int, int]]) -> int:
    """
    Desenvolva um algoritmo com complexidade $O(m  log n)$ que retorne
    o custo mínimo total.

    Entrada:
    - $n$: Número de planetas ($1 <= n <= 10^5$).
    - $m$: Número de rotas ($1 <= m <= 2 * 10^5$).
    - rotas: Lista de $m$ tuplas $(a, b, c)$, onde $a$ é a origem,
      $b$ é o destino e $c$ é o custo.

    Saída:
    - Retorne o menor custo total possível para a viagem.
    """

    v = 0

    G = GraphAdjacencyList()
    for _ in range(n):
        G.add_node()
    for c1, c2, w in rotas:
        G.add_edge(c1-1, c2-1, w)
        G.add_edge(c2-1, c1-1, w)

    distances_without = [float('inf') for _ in range(n)]
    distances_with = [float('inf') for _ in range(n)]

    distances_with[v] = 0
    distances_without[v] = 0

    visited_with = [False for _ in range(n)]
    visited_without = [False for _ in range(n)]
    
    # Eu tenho um heap que armazena a estimativa para o nó da segunda posição
    # e a terceira indica se aquela estimativa é já com um cupom aplicado ou
    # sem nenhum cupom aplicado (0 para não tem cupom aplicado e 1 para que
    # tem cumpom aplicado)
    heap = [(0, v, 0)]

    while heap:
        dist, node, has_cupom = heapq.heappop(heap)

        if has_cupom and visited_with[node]:
            continue
        if not has_cupom and visited_without[node]:
            continue

        if has_cupom:
            visited_with[node] = True
        else:
            visited_without[node] = True

        for neigh, w in G.get_neighbours(node):
            if not has_cupom:
                # Aplico o desconto na aresta atual
                new_dist_with_cupom = dist + int(w/2)
                # Não aplico o desconto na aresta
                new_dist_without_cupom = dist + w

                if new_dist_with_cupom < distances_with[neigh]:
                    distances_with[neigh] = new_dist_with_cupom
                    heapq.heappush(heap, (distances_with[neigh], neigh, 1))
                if new_dist_without_cupom < distances_without[neigh]:
                    distances_without[neigh] = new_dist_without_cupom
                    heapq.heappush(heap, (distances_without[neigh], neigh, 0))
            else:
                # Aplico o desconto sem cupom pois estou lidando com
                # uma estimativa com cupom
                new_dist_without_cupom = dist + w

                if new_dist_without_cupom < distances_with[neigh]:
                    distances_with[neigh] = new_dist_without_cupom
                    heapq.heappush(heap, (distances_with[neigh], neigh, 1))

    return distances_with[-1]