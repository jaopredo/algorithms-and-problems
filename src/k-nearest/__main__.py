
def k_nearest(v: list[int], k: int, x: int) -> list[int]:
    """
    Retorna os k elementos mais próximos do valor em v[x], excluindo o próprio v[x].

    Regras:
    - Se k <= 0, retorna [].
    - Se k > n-1, limita para n-1 (não há como escolher mais do que todos os outros).
    - Empate de distância: prefere o elemento à esquerda (índice menor).

    ESPACO DO ALUNO:
    <Descrever aqui informações adicionais>
    """
    n = len(v)

    if k <= 0:
        return []
    if k > n-1:
        k = n-1

    proximos = []

    l = 0
    i = x+1
    j = x-1

    while l != k:
        dist_direita = float('inf')
        dist_esquerda = float('inf')

        if i < n:
            dist_direita = abs(v[x]-v[i])
        if j >= 0:
            dist_esquerda = abs(v[x]-v[j])
        
        if dist_esquerda <= dist_direita:
            proximos.append(v[j])
            j -= 1
        else:
            proximos.append(v[i])
            i += 1
        
        l += 1

    return proximos
