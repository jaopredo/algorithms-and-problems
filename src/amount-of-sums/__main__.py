
def amount_of_sums_A(A: list[int], k: int) -> int:
    """
    Dado um inteiro k e uma lista A que contém n inteiros, projete um algoritmo 
    que retorne a quantidade de pares de inteiros em A cuja soma seja k. 
    Mais especificamente, retorne a quantidade de pares $(i, j)$ com $i<j$, 
    tal que $A_i + A_j = k$

    Projete o algoritmo com complexidade de execução $O(n)$
    """
    auxiliar = {}  # Hash auxiliar para armazenar os valores que foram analisados
    qtd = 0  # O valor que será retornado

    for element in A:  # Para cada elemento em A
        procurar = k - element  # Vejo que elemento deve estar na lista
                                # Para somar na quantidade que será retornada
        
        # Se o elemento que eu tenho que procurar estiver no dicionário
        if procurar in auxiliar:
            # Então eu somo a quantidade de vezes que
            # ele foi observado com a quantidade de
            # combinações possiveis
            qtd += auxiliar[procurar]
        
        # Se o elemento atual for uma chave no dicionário
        if element in auxiliar:
            # Eu somo mais 1 na quantidade de elementos
            # observado
            auxiliar[element] += 1
        else:  # Se não
            # Eu crio a chave com esse elemento
            auxiliar[element] = 1
    
    return qtd


def amount_of_sums_B(A: list[int], k: int) -> int:
    """
    [...]
    Novamente assumindo que A está ordenado, projeto o algoritmo com complexidade 
    de execução $O(n)$ e complexidade de espaço $O(1)$
    """
    i = 0  # Índice de análise direito
    j = len(A)-1  # Índice e análise esquerdo
    qtd = 0  # Quantidade de combinações da soma de k

    # Variáveis de controle para evitar contagens repetidas
    changed_i = False
    changed_j = False
    # Quantas vezes eu analisei um valor repetido
    repeated_i = 1
    repeated_j = 1
    while i < j:
        if A[i] + A[j] < k:
            changed_i = True
            changed_j = False
            i += 1
        elif A[i] + A[j] > k:
            changed_i = False
            changed_j = True
            j -= 1
        else:
            if A[i] != A[j]:
                # Analisando se o elemento anterior é igual ao atual:
                if i > 0 and A[i-1] == A[i] and changed_i:
                    repeated_i += 1
                if j < len(A)-1 and A[j+1] == A[j] and changed_j:
                    repeated_j += 1
        
                if A[i+1]==A[i]:
                    changed_i = True
                    changed_j = False
                    i+=1
                elif A[j-1]==A[j]:
                    changed_j = True
                    changed_i = False
                    j-=1
                else:
                    qtd += repeated_i * repeated_j

                    repeated_j = 1
                    repeated_i = 1

                    changed_i = True
                    changed_j = False
                    i += 1
            else:
                qtd += (j-i+1)*(j-i)//2
                break
    
    return qtd
