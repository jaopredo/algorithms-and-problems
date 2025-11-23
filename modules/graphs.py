
class GraphAdjacencyMatrix:
    """Class for representing graphs
    """
    def __init__(self):
        # Matriz de adjacência
        self.__adjacency: list[list] = None
    
    def add_node(self, edges_list: list[tuple[int, int]] = None):
        """Appends a node into the graph along with its edges (If specified)

        Args:
            edges_list (list[tuple[int, int]], optional): The list containing tuples like `(source, target)`. Defaults to None.
        """
        if self.__adjacency is None:  # Se eu tenho um grafo nulo
            self.__adjacency= [[0]]  # Insiro apenas um nó
        else:  # Se não
            n = len(self.__adjacency)  # Pego quantos nós eu tenho agora
            for line in self.__adjacency:  # Para cad linha na matriz de adjacência
                line.append(0)  # Eu adiciono um 0 no final da linha
            self.__adjacency.append([0 for _ in range(n+1)])  # E depois adiciono uma linha inteira nova

        if edges_list is not None:  # Se eu tenho as informações das minhas arestas
            for edge in edges_list:  # Eu vou percorrer uma a uma
                # E informar na matriz de adjacência que elas estão interligadas
                self.add_edge(edge[0], edge[1])
    
    def add_edge(self, source: int, target: int):
        """Adds an edge

        Args:
            source (int): Source node
            target (int): Target node
        """
        self.__adjacency[source][target] = 1
        self.__adjacency[target][source] = 1
    
    def remove_edge(self, source: int, target: int):
        """Removes an edge

        Args:
            source (int): Source node
            target (int): Target node
        """
        self.__adjacency[source][target] = 0
        self.__adjacency[target][source] = 0
    
    def __iter__(self):
        return iter(self.__adjacency)
    
    def __len__(self):
        return len(self.__adjacency)
    
    def __getitem__(self, idx):
        if isinstance(idx, tuple):
            return self.__adjacency[idx[0]][idx[1]]
        else:
            return self.__adjacency[idx]
    
    def print_matrix(self):
        """Shows the matrix's in the terminal
        """
        for line in self.__adjacency:
            print(line)

class Node:
    def __init__(self, value, weight):
        self.value = value
        self.next: Node = None
        self.weight = weight

class GraphAdjacencyList:
    """Class for representing graphs
    """
    def __init__(self, weighted = False):
        # Matriz de adjacência
        self.__adjacency: list[Node] = []
        self.weighted = weighted
    
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
            if self.weighted:
                l.append((target.value, target.weight))
            else:
                l.append(target.value)
            target = target.next
        
        return l
    
    def add_edge(self, source: int, target: int, weight: float = 1):
        """Adds an edge

        Args:
            source (int): Source node
            target (int): Target node
        """
        prev = self.__adjacency[source]
        if prev is None:
            self.__adjacency[source] = Node(target, weight)
            return

        node = prev.next

        while node:
            if node.value == target:
                return
            prev = node
            node = node.next
        
        prev.next = Node(target, weight)
    
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