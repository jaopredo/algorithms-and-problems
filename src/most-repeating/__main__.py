
def most_repeating(v: list[int]) -> int:
    """
    Encontre o número mais frequente em v.
    Restrição: cada v[i] ∈ {n^2, n^2 + 1, …, n^2 + n}, onde n = len(v).
	Em caso de empate, retorne qualquer um dos valores empatados.
	Retorne None se v estiver vazio.

    ESPACO DO ALUNO:
    <Descrever aqui informações adicionais>
    """
    numeros = {}
    max_num = 0
    respective_num = None

    for num in v:
        if numeros.get(num):
            atual = numeros.get(num) + 1
            
            if atual >= max_num:
                max_num = atual
                respective_num = num
            
            numeros[num] += 1
        else:
            numeros[num] = 1
    
    return respective_num
