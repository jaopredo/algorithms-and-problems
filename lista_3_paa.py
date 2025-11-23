import sys
import heapq
from collections import deque
from typing import List, Tuple, Dict, Set

# sys.setrecursionlimit(200010)

##### ATENÇÃO #####
# Não altere o nome deste arquivo.
# Não altere a assinatura das funções.
# Não importe outros módulos além dos já importados.
# Você pode criar outras funções ou classes se julgar necessário, mas deve defini-las no corpo da função do exercicio.

# ==============================================================================
# Problema de exemplo
# ==============================================================================
def problema_0(n: int, m: int, A: List[Tuple[int, int]]) -> int:
    """
    Recebe um grafo com $n$ vertices numerados de $1$ a $n$ e m arestas
    bidirecionadas e retorna o número de componentes conexas do grafo.
    
    Complexidade: O(n + m)
    """

    # Podemos utilizar listas simples, ao invés de dicionários ou conjuntos, para 
    # representar o grafo, já que os vértices são numerados de 1 a n.
    # Isso economiza processamento e memória.
    visited = [False] * (n + 1)
    adj = [[] for _ in range(n + 1)] # lista de adjacência
	
    # Construindo o grafo
    for u, v in A:
        adj[u].append(v)
        adj[v].append(u)

    # No geral, dê preferência a BFS iterativa, pois é mais eficiente que a
    # DFS recursiva (principalmente em Python).
    def bfs(start: int):
        queue = deque([start]) # fila para BFS
        visited[start] = True

        while queue:
            u = queue.popleft() # nó atual

            for v in adj[u]: # vizinhos
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)

    number_of_components = 0
    for u in range(1, n + 1):
        if not visited[u]:
            bfs(u)
            number_of_components += 1

    return number_of_components


# ==============================================================================
# Problema 1 - Sisi e a Sorveteria: Parte 2
# ==============================================================================

def problema_1(n: int, A: List[int]) -> int:
    """
    Desenvolva um algoritmo com complexidade $O(n)$ que encontre a quantidade
    máxima total de sorvete que Sisi pode obter.

    Entrada:
    A entrada consiste em uma lista de $n$ inteiros $A = [a_1, a_2,  dots, a_n]$,
    onde $a_i$ é o estoque do $i$-ésimo sorvete.

    Saída:
    Retorne um único inteiro $Q$, a quantidade máxima total de sorvete
    que Sisi pode obter.
    """
    soma = 0
    max_gain_val = float('inf')
    sequence = []

    # Encontrando o índice da sequência com maior ganho
    for j in range(n-1,-1,-1):
        max_gain_val = min(max_gain_val, A[j])
        soma += max_gain_val
        sequence.append(max_gain_val)
        max_gain_val -= 1
        if max_gain_val < 1:
            break
    
    return soma


# ==============================================================================
# Problema 2 - Minimizando Custos de Reparo
# ==============================================================================

def problema_2(n: int, k: int, C1: int, C2: int, A: List[int]) -> int:
    """
    Desenvolva um algoritmo com complexidade $O(k * log k)$ que encontre o
    custo mínimo para reparar a estrada.

    Entrada:
    - $n$: O expoente do comprimento da estrada ($L = 2^n$).
    - $C1$, $C2$: As constante de custo.
    - $A = [a_1, a_2,  dots, a_k]$: Uma lista com as $k$ posições dos buracos.

    Saída:
    - Retorne um único inteiro: o custo mínimo total para reparar toda a estrada.
    """
    def binary_search(a, x):
        lo, hi = 0, len(a) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if a[mid] == x:
                return mid
            elif a[mid] < x:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    # Lista onde o i-ésimo item indica o índice que a caixa está localizada
    # dentro da lista de tamanho 2^n (0, 2^n-1) representando a estrada. No início, eu sei
    # que cada buraco vai estar localizado na caixinha da sua própria posição
    # global
    boxes = [a - 1 for a in sorted(A.copy())]
    # Lista onde o i-ésimo elemento tem o número de buracos na caixa i
    holes = [1 for _ in range(k)]
    # Lista contendo os custos da caixa onde cada buraco está localizado, ou seja,
    # se holes[i] = x, então costs[i] vai ser o melhor custo obtido ao tomar as
    # decisões corretas na caixinha x
    costs = [C2 for _ in range(k)]

    def compare_costs(b1, b2, i, b1_idx):
        N1 = holes[b1_idx]
        b2_idx = binary_search(boxes, b2)
        if b2_idx == -1:
            N2 = 0
        else:
            N2 = holes[b2_idx]

        l1 = l2 = 2**i

        j = binary_search(boxes, b2)

        min_cost_l1 = costs[b1_idx]
        if b2_idx == -1:
            min_cost_l2 = C1
        else:
            min_cost_l2 = costs[j]
        
        holes[b1_idx] = N1+N2

        if N1 > 0 and N2 > 0:
            return min_cost_l1 + min_cost_l2
        else:
            if N1 == 0 and N2 > 0:
                return min(N2 * (l1 + l2) * C2, min_cost_l1+min_cost_l2)
            elif N2 == 0 and N1 > 0:
                return min(N1 * (l1 + l2) * C2, min_cost_l1+min_cost_l2)
            else:
                return C1

    def aux(B, i):
        """Atualiza a lista de buracos e de custos

        Args:
            H (list[int]): Lista de buracos
            i (int): Iteração atual
        """
        for l, box in enumerate(B):  # Vou percorrer cada caixa e seu índice
            if box%2 == 0:  # Se ele for par, então ela ta na esquerda da caixinha
                l_or_r = 1  # Então eu vou comparar ela e a da direita
            else:  # Se não
                l_or_r = -1  # Eu vou comparar ela e a da esquerda
            # Eu pego o melhor custo entre ela e a caixa que ela vai se unir
            # pra formar a nova caixinha
            cost = compare_costs(box, box+l_or_r, i, l)
            # Seto esse novo custo
            costs[l] = cost

        for j in range(k):
            B[j]//=2
    
    for i in range(n):  # Eu só vou fazer n iterações já que seria log_2(2^n)=n
        # Vou atualizar a lista dos buracos
        aux(boxes, i)
    
    return costs[0]


# ==============================================================================
# Problema 3 - Subsequências radicais
# ==============================================================================

def problema_3(n: int, A: List[int]) -> int:
    """
    Desenvolva um algoritmo com complexidade $O(n * sqrt n)$ que retorne
    a quantidade de subsequências radicais.

    Entrada:
    - $A = [a_1, a_2,  dots, a_n]$ (com $1 <= a_i <= n$).

    Saída:
    - A quantidade total de subsequências radicais, módulo $999999937$.
    """
    # IMPLEMENTAÇÃO LENTA PRIMEIRO

    # O i-ésimo elemento dessa lista representa a quantidade de elementos de
    # A que são divisíveis por i
    L = [1, *(0 for i in range(n))]

    def find_divisors(k):
        divisors = []
        for i in range(1, int(k**0.5)+1):  # O(sqrt(n))
            if k % i == 0:
                if i <= n and k//i <= n and i != k//i:
                    divisors.append(i)
                    divisors.append(k//i)
        return divisors

    for element in A:
        valid_positions = find_divisors(element)  # O(sqrt(n))



# ==============================================================================
# Problema 4 - Cavalo
# ==============================================================================

def problema_4(n: int) -> List[List[int]]:
    """
    Desenvolva um algoritmo com complexidade $O(n^2)$ que retorne
    a matriz de movimentos mínimos.

    Entrada:
    - $n$: O tamanho do lado do tabuleiro ($3   <= n   <= 10^3$).

    Saída:
    - Retorna uma matriz $A$, onde $A[i][j]$ é o número mínimo de
      movimentos para um cavalo ir da posição (i, j) para a posição (0, 0).
    """
    class Node:
        def __init__(self, value):
            self.value = value
            self.next: Node = None
    class GraphAdjacencyList:
        """Class for representing graphs
        """
        def __init__(self):
            # Matriz de adjacência
            self.__adjacency: list[Node] = []
        
        def add_node(self, adjacency_list: list[int] = None):
            """Appends a node into the graph along with its edges (If specified)

            Args:
                edges_list (list[int], optional): List containing the nodes wich the node will connect. Defaults to None.
            """
            n = len(self.__adjacency)
            self.__adjacency.append(None)

            if adjacency_list is not None:
                self.__adjacency[n] = Node(adjacency_list[0])
                for i in range(1,len(adjacency_list)):
                    self.add_edge(n, adjacency_list[i])
        
        def get_neighbours(self, v):
            l = []
            target = self.__adjacency[v]

            while target is not None:
                l.append(target.value)
                target = target.next
            
            return l
        
        def add_edge(self, source: int, target: int):
            """Adds an edge

            Args:
                source (int): Source node
                target (int): Target node
            """
            prev = self.__adjacency[source]
            if prev is None:
                self.__adjacency[source] = Node(target)
                return

            node = prev.next

            while node:
                if node.value == target:
                    return
                prev = node
                node = node.next
            
            prev.next = Node(target)
        
        def remove_edge(self, source: int, target: int):
            """Removes an edge

            Args:
                source (int): Source node
                target (int): Target node
            """
            node1 = self.__adjacency[source]
            node2 = self.__adjacency[target]

            while node1.next:
                if node1.next.value == target:
                    temp = node1.next
                    node1.next = temp.next
                    del temp
                    break
                node1 = node1.next
            while node2.next:
                if node2.next.value == source:
                    temp = node2.next
                    node2.next = temp.next
                    del temp
                    break
                node2 = node2.next
        
        def has_edge(self, source: int, target: int):
            """Checks if a edge exists between two nodes

            Args:
                source (int): _description_
                target (target): _description_
            """
            node = self.__adjacency[source].next
            while node:
                if node.value == target:
                    return True
                node = node.next
            
            node = self.__adjacency[target].next
            while node:
                if node.value == source:
                    return True
                node = node.next
            return False
        
        def __iter__(self):
            return iter(self.__adjacency)
        
        def __len__(self):
            return len(self.__adjacency)
        
        def __getitem__(self, idx):
            return self.__adjacency[idx]

    # Crio o grafo que vai representar o tabuleiro
    G = GraphAdjacencyList()

    possible_moves = [
        (1, 2), (2,1), (2, -1), (1, -2),
        (-1, -2), (-2, -1), (-2, 1), (-1, 2)
    ]

    # Adiciono todos os meus vértices
    for _ in range(n**2):
        G.add_node()
    
    for i in range(n):
        for j in range(n):
            # Pego a numeração do vértice
            v = i * n + j

            # Vou analisar cada deslocamento possivel
            for di, dj in possible_moves:
                # Pego as coordenadas no tabuleiro
                ni, nj = i + di, j + dj

                # Só adiciono se estiver dentro do tabuleiro
                if 0 <= ni < n and 0 <= nj < n:
                    u = ni * n + nj
                    G.add_edge(v, u)
    
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
        n = len(G)

        if n == 0:
            raise ValueError("Você passou um grafo vazio")

        distances = [-1 for _ in range(n)]
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

    distances = bfs_path(G, 0)

    table = [distances[i*n:(i+1)*n] for i in range(n)]

    return table


# ==============================================================================
# Problema 5 - Escape se for possível
# ==============================================================================

def problema_5(n: int, m: int, grid: List[List[str]]) -> int:
    """
    Desenvolva um algoritmo com complexidade $O(n^2)$ que retorne
    o menor tempo para escapar.

    Entrada:
    - grid: Uma lista de listas de strings representando a caverna.

    Saída:
    - Retorne o menor tempo para escapar. Se não for possível, retorne -1.
    """
    pass


# ==============================================================================
# Problema 6 - Viagem Intergalática
# ==============================================================================

def problema_6(n: int, m: int, rotas: List[Tuple[int, int, int]]) -> int:
    """
    Desenvolva um algoritmo com complexidade $O(m  log n)$ que retorne
    o custo mínimo total.

    Entrada:
    - $n$: Número de planetas ($1 <= n <= 10^5$).
    - $m$: Número de rotas ($1 <= m <= 2 * 10^5$).
    - rotas: Lista de $m$ tuplas $(a, b, c)$, onde $a$ é a origem,
      $b$ é o destino e $c$ é o custo.

    Saída:
    - Retorne o menor custo total possível para a viagem.
    """
    pass


# ==============================================================================
# Problema 7 - Reparo das Estradas
# ==============================================================================

def problema_7(n: int, m: int, estradas: List[Tuple[int, int, int]]) -> int:
    """
    Desenvolva um algoritmo com complexidade $O(m  log n)$ que retorne
    o custo mínimo total para conectar as cidades.

    Entrada:
    - $n$: Número de cidades ($1 <= n <= 10^5$).
    - $m$: Número de estradas ($1 <= m <= 2 * 10^5$).
    - estradas: Lista de $m$ tuplas $(a, b, c)$, onde $a$ e $b$ são
      cidades e $c$ é o custo do reparo.

    Saída:
    - Retorne o custo mínimo total para conectar todas as $n$ cidades.
    """
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            rx = self.find(x)
            ry = self.find(y)

            if rx == ry:
                return

            if self.rank[rx] < self.rank[ry]:
                self.parent[rx] = ry
            elif self.rank[rx] > self.rank[ry]:
                self.parent[ry] = rx
            else:
                self.parent[ry] = rx
                self.rank[rx] += 1

    edges = []

    for s, t, w in estradas:
        edges.append((w, s-1, t-1))
    
    edges.sort(key=lambda info: info[0])
    
    components = UnionFind(n)

    total = 0
    added = 0

    for w, source, target in edges:
        if added == n-1:
            break
        source_component = components.find(source)
        target_component = components.find(target)

        if source_component != target_component:
            total += w
            added += 1
            components.union(source, target)

    return total


# ==============================================================================
# Problema 8 - Video Game
# ==============================================================================

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
    class Node:
        def __init__(self, value):
            self.value = value
            self.next: Node = None
    class GraphAdjacencyList:
        """Class for representing graphs
        """
        def __init__(self):
            # Matriz de adjacência
            self.__adjacency: list[Node] = []
        
        def add_node(self, adjacency_list: list[int] = None):
            """Appends a node into the graph along with its edges (If specified)

            Args:
                edges_list (list[int], optional): List containing the nodes wich the node will connect. Defaults to None.
            """
            n = len(self.__adjacency)
            self.__adjacency.append(None)

            if adjacency_list is not None:
                self.__adjacency[n] = Node(adjacency_list[0])
                for i in range(1,len(adjacency_list)):
                    self.add_edge(n, adjacency_list[i])
        
        def get_neighbours(self, v):
            l = []
            target = self.__adjacency[v]

            while target is not None:
                l.append(target.value)
                target = target.next
            
            return l
        
        def add_edge(self, source: int, target: int):
            """Adds an edge

            Args:
                source (int): Source node
                target (int): Target node
            """
            prev = self.__adjacency[source]
            if prev is None:
                self.__adjacency[source] = Node(target)
                return

            node = prev.next

            while node:
                if node.value == target:
                    return
                prev = node
                node = node.next
            
            prev.next = Node(target)
        
        def remove_edge(self, source: int, target: int):
            """Removes an edge

            Args:
                source (int): Source node
                target (int): Target node
            """
            node1 = self.__adjacency[source]
            node2 = self.__adjacency[target]

            while node1.next:
                if node1.next.value == target:
                    temp = node1.next
                    node1.next = temp.next
                    del temp
                    break
                node1 = node1.next
            while node2.next:
                if node2.next.value == source:
                    temp = node2.next
                    node2.next = temp.next
                    del temp
                    break
                node2 = node2.next
        
        def has_edge(self, source: int, target: int):
            """Checks if a edge exists between two nodes

            Args:
                source (int): _description_
                target (target): _description_
            """
            node = self.__adjacency[source].next
            while node:
                if node.value == target:
                    return True
                node = node.next
            
            node = self.__adjacency[target].next
            while node:
                if node.value == source:
                    return True
                node = node.next
            return False
        
        def __iter__(self):
            return iter(self.__adjacency)
        
        def __len__(self):
            return len(self.__adjacency)
        
        def __getitem__(self, idx):
            return self.__adjacency[idx]

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


if __name__ == '__main__':
    # A = [1,2,2]
    # print(problema_3(len(A), A))
    n = 5; m = 7; A = [(1, 3), (3, 4), (1, 2), (2, 5), (1, 4), (4, 5), (3, 5)]
    print(problema_8(n, m, A))
