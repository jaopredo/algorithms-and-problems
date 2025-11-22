import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

import networkx as nx
from modules.structures import Heap


def prim(G: nx.Graph):
    n = len(G)

    # Lista com as arestas que geram a árvore minimal
    tree_edges = []

    # Meu critério de comparação no heap
    # (Vai ser uma tupla com o peso da aresta
    # e a a aresta em si)
    criterium = lambda i, j: i[0]<j[0]
    # Lista onde i-ésimo item indica se
    # o nó i já foi ou não adicionado
    # dentro da minha árvore minimal
    added = [False for _ in range(n)]
    # Heap com as arestas minimais de cada nó
    heap = Heap(criterium)
    # Vértice que vou iniciar
    actual=0
    # Seto que meu vértice inicial já ta dentro
    # da árvore minimal
    added[actual]=True

    for i in range(n-1):
        neighbors = G.neighbors(actual)
        for node in neighbors:
            # Eu só adiciono no heap se a aresta não levar do nó atual
            # até um já adiconado na árvore (Estou levando em conta que
            # o nó atual JÁ foi adicionado na árvore)
            if not added[node]:
                weight = G.get_edge_data(actual, node)['weight']
                heap.push((weight, (actual, node)))
        _, (source, target) = heap.pop()
        actual = target
        added[actual] = True
        tree_edges.append((source, target))
    
    return tree_edges
