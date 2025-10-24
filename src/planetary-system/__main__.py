
def planetary_system(A: list[int], k: int) -> int:
    """
    Dado um conjunto de períodos orbitais $A_1, A_2, \\dots, A_n$ e um número
    alvo de voltas $k$, encontre o menor número inteiro de anos, $T$, no qual
    a soma total de órbitas completadas por todos os $n$ planetas do sistema
    seja maior ou igual a $k$.

    A complexidade esperada é de $O(n \\cdot \\log(M))$, onde $M$ é a maior
    resposta possível.
    """
    from math import floor
    M = k * min(A)

    esquerda = 0
    direita = M
    
    while esquerda <= direita:
        atual = (esquerda + direita)//2
        anterior = atual-1

        soma_atual = 0
        soma_anterior = 0

        for a in A:
            soma_atual += floor(atual/a)
            soma_anterior += floor(anterior/a)
        
        if soma_atual >= k and soma_anterior < k:
            return atual
        
        elif soma_atual >= k and soma_anterior >= k:
            direita = atual - 1
        
        elif soma_anterior < k and soma_atual < k:
            esquerda = atual + 1
    
    return atual
