# Minimizando Custos de Reparo

A empresa DpC (Divisão para Consertar) opera em estradas contínuas cujo comprimento $L$ é uma potência de 2 (ou seja, $L = 2^n$ para algum $n \geq 0$). O processo de reparo é definido por uma estratégia recursiva, começando pela análise da estrada inteira (um segmento de 1 a $L$).

Para qualquer segmento de estrada sendo analisado, a equipe de engenheiros pode tomar uma de duas decisões:

* **Opção 1: Dividir**
    * Se o comprimento $l$ do segmento atual for 2 ou mais, a equipe pode dividi-lo em duas metades exatas (de comprimento $l/2$ cada).

* **Opção 2: Consertar**
    * A equipe pode consertar o segmento atual de comprimento $l$ de uma só vez. O custo desta ação depende da quantidade de buracos ($N_b$) neste segmento específico:
        * Se $N_b = 0$ (sem buracos), o custo é $C_1$.
        * Se $N_b > 0$ (com buracos), o custo é $C_2 \cdot N_b \cdot l$.

Você foi contratado pela DpC para minimizar os custos da operação. Desenvolva um algoritmo que encontre o custo mínimo para reparar a estrada inteira. O algoritmo deve ter uma complexidade de tempo $O(n \cdot k \log k)$.

## Entrada

* $1 \leq n \leq 30$: O expoente do comprimento da estrada ($L = 2^n$).
* $1 \leq k \leq 10^5$: O número de buracos.
* $1 \leq C_1, C_2 \leq 10^9$: As constantes de custo por unidade de comprimento para reparar um trecho sem buracos, e com buracos, respectivamente.
* $A = [a_1, a_2, \ldots, a_k]$, com $1 \leq a_i \leq 2^n$: Uma lista com as $k$ posições dos buracos.

## Saída

* Retorne um único inteiro: o custo mínimo total para reparar toda a estrada.

## Exemplos

| Entrada | Saída |
|:---:|:---:|
| $n = 2$; $k = 2$; $C_1 = 1$; $C_2 = 2$; $A = [1, 3]$ | 6 |
| $n = 3$; $k = 2$; $C_1 = 1$; $C_2 = 2$; $A = [1, 7]$ | 8 |

### Explicação do primeiro exemplo:

Começamos com o intervalo de pista $[1, 4]$ e podemos consertá-lo com custo $2 \cdot 2 \cdot 4 = 16$.

Ou podemos dividi-lo em $[1, 2]$ e $[3, 4]$.

Para o intervalo $[1, 2]$ podemos consertar com custo $2 \cdot 1 \cdot 2 = 4$, ou dividir em $[1, 1]$ e $[2, 2]$.

O intervalo $[1, 1]$ tem custo 2 e o intervalo $[2, 2]$ custo 1. Então o custo total fica $2 + 1 = 3$, que é menor que o custo de consertar o intervalo $[1, 2]$ sem dividi-lo.

Analogamente, o custo mínimo do intervalo $[3, 4]$ é 3. Dessa forma, o custo mínimo total de conserto é $3 + 3 = 6$.