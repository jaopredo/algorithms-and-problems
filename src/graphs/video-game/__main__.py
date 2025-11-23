import sys
import os
from typing import List, Tuple

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

from modules.graphs import GraphAdjacencyList

def problema_8(n: int, m: int, transicoes: List[Tuple[int, int]]) -> int:
    """
    Desenvolva um algoritmo com complexidade $O(n + m)$ que encontre o número
    de formas distintas de ir do estado 1 ao estado $n$.

    Entrada:
    - $n$: O número de estados ($1 <= n <= 10^5$).
    - $m$: O número de transições ($1 <= m <= 2 * 10^5$).
    - transicoes: Uma lista com $m$ tuplas $(a, b)$ representando
      transições válidas.

    Saída:
    - Retorne um único inteiro: o número de formas distintas de ir do
      estado 1 ao estado $n$.
    """
    G = GraphAdjacencyList()

    # Montando o grafo
    for _ in range(n):
        G.add_node()
    
    # Adicionando as arestas
    for source, target in transicoes:
        G.add_edge(source-1, target-1)
    
    # Vetor onde o i-pesimo elemento é a quantidade
    # de caminhos até o vértice n-1 saindo do vértice i
    paths = [-1 for _ in range(n)]
    paths[n-1]=1


    def reach_recursive(v):
        # Se eu ja tenho as informações das distâncias a partir do nó atual
        # eu simplesmente retorno essas informações
        if paths[v] != -1:
            return paths[v]
        # do contrário:

        # Pego os vizinhos do nó
        v_neighbours = G.get_neighbours(v)

        # Quantidade de caminhos possíveis até o nó n-1
        # a partir do nó v passado
        total = 0
        
        # E vou fazer o mesmo processo em cada um até checar em 
        for node in v_neighbours:
            total += reach_recursive(node)
        
        paths[v] = total

        return total 


    reach_recursive(0)

    print(paths)

    return paths[0]
