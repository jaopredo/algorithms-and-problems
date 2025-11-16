import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

from modules.graphs import GraphAdjacencyList


def find_topological_numeration(G: GraphAdjacencyList) -> list[int]:
    n = len(G)

    order = [None for _ in range(n)]

    # Declaro uma lista onde a i-ésima entrada é a quantidade
    # de arestas que APONTAM para meu nó
    inDegree = [0 for _ in range(n)]

    # Vou fazer esse cálculo a partir da lista de adjacências
    for i in range(n):
        edge_node = G[i]
        while edge_node:
            inDegree[edge_node.value] += 1
            edge_node = edge_node.next
    
    # Aqui eu declaro uma fila de forma que, de start até end, é onde estão os
    # meus nós com exatamente 0 graus, de forma que vou percorrer um por um
    # adicionando-os à numeração e, se em algum momento, start == end, então é
    # porque não há mais nenhum nó sem grau de entrada
    queue = [0 for _ in range(n)]
    start = 0
    end = 0
    for i in range(n):
        if inDegree[i] == 0:
            queue[end] = i
            end += 1

    counter = 0  # Sempre conta quantos vértices eu analisei
    while start < end:
        # Pego o vértice que vou começar, que é o que possui
        # inDegree = 0
        v = queue[start]
        start += 1
        order[v] = counter
        counter += 1

        edge = G[v]
        while edge:
            inDegree[edge.value] -= 1
            if inDegree[edge.value] == 0:
                queue[end] = edge.value
                end += 1
            edge = edge.next
        
    return order if counter >= n else None
