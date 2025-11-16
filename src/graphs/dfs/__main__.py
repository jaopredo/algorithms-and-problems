import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

from modules.graphs import GraphAdjacencyList


def dfs(G: GraphAdjacencyList) -> tuple[list[int], list[int]]:
    """Recebe um grafo G e retorna a lista de visita do pre-order

    Args:
        G (GraphAdjacencyList): Grafo a ser analisado

    Returns:
        tuple[list[int], list[int]]: Lista de pre-order e de pos-order
    """
    n = len(G)
    visited = [0 for _ in range(n)]

    preorder = [-1 for _ in range(n)]
    posorder = [-1 for _ in range(n)]

    visit_preorder = 0
    visit_posorder = 0

    def reach_recursive(v):
        nonlocal visit_preorder, visit_posorder

        # Se eu ja vizitei o nó atual
        if visited[v]:
            return
        
        v_neighbours = G.get_neighbours(v)

        visited[v] = 1
        preorder[v] = visit_preorder
        visit_preorder += 1
        for node in v_neighbours:
            reach_recursive(node)
        posorder[v] = visit_posorder
        visit_posorder += 1

    for i in range(n):
        reach_recursive(i)

    return preorder, posorder


G = GraphAdjacencyList()

G.add_node()
G.add_node()
G.add_node()
G.add_node()
G.add_node()
G.add_node()

edges = [(0,2),(0,1),(1,3),(1,4),(2,4),(4,1),(4,5)]

for edge in edges:
    G.add_edge(*edge)


print(dfs(G))
