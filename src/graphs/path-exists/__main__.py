import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

from modules.graphs import GraphAdjacencyList


def dfs(G: GraphAdjacencyList, v1: int, v2: int):
    n = len(G)
    visited = [0 for _ in range(n)]

    def reach_recursive(v):
        v_neighbours = G.get_neighbours(v)

        # Se eu ja vizitei o nó atual
        if visited[v]:
            return
        else:
            visited[v] = 1
            for node in v_neighbours:
                reach_recursive(node)

    reach_recursive(v1)

    return bool(visited[v2])


G = GraphAdjacencyList()

for i in range(0,5):
    G.add_node()

edges = [(0,1),(1,2),(3,4)]
for edge in edges:
    G.add_edge(edge[0], edge[1])

print(dfs(G, 1, 4))
