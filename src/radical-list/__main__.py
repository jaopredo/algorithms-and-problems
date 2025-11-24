
def radical_list(n: int, A: list[int]) -> int:
    """
    Desenvolva um algoritmo com complexidade $O(n * sqrt n)$ que retorne
    a quantidade de subsequências radicais.

    Entrada:
    - $A = [a_1, a_2,  dots, a_n]$ (com $1 <= a_i <= n$).

    Saída:
    - A quantidade total de subsequências radicais, módulo $999999937$.
    """
    MOD = 999999937
    
    D = [0 for _ in range(n+1)]
    D[0] = 1

    def divisores(num: int):
        divs_low = []
        divs_high = []

        r = int(num**.5)
        for i in range(1, r + 1):
            if num % i == 0 and i <= n:
                divs_low.append(i)

                if i != num // i and num//i <= n:
                    divs_high.append(num // i)
        return divs_high + divs_low

    for a in A:
        divs = divisores(a)
        for k in divs:
            D[k] = D[k] + D[k-1]
    
    total_radical_subsequences = sum(D) - 1

    return total_radical_subsequences % MOD
