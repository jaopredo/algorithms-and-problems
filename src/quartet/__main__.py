
def quartet(A: list[int], k: int) -> tuple[int,int,int,int]:
    """
    Dado um vetor $A$ com $n$ inteiros e um valor alvo $k$, encontre quatro
    índices distintos cuja soma dos elementos seja igual a $k$.

    O algoritmo deve retornar uma tupla com os quatro índices em ordem
    crescente, $(a, b, c, d)$ com $a<b<c<d$, que satisfaça a condição
    $A_a + A_b + A_c + A_d = k$.

    Caso existam múltiplas soluções, retornar qualquer uma delas é suficiente.
    Se nenhuma combinação válida for encontrada, o algoritmo deve retornar
    (-1, -1, -1, -1).

    O algoritmo deve ter uma complexidade de tempo de $O(n^2 \\log n)$.
    """
    # A lógica é calcular as combinações k - A_i - A_j para todo i < j
    # então eu armazeno isso dentro de uma tupla ou lista, enfim
    # então eu também faço as SOMAS de A_i + A_j para todo i < j
    # de forma que depois eu apenas preciso ordenar ou as somas ou as
    # combinações e aplicar uma busca binária de uma na outra

    # Eu também posso usar hash pra armazenar as diferenças k - A_i - A_j
    # para todo i < j e fazer um outro loop n^2 que passa por todas as combinações
    # A_k + A_l para todo k < l e checar se o negativo da soma delas está presente
    # no hash (Se sim, então quer dizer que existem k - A_i - A_j - A_k - A_l = 0)
    # Ou seja, A_i+A_j+A_k+A_l = k

    # Eu poderia também tentar fazer apenas as somas A_i + A_j
    # e dentro de um loop n^2 eu aplico uma busca binária em A_k + A_l até
    # encontrar algum que seja igual a k
    somas = []
    n = len(A)

    for i in range(n):
        for j in range(i,n):
            somas.append((A[i]+A[j], i, j))

    somas = sorted(somas, key=lambda soma:(soma[0], soma[1], soma[2]))

    indices = None

    for i in range(n):
        for j in range(i,n):
            esquerda = 0
            direita = len(somas)-1
            
            while esquerda <= direita:
                atual = (esquerda + direita)//2

                soma = somas[atual]
                
                if soma[0] + A[i] + A[j] > k:
                    direita = atual - 1
                elif soma[0] + A[i] + A[j] < k:
                    esquerda = atual + 1
                elif len({i, j, soma[1], soma[2]}) == 4:
                    indices = (i+1, j+1, soma[1]+1, soma[2]+1)
                    break
            
            if indices is not None:
                break
        if indices is not None:
            break
    
    if indices is None:
        return (-1,-1,-1,-1)

    indices = sorted(indices)

    return indices
