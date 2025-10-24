def hilbert_hotel(estadias: list[tuple[int,int]]) -> tuple[int,list[int]]:
    """
    O Grande Hotel de Hilbert receberá $n$ hóspedes. Para cada hóspede,
    conhecemos um par de inteiros $(a, b)$, que representam seu tempo de
    chegada e de partida, respectivamente. Para minimizar os custos, o
    gerente deseja utilizar o menor número possível de quartos. Duas pessoas
    podem ocupar o mesmo quarto, desde que o período de estadia delas não se
    sobreponha.

    O algoritmo deverá receber $n$ pares de inteiros $(a, b)$ e retornar
    $k, [r_1, r_2, \\dots, r_n]$, onde $k$ é a quantidade mínima de quartos
    necessários e $r_i$ é o quarto que o i-ésimo hóspede (na mesma ordem da
    entrada) deverá utilizar.

    O algoritmo deve ter tempo de execução $O(n \\log n)$.
    """
    def heapify(arr, i):
        n = len(arr)

        menor = i

        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left][0] < arr[menor][1]:
            menor = left
        if right < n and arr[right][0] < arr[menor][1]:
            menor = right
            
        if menor != i:
            arr[i], arr[menor] = arr[menor], arr[i]  # Swap            
            heapify(arr, n, menor)

    def heap_push(heap, elemento):
        n = len(heap)

        heap.append(elemento)

        i = n - 1
        while i > 0:
            pai = (i - 1) // 2
            if heap[i][0] < heap[pai][0]:
                heap[i], heap[pai] = heap[pai], heap[i]  # Swap
                i = pai
            else:
                break

    def heap_pop(heap):
        if not heap:
            return None
        menor = heap[0]
        ultimo = heap.pop()
        if heap:
            heap[0] = ultimo
            heapify(heap, 0)
        return menor
    
    estadias_com_id_original = [(estadia[0], estadia[1], i) for i, estadia in enumerate(estadias)]

    linha_do_tempo = []

    for estadia in estadias_com_id_original:     # O(n)
        # Marcador na linha do tempo tem o seguinte formado:
        # (
        #   Momento no tempo,
        #   Índice de onde o tempo daquela pessoa estava armazenado na lista original
        # )
        linha_do_tempo.append((estadia[0], estadia[2]))
        linha_do_tempo.append((estadia[1], estadia[2]))

    n = len(estadias)
    hospedes = []
    for i in range(n):
        hospedes.append((estadias[i][0], estadias[i][1], i))
    hospedes.sort(key=lambda x: (x[0], x[2]))

    heap = []
    resultado = [0] * n
    min_quartos_utilizados = 1

    for chegada, saida, i in hospedes:
        if heap and heap[0][0] < chegada:
            _, quarto = heap_pop(heap)
        else:
            quarto = min_quartos_utilizados
            min_quartos_utilizados += 1  

        resultado[i] = quarto
        heap_push(heap, (saida, quarto))

    return min_quartos_utilizados - 1, resultado