from typing import List
import sys
import os
from collections import deque

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

from modules.graphs import GraphAdjacencyList


def problema_5(n: int, m: int, grid: List[List[str]]) -> int:
    """
    Desenvolva um algoritmo com complexidade $O(n^2)$ que retorne
    o menor tempo para escapar.

    Entrada:
    - grid: Uma lista de listas de strings representando a caverna.

    Saída:
    - Retorne o menor tempo para escapar. Se não for possível, retorne -1.
    """
    # Crio o grafo que vai representar o tabuleiro
    G = GraphAdjacencyList()

    possible_moves = [
        (1,0), (-1,0), (0,-1), (0,1)
    ]

    # Adiciono todos os meus vértices
    for _ in range(n*m):
        G.add_node()
    
    water_positions = []
    initial_position = (None, None)
    exit_positions = []
    
    for i in range(n):
        for j in range(m):
            # Pego a numeração do vértice
            v = i * m + j

            if grid[i][j] == 'A':
                water_positions.append((i,j))
            elif grid[i][j] == 'V':
                initial_position = (i, j)
            elif (i == n-1 or i == 0 or j == m-1 or j == 0) and grid[i][j]=='.':
                exit_positions.append((i,j))

            # Vou analisar cada deslocamento possivel
            for di, dj in possible_moves:
                # Pego as coordenadas no tabuleiro
                ni, nj = i + di, j + dj

                # Só adiciono se estiver dentro do tabuleiro
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] != '#':
                    u = ni * m + nj
                    G.add_edge(v, u)
    
    def water_bfs(G: GraphAdjacencyList) -> list[int]:
        nonlocal water_positions
        """Recebe um grafo G e retorna a lista de visita no BFS

        Args:
            G (GraphAdjacencyList): Grafo a ser analisado
            v (int): Vértice que será analisado a distância relativa a todos
            os outros vértices

        Returns:
            list[int]: Lista de distâncias onde list[i] é a distância de
            i para v
        """
        if n == 0:
            raise ValueError("Você passou um grafo vazio")

        distances = [-1 for _ in range(m*n)]
        for i,j in water_positions:
            distances[i*m+j] = 0

        def apply_bfs():
            queue = deque()
            for i, j in water_positions:
                queue.append(i*m + j)
            actual = None

            while queue:
                actual = queue.popleft()
                neighbours = G.get_neighbours(actual)

                for node in neighbours:
                    if distances[node] == -1:
                        distances[node] = distances[actual]+1
                        queue.append(node)
                    else:
                        distances[node] = min(distances[node], distances[actual]+1)
        
        # Só checo para v
        apply_bfs()
        
        return distances

    def bfs_path(G: GraphAdjacencyList, v: int) -> list[int]:
        """Recebe um grafo G e retorna a lista de visita no BFS

        Args:
            G (GraphAdjacencyList): Grafo a ser analisado
            v (int): Vértice que será analisado a distância relativa a todos
            os outros vértices

        Returns:
            list[int]: Lista de distâncias onde list[i] é a distância de
            i para v
        """
        if n == 0:
            raise ValueError("Você passou um grafo vazio")

        distances = [-1 for _ in range(m*n)]
        distances[v] = 0

        def apply_bfs(init_actual):
            actual = init_actual
            queue = deque()
            queue.append(actual)

            while queue:
                actual = queue.popleft()
                neighbours = G.get_neighbours(actual)

                for node in neighbours:
                    if distances[node] == -1:
                        distances[node] = distances[actual]+1
                        queue.append(node)
                    else:
                        distances[node] = min(distances[node], distances[actual]+1)
        
        # Só checo para v
        apply_bfs(v)
        
        return distances

    water_table = water_bfs(G)
    min_water_time_arrivals = [water_table[i*m+j] for i, j in exit_positions]
    
    player_table = bfs_path(G, initial_position[0]*m+initial_position[1])
    min_player_time_arrivals = [player_table[i*m+j] for i, j in exit_positions]

    compatible_times = []

    for i in range(len(min_player_time_arrivals)):
        if min_player_time_arrivals[i] < min_water_time_arrivals[i]:
            compatible_times.append(min_player_time_arrivals[i])
    
    return min(compatible_times) if len(compatible_times) > 0 else -1