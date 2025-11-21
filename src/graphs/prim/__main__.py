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

    # Lista onde o i-ésimo item é um
    # heap com as arestas do nó i (Ordenadas
    # com base no peso)
    nodes = [None for _ in range(n)]
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

    def update_nodes(i: int):
        """Função que atualiza as informações das arestas minimais
        dentro da minha lista de heaps sobre as arestas de cada nó

        Args:
            i (int): Nó que vou atualizar
        """
        nonlocal criterium  # Pego o critério local
        neighbors = G.neighbors(i)  # Pego os nós que i aponta
        nodes[i] = Heap(criterium)  # Inicio o heap de i
        for node in neighbors:  # Para cada vértice que i aponta (Adajcente)
            weight = G.get_edge_data(i, node)['weight']  # Pego o peso da aresta
            node[i].push((weight, (i, node)))  # Adiciono a aresta e o seu peso no heap
        heap.push(nodes[i][0])  # Adiciono a aresta com menor peso dentro do heap geral

    # Vou fazer esse processo |V|-1 vezes (Pois só posso ter essa quantidade)
    # de arestas
    for i in range(n-1):
        update_nodes(actual)
        while True:
            w, (source, target) = heap[0]
            if not added[target]:
                tree_edges.append((source, target, w))
                break
