from typing import Optional


class TreeNode:
    """
    Classe para representar um nó de uma árvore binária.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def insert(self, value: int):
        if value <= self.val:
            if self.left:
                self.left.insert(value)
            else:
                self.left = TreeNode(value)
        elif value >= self.val:
            if self.right:
                self.right.insert(value)
            else:
                self.right = TreeNode(value)


def minimum_absolute_difference(raiz: Optional[TreeNode]) -> int:
    """
    Dada uma árvore binária de busca (BST) T com $n$ nós contendo inteiros, projete
    um algoritmo que encontre a menor diferença absoluta entre dois nós diferentes 
    da árvore. O algoritmo deve ter complexidade $O(n)$ no pior caso.
    """
    # Inicio minha menor distância como infinito
    menor_distancia = float("inf")

    # Faço o inorder trasversal
    def comparar_in_order(raiz: TreeNode, anterior: int):
        nonlocal menor_distancia
        # Se eu tenho uma subárvore na esquerda
        if raiz.left:
            # Começo a percorrer a subarvore da esquerda
            comparar_in_order(raiz.left, raiz.val)
        
        # Faço a diferença do nó atual com o anterior
        dif = abs(raiz.val - anterior)

        # Se a distância menor encontrada for maior que a atual
        if menor_distancia >= dif:
            # Atulizo a menor distância
            menor_distancia = dif
        
        # Se eu tenho uma subárvore na direita
        if raiz.right:
            # Também vou percorrer essa subárvore
            comparar_in_order(raiz.right, raiz.val)

    comparar_in_order(raiz, menor_distancia)

    return menor_distancia