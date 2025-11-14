import numpy as np

def LCS(A:str,B:str):
    p = len(A)
    q = len(B)

    LCS_cache = np.full((p+1, q+1), -1)
    # Tamanho do LCS dado que eu analisei dado que a string A
    # tinha apenas as i primeiras letras e B tinha apenas as
    # j primeiras letras

    for i in range(p+1):
        LCS_cache[i, 0] = 0
    for j in range(q+1):
        LCS_cache[0, j] = 0

    for i in range(1, p+1):
        # Dado que eu estou trabalhando com a substring
        # de tamanho i de A (Apenas os i primeiros caracteres)
        for j in range(1, q+1):
            if A[i-1] == B[j-1]:
                LCS_cache[i,j] = LCS_cache[i-1,j-1]+1
            else:
                LCS_cache[i,j] = max(LCS_cache[i-1,j], LCS_cache[i,j-1])
    
    return LCS_cache[p, q]
