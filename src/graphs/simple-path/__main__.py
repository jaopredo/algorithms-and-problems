import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

from modules.graphs import GraphAdjacencyList, GraphAdjacencyMatrix

def is_simple_path_adjacency_matrix(G: GraphAdjacencyMatrix, P: list[int]) -> bool:
    checkeds = {}
    for v in P:
        if checkeds.get(v) is not None:
            return False
        checkeds[v] = 1

    for i in range(len(P)-1):
        # Checando se a aresta existe
        if G[P[i], P[i+1]] == 0:
            return False
    
    return True


def is_simple_path_adjacency_list(G: GraphAdjacencyList, P: list[int]) -> bool:
    checkeds = {}
    for v in P:
        if checkeds.get(v) is not None:
            return False
        checkeds[v] = 1
    
    for i in range(len(P)-1):
        if not G.has_edge(i, i+1):
            return False
    
    return True
