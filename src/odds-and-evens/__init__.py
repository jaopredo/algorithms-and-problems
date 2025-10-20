
def odds_and_evens(A: list[int]) -> list[int]:
    """
    Desenvolva um algoritmo $O(n)$ que particiona um array $A$ em números pares e ímpares. 
    O algoritmo deve terminar com A contendo todos os seus elementos pares precedendo todos 
    os seus elementos ímpares. A solução deve ser um algoritmo in-place, o que significa que 
    ele pode usar apenas um espaço de memória constante além do próprio $A$. Na prática, 
    isso significa que você não pode usar outro array auxiliar.
    """
    i = 0
    j = -1
    array_size = len(A)

    def swap(A, i, j):
        Ai = A[i]
        A[i] = A[j]
        A[j] = Ai

    for _ in range(array_size):
        if A[i] % 2 == 1 and A[j] % 2 == 0:
            swap(A, i, j)
        
        if A[i+1] == A[j]:
            break
        
        if A[i] % 2 == 0:
            i += 1
        if A[j] % 2 == 1:
            j -= 1

    return A