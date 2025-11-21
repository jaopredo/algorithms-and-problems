import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

from modules.graphs import GraphAdjacencyList


# Função DFS feita no problema do DFS
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


def advance_return_or_crossed(G: GraphAdjacencyList, e: tuple[int, int]) -> str:
    """Recebe um grafo e uma aresta e a classifica como aresta de retorno,

    Args:
        G (GraphAdjacencyList): _description_
        e (tuple[int, int]): _description_

    Returns:
        str: _description_
    """
    preorder, postorder = dfs(G)

    vi = e[0]
    vj = e[1]

    if preorder[vi] < preorder[vj] and postorder[vj] < postorder[vi]:
        return 'advance'
    elif preorder[vi] > preorder[vj] and postorder[vj] > postorder[vi]:
        return 'return'
    else:
        return 'crossed'
