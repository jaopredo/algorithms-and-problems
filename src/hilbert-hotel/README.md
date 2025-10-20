# Hotel de Hilbert
O Grande Hotel de Hilbert está se preparando para sua reinauguração e receberá $n$
hóspedes. Para cada hóspede, conhecemos um par de inteiros $(a, b)$, que representam seu
tempo de chegada e de partida, respectivamente. Para minimizar os custos, o gerente
deseja utilizar o menor número possível de quartos.

Sua tarefa é ajudar o gerente a distribuir os hóspedes nos quartos de forma otimizada.
Duas pessoas podem ocupar o mesmo quarto, desde que o período de estadia delas não
se sobreponha. Ou seja, uma pessoa pode usar um quarto após a outra se o tempo de
saída da primeira for estritamente menor ao tempo de entrada da segunda. Os quartos
são numerados de $1$ a $n$.

Desenvolva um algoritmo com tempo de execução $O(n log n)$ que resolva esse problema. O
algoritmo deverá receber n pares de inteiros $(a, b)$, onde $a$ representa o horário de entrada
e $b$ o de saída de um hóspede. Como resultado, ele deve retornar $k$, $[r_1, r_2, . . . , r_n]$, onde
$k$ é a quantidade mínima de quartos necessários e $r_i$ é o quarto que o $i$-ésimo hóspede
(na mesma ordem da vetor de entrada) deverá utilizar.
Caso exista mais de uma distribuição de quartos válida que utilize o número mínimo $k$,
qualquer uma delas é uma resposta válida.

## Restrições
- $1 \le n \le 2 · 10^5$
- $1 \le a_i \le b_i \le 10^9$ para todo $1 \le i \le n$
- Para a saída: $1 \le ri \le k$ para todo $1 \le i \le n$

## Exemplos

| Entrada | Saída |
|---------|-------|
| $[(1, 2),(3, 3),(4, 5)]$ | $1, [1, 1, 1]$ |
| $[(2, 4),(1, 2),(4, 4)]$ | 2, [1, 2, 2] ou 2, [2, 1, 1] |
| $[(1, 2),(2, 4),(4, 4)]$ | 2, [1, 2, 1] ou 2, [2, 1, 2] |
| $[(1, 4),(1, 2),(2, 4)]$ | 3, [1, 2, 3] ou 3, [*qualquer permutação de 1, 2, 3*] |
