import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

from modules.graphs import GraphAdjacencyList
from modules.structures import Queue

def bfs_path(G: GraphAdjacencyList, v: int) -> list[int]:
    """Recebe um grafo G e retorna a lista de visita no BFS

    Args:
        G (GraphAdjacencyList): Grafo a ser analisado
        v (int): Vértice que será analisado a distância relativa a todos
        os outros vértices

    Returns:
        list[int]: Lista de distâncias onde list[i] é a distância de
        i para v
    """
    n = len(G)

    if n == 0:
        raise ValueError("Você passou um grafo vazio")

    distances = [-1 for _ in range(n)]
    distances[v] = 0

    def apply_bfs(init_actual):
        actual = init_actual
        queue = Queue(n)
        queue.enqueue(actual)

        while not queue.is_empty():
            actual = queue.dequeue()
            neighbours = G.get_neighbours(actual)

            for node in neighbours:
                if distances[node] == -1:
                    distances[node] = distances[actual]+1
                    queue.enqueue(node)
    
    # Só checo para v
    apply_bfs(v)
    
    return distances



G = GraphAdjacencyList()
for _ in range(10):
    G.add_node()

arestas = [
    # Arestas de 0 (Nó Inicial Verde)
    (0, 1),
    (0, 5),

    # Arestas de 1
    (1, 2),

    # Arestas de 2
    (2, 3),
    (2, 6),

    # Arestas de 3
    (3, 4),
    (3, 8),

    # Arestas de 4
    (4, 9), # Vai para o Nó Final Vermelho

    # Arestas de 5
    (5, 6),

    # Arestas de 6
    (6, 7),
    (6, 8),

    # Arestas de 7
    (7, 8),

    # Arestas de 8
    (8, 9) # Vai para o Nó Final Vermelho

    # Os nós 9 (final) não têm arestas de saída.
]

for aresta in arestas:
    G.add_edge(*aresta)


print(bfs_path(G, 0))
