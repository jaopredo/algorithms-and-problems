
def sisi_and_ice_cream(sabores: list[int]) -> int:
    """
    Sisi quer saber qual foi o período mais longo, em dias consecutivos, que
    ela passou sem repetir um único sabor de sorvete.

    Você deve desenvolver um algoritmo com tempo de execução $O(n)$ que receba
    a sequência de sabores consumidos e retorne o tamanho da maior
    subsequência contínua de valores distintos.
    """
    sabores_hash = {}  # Hash para armazenar os valores que ja repetiram
    seqs = []
    seq = 0

    for i, sabor in enumerate(sabores):  # Para cada sabor nos sabores
        seq+=1
        
        if sabores_hash.get(sabor) is not None:
            # print(sabor)
            indice_do_repetido = sabores_hash.get(sabor)
            if i == indice_do_repetido:
                seq = 1
            seqs.append(seq-1)
            seq = i - indice_do_repetido
        
        sabores_hash[sabor] = i
    
    seqs.append(seq)

    max_seq = max(seqs)
    
    return max_seq
