from typing import List

def sisi_and_ice_cream_2(n: int, A: List[int]) -> int:
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
