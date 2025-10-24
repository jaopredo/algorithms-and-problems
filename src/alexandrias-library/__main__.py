def alexandrias_library(eventos: list[tuple[int,int]]) -> tuple[int, tuple[int, int]]:
    """
    A administração da biblioteca busca compreender o padrão de uso de seus
    frequentadores e, para isso, precisa identificar o período de pico, ou
    seja, o intervalo de tempo em que há o maior número de usuários presentes.

    O algoritmo deverá receber $n$ pares de inteiros $(a, b)$, onde $a$
    representa o horário de entrada e $b$ o de saída de um usuário. Como
    resultado, ele deve retornar $k, (u, v)$, onde $k$ é a quantidade
    máxima de pessoas na biblioteca e $(u, v)$ é o intervalo de tempo
    maximal (de maior tamanho) correspondente a esse pico. Se houver mais
    de um intervalo de pico maximal, retorne aquele com menor $u$.

    O algoritmo deve ter tempo de execução $O(n \\log n)$.
    """
    auxiliar = []
    eventos_sorted = sorted(eventos, key=lambda event: event[0])

    for i, item in enumerate(eventos_sorted):     # O(n)
        auxiliar.append((item[0], i+1))
        auxiliar.append((item[1], i+1))
    
    auxiliar = sorted(auxiliar, key=lambda item: item[0])     # O(nlog(n))

    start_max_time = 0
    end_max_time = None
    max_pessoas = 0
    last_entered = 0
    num_pessoas = 0

    maximais = []

    for item in auxiliar:
        if item[1] > last_entered:
            num_pessoas += 1
            last_entered = item[1]
        else:
            num_pessoas -= 1
        
        if num_pessoas >= max_pessoas:
            max_pessoas = num_pessoas
            start_max_time = item[0]
        elif num_pessoas + 1 == max_pessoas:
            end_max_time = item[0]
            maximais.append((start_max_time, end_max_time, max_pessoas))
    
    
    definitive_maximal = (0,0)
    k = 0

    for maximal in maximais:
        if maximal[2] > k:
            definitive_maximal = (maximal[0], maximal[1])
            k = maximal[2]
        elif maximal[2] == k:
            max_dif = maximal[1] - maximal[0]
            def_max_dif = definitive_maximal[1] - definitive_maximal[0]
            if max_dif > def_max_dif:
                definitive_maximal = (maximal[0], maximal[1])
            elif max_dif == def_max_dif:
                definitive_maximal = min([definitive_maximal, maximal], key=lambda maxim: maxim[0])

    return k, definitive_maximal