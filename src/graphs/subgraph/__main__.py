from modules.graphs import GraphAdjacencyList, GraphAdjacencyMatrix

def is_subgraph_adjacency_matrix(G: GraphAdjacencyMatrix, H: GraphAdjacencyMatrix):
    v = len(H)
    
    for i in range(v):
        for j in range(v):
            if H[i,j] == 1 and G[i,j] == 0:
                return False

    return True


def is_subgraph_adjacency_list(G: GraphAdjacencyList, H: GraphAdjacencyList):
    for i, node in enumerate(H):
        node = node.next
        while node:
            if not G.has_edge(i, node.value):
                return False
            node = node.next
    
    return True
