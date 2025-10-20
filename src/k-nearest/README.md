# $k$ mais próximos

Dada uma sequência $v$ ordenada com $n$ números distintos, projete um algoritmo que encontre
os $k$ elementos mais próximos do valor contido em uma posição $x$ (os parâmetros são $v$, $k$ e $x$).
A proximidade entre os números nas posições $i$ e $j$ é calculada como $|a_i - a_j|$. O retorno deverá
ser uma lista contendo os elementos mais próximo do elemento na posição $x$. O algoritmo deverá
apresentar uma complexidade $O(k)$.