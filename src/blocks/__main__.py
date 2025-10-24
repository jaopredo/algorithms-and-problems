
def the_blocks(blocos: list[int]) -> int:
    """
    Você recebeu $n$ blocos de madeira e seu desafio é empilhá-los, formando
    o menor número possível de torres, seguindo duas regras:
    1. Um bloco só pode ser colocado sobre outro se o seu tamanho for menor ou
       igual ao do bloco inferior.
    2. Os blocos devem ser processados um a um, na sequência predefinida em
       que são apresentados.

    A cada bloco, você deve decidir se o coloca no topo de uma torre existente
    ou se inicia uma nova torre com ele. O algoritmo deve encontrar o número
    mínimo de torres necessárias com complexidade $O(n \\log n)$.
    """
    # Aqui a lógica é montar as torres aos poucos. Eu vou fazer da seguinte forma:
    # eu vou analisar se o meu bloco atual é menor ou igual do que cada um dos
    # blocos no TOPO de cada torre, se ele se encaixar na condição, então eu adiciono
    # o número na lista respectiva da torre (Empilho o meu bloco). Só que se ele é maior
    # eu vou passar pro próximo até encontrar um menor igual. Só que isso daria O(n^2)
    # porém, por construção, se eu tenho duas torres t_i e t_j (i < j) e  os blocos no
    # topo delas são a_k e a_l respectivamente, se a_k = a_l então eu deveria ter empilhado
    # a_l em a_k antes. Ou seja, eu tenho que os blocos no topo vão seguir uma ordem
    # CRESCENTE, perfeito para em vez de percorrer um por um, eu aplicar uma
    # busca binária
    torres = [[blocos[0]]]
    qtd_torres = 1
    n = len(blocos)

    for i in range(n):
        if i == 0:
            continue
        
        atual = None
        esquerda = 0
        direita = qtd_torres-1
        while esquerda <= direita:
            atual = (esquerda + direita)//2
            
            if blocos[i] > torres[atual][-1]:
                esquerda = atual + 1
            elif blocos[i] <= torres[atual][-1]:
                torres[atual].append(blocos[i])
                break
        else:
            torres.append([blocos[i]])
            qtd_torres += 1
    
    return qtd_torres
