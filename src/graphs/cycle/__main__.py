import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

from modules.graphs import GraphAdjacencyList


def is_cycle_in_graph(G: GraphAdjacencyList) -> bool:
    """Recebe um grafo G e retorna `True` se ele possui ciclose `False` se não

    Args:
        G (GraphAdjacencyList): Grafo a ser analisado

    Returns:
        bool: Se possui ou não ciclos
    """
    n = len(G)
    visited = [0 for _ in range(n)]

    preorder = [-1 for _ in range(n)]
    postorder = [-1 for _ in range(n)]

    visit_preorder = 0
    visit_posorder = 0

    def is_return_edge(vi, vj):
        if preorder[vj] == -1 or postorder[vj] != -1:
            return False
        return True

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
            have_return_edge = is_return_edge(v, node)
            if have_return_edge:
                return True
            reach_recursive(node)
        postorder[v] = visit_posorder
        visit_posorder += 1

    for i in range(n):
        have_return_edge = reach_recursive(i)
        if have_return_edge:
            return True

    return False
