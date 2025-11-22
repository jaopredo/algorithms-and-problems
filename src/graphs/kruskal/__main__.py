import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

import networkx as nx
from modules.structures import UnionFind


def kruskal(G: nx.Graph):
    n = len(G)

    # Lista com as arestas que geram a árvore minimal
    tree_edges = []

    edges = []

    for edge in G.edges:
        weight = G.get_edge_data(*edge)['weight']
        edges.append((weight, edge))
    
    edges.sort(key=lambda info: info[0])
    
    components = UnionFind(n)

    for _, (source, target) in edges:
        if len(tree_edges) == n-1:
            break
        source_component = components.find(source)
        target_component = components.find(target)

        if source_component != target_component:
            tree_edges.append((source, target))
            components.union(source, target)

    return tree_edges


G = nx.Graph()

edges = [
    (0, 1, 2),   # A-B
    (0, 3, 3),   # A-D
    (0, 2, 3),   # A-C
    (1, 2, 4),   # B-C
    (1, 4, 3),   # B-E
    (2, 3, 5),   # C-D
    (2, 4, 1),   # C-E
    (3, 5, 7),   # D-F
    (5, 6, 9),   # F-G
    (5, 4, 8),   # F-E
]

for u, v, w in edges:
    G.add_edge(u, v, weight=w)

print(kruskal(G))
