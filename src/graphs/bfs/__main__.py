import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

from modules.graphs import GraphAdjacencyList
from modules.structures import Queue


def bfs(G: GraphAdjacencyList) -> list[int]:
    """Recebe um grafo G e retorna a lista de visita no BFS

    Args:
        G (GraphAdjacencyList): Grafo a ser analisado

    Returns:
        list[int]: Lista de visitações onde `order[v]` é o momento que
        o vértice v foi visitado
    """
    n = len(G)

    order = [-1 for _ in range(n)]
    counter = 0

    def apply_bfs(init_actual):
        nonlocal counter, n
        actual = init_actual
        queue = Queue(n)
        queue.enqueue(actual)
        order[actual] = counter

        while not queue.is_empty():
            actual = queue.dequeue()
            neighbours = G.get_neighbours(actual)

            for node in neighbours:
                if order[node] == -1:
                    counter += 1
                    order[node] = counter
                    queue.enqueue(node)
    
    for i in range(n):
        if order[i] == -1:
            apply_bfs(i)
    
    return order
