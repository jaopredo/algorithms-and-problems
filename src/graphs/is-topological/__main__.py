import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

from modules.graphs import GraphAdjacencyList

def is_topological(G: GraphAdjacencyList) -> bool:
    for i, node in enumerate(G):  # Para cada lista de adjacências
        if node is None:  # Checo se ela existe
            continue
        
        actual = node  # Defino o nó atual como o primeiro
        while actual:  # Enquanto eu não chegar no último
            # Se algum nó que ele se conecta tiver numeração maior
            # que ele, retorno falso
            if actual.value < i:
                return False
            actual = actual.next
    
    return True
