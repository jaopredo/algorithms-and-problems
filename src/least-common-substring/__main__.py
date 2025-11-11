import numpy as np


def LCS(A:str,B:str):
    n = len(A)
    m = len(B)

    LCS_cache = np.full((n+1, m+1), -1)
    # Tamanho do LCS dado que eu analisei dado que a string A
    # tinha apenas as i primeiras letras e B tinha apenas as
    # j primeiras letras

    A_LCS_indexes = np.full((n+1, m+1), -1)
    # O índice da última letra da LCS entre a substring das
    # primeiras i letras de A e das primeiras j letras de B na
    # substring das primeiras i letras de A

    B_LCS_indexes = np.full((n+1, m+1), -1)
    # O índice da última letra da LCS entre a substring das
    # primeiras i letras de A e das primeiras j letras de B na
    # substring das primeiras j letras de B

    for i in range(n+1):
        LCS_cache[i, 0] = 0
    for j in range(m+1):
        LCS_cache[0, j] = 0

    for i in range(1, n+1):
        # Dado que eu estou trabalhando com a substring
        # de tamanho i de A (Apenas os i primeiros caracteres)
        C = A[:i]
        for j in range(1, m+1):
            # Dado que eu estou analisando apenas a substring
            # dos primeiros j elementos de B
            D = B[:j]


print(LCS("ABCDAB", "BDCABA"))
