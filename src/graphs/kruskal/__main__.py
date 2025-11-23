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
