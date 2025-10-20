# A Biblioteca de Alexandria
A administração da biblioteca busca compreender o padrão de uso de seus frequentadores
e, para isso, precisa identificar o período de pico, ou seja, o intervalo de tempo em que há
o maior número de usuários presentes. A biblioteca dispõe de uma catraca que registra
os horários de entrada e saída de cada pessoa.

Seu desafio é desenvolver um algoritmo com tempo de execução $O(n log (n))$ que resolva
essa questão. O algoritmo deverá receber $n$ pares de inteiros $(a, b)$, onde $a$ representa
o horário de entrada e $b$ o de saída de um usuário. Como resultado, ele deve retornar
$k$, $(u, v)$, onde $k$ é a quantidade máxima de pessoas na biblioteca e $(u, v)$ é o intervalo
de tempo maximal (de maior tamanho) correspondente a esse pico. Se houver mais de
um intervalo de pico maximal, retorne aquele com menor $u$.

## Restrições
- 1 ≤ n ≤ 2 · 105
- 1 ≤ ai < bi ≤ 109 para todo 1 ≤ i ≤ n.
- $a_i \neq a_j$, $a_i \neq b_j$, $b_i \neq b_j$ para todo $1 \le i \lt j \le n$. Ou seja, todos os tempos de
entrada e saída são distintos.

## Exemplos
|    Entrada    |     Saída     |
|---------------|---------------|
| $[(5, 8),(2, 4),(3, 9)]$ | $2,(5, 8)$ |
| $[(5, 8),(2, 6),(3, 9)]$ | $3,(5, 6)$ |
