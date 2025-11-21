import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

import networkx as nx
import numpy as np


def dijkstra(G: nx.DiGraph, v: int):
    n = len(G)

    # Vetor com as distâncias até cada vértice
    distances = [float('inf') for _ in range(n)]
    distances[v] = 0
    # Vetor com booleanos dizendo se um nó já foi
    # ou ainda não foi visitado
    visiteds = [False for _ in range(n)]
    visiteds[v] = True

    actual = v
    while True:
        neighbors = G.neighbors(actual)

        next_node = v
        min_non_visited_weight = float('inf')

        # Atualizo as estimativas dos nós NÃO visitados
        for node in neighbors:
            if not visiteds[node]:
                weight = G.get_edge_data(actual, node)['weight']
                distances[node] = min(distances[node], distances[actual] + weight)
        
        for i in range(n):
            if not visiteds[i] and distances[i] < min_non_visited_weight:
                min_non_visited_weight = distances[i]
                next_node = i
        
        # Agora que sei as novas estimativas mínimas dos nós não visitados,
        # o próximo nó será o com menor estimativa
        actual = next_node
        visiteds[actual] = True

        # Se eu volto pro v, quer dizer que eu não tenho
        # nenhum vértice não visitado acessível, logo
        # não há mais vértices acessíveis a partir de v
        if actual == v:
            break

    return distances
