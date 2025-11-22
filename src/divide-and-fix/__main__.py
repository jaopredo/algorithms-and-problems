
def divide_and_fix(n: int, k: int, C1: int, C2: int, A: list[int]) -> int:
    """
    Desenvolva um algoritmo com complexidade $O(k * log k)$ que encontre o
    custo mínimo para reparar a estrada.

    Entrada:
    - $n$: O expoente do comprimento da estrada ($L = 2^n$).
    - $C1$, $C2$: As constante de custo.
    - $A = [a_1, a_2,  dots, a_k]$: Uma lista com as $k$ posições dos buracos.

    Saída:
    - Retorne um único inteiro: o custo mínimo total para reparar toda a estrada.
    """
    def binary_search(a, x):
        lo, hi = 0, len(a) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if a[mid] == x:
                return mid
            elif a[mid] < x:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    # Lista onde o i-ésimo item indica o índice que a caixa está localizada
    # dentro da lista de tamanho 2^n (0, 2^n-1) representando a estrada. No início, eu sei
    # que cada buraco vai estar localizado na caixinha da sua própria posição
    # global
    boxes = [a - 1 for a in sorted(A.copy())]
    # Lista onde o i-ésimo elemento tem o número de buracos na caixa i
    holes = [1 for _ in range(k)]
    # Lista contendo os custos da caixa onde cada buraco está localizado, ou seja,
    # se holes[i] = x, então costs[i] vai ser o melhor custo obtido ao tomar as
    # decisões corretas na caixinha x
    costs = [C2 for _ in range(k)]

    def compare_costs(b1, b2, i, b1_idx):
        N1 = holes[b1_idx]
        b2_idx = binary_search(boxes, b2)
        if b2_idx == -1:
            N2 = 0
        else:
            N2 = holes[b2_idx]

        l1 = l2 = 2**i

        j = binary_search(boxes, b2)

        min_cost_l1 = costs[b1_idx]
        if b2_idx == -1:
            min_cost_l2 = C1
        else:
            min_cost_l2 = costs[j]
        
        holes[b1_idx] = N1+N2

        if N1 > 0 and N2 > 0:
            return min_cost_l1 + min_cost_l2
        else:
            if N1 == 0 and N2 > 0:
                return min(N2 * (l1 + l2) * C2, min_cost_l1+min_cost_l2)
            elif N2 == 0 and N1 > 0:
                return min(N1 * (l1 + l2) * C2, min_cost_l1+min_cost_l2)
            else:
                return C1

    def aux(B, i):
        """Atualiza a lista de buracos e de custos

        Args:
            H (list[int]): Lista de buracos
            i (int): Iteração atual
        """
        for l, box in enumerate(B):  # Vou percorrer cada caixa e seu índice
            if box%2 == 0:  # Se ele for par, então ela ta na esquerda da caixinha
                l_or_r = 1  # Então eu vou comparar ela e a da direita
            else:  # Se não
                l_or_r = -1  # Eu vou comparar ela e a da esquerda
            # Eu pego o melhor custo entre ela e a caixa que ela vai se unir
            # pra formar a nova caixinha
            cost = compare_costs(box, box+l_or_r, i, l)
            # Seto esse novo custo
            costs[l] = cost

        for j in range(k):
            B[j]//=2
    
    for i in range(n):  # Eu só vou fazer n iterações já que seria log_2(2^n)=n
        # Vou atualizar a lista dos buracos
        aux(boxes, i)
    
    return costs[0]
