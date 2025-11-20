import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

from modules.graphs import GraphAdjacencyList


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class Queue:
    def __init__(self):
        self.first_node = None
        self.last_node = None
    
    def enqueue(self, v):
        if self.last_node:
            self.last_node.next = Node(v)
            self.last_node = self.last_node.next
        else:
            self.first_node = Node(v)
            self.last_node = self.first_node
    
    def dequeue(self):
        if self.first_node:
            v = self.first_node.value
            self.first_node = self.first_node.next
            return v
        else:
            raise IndexError("Fila vazia")
    
    def is_empty(self):
        return self.first_node is None


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
        nonlocal counter
        actual = init_actual
        queue = Queue()
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
