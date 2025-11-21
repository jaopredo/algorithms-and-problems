import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

from modules.graphs import GraphAdjacencyList


def spt_in_topological(G: GraphAdjacencyList):
    """Calcula a menor distância do vértice 0 até os outros nós, assumindo
    que eles estão enumerados de acordo com uma ordem topológica

    Args:
        G (GraphAdjacencyList): O grafo já enumerado topologicamente
    """
    n = len(G)
    # Lista de distâncias de cada vértice até o vértice 0
    distances = [float('inf') for _ in range(n)]
    distances[0] = 0

    for i in range(n):
        neighbours = G.get_neighbours(i)
        for j in neighbours:
            distances[j] = min(distances[j], distances[i]+1)
    
    return distances
