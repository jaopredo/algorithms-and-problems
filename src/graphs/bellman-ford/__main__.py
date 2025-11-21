import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

import networkx as nx


def bellman_ford(G: nx.DiGraph, v: int) -> list[float]:
    """Aplica o algoritmo de Bellman Ford em um grafo G direcionado
    tendo início no nó v

    Args:
        G (nx.DiGraph): Grafo desejado
        v (int): Nó inicial

    Raises:
        ValueError: Levanta quando o grafo tem ciclos negativos

    Returns:
        list[float]: Vetor de distâncias
    """
    n = len(G)
    distances = [float('inf') for _ in range(n)]
    distances[v] = 0

    edges = G.edges

    for k in range(n):
        for edge in edges:
            i, j = edge
            weight = G.get_edge_data(i, j)['weight']
            if k != n-1:
                distances[j] = min(distances[j], distances[i]+weight)
            elif min(distances[j], distances[i]+weight) != distances[j]:
                raise ValueError('O grafo possui um ciclo negativo')
    
    return distances
