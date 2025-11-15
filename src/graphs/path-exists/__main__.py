import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

from modules.graphs import GraphAdjacencyList


def dfs(G: GraphAdjacencyList) -> list[int]:
    """Recebe um grafo G e retorna a lista de visita do pre-order

    Args:
        G (GraphAdjacencyList): Grafo a ser analisado

    Returns:
        list[int]: Lista de pre-order
    """
    n = len(G)
    visited = [0 for _ in range(n)]

    preorder = [-1 for _ in range(n)]
    visit = 1

    def reach_recursive(v):
        nonlocal visit

        # Se eu ja vizitei o nó atual
        if visited[v]:
            return
        
        v_neighbours = G.get_neighbours(v)

        visited[v] = 1
        preorder[v] = visit
        visit += 1
        for node in v_neighbours:
            reach_recursive(node)

    for i in range(n):
        reach_recursive(i)

    return preorder


G = GraphAdjacencyList()

for i in range(0,5):
    G.add_node()

edges = [(0,1),(1,2),(3,4)]
for edge in edges:
    G.add_edge(edge[0], edge[1])

print(dfs(G))
