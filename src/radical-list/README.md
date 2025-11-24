# Subsequências radiciais

Pedrinho adora brincar com **sequências de números inteiros**. Recentemente, ele está com seu foco voltado para as **sequências radiciais**:

Uma sequência $A = [a_1, a_2, \dots, a_k]$ de $k$ inteiros é dita **radical** se, para todo índice $i$ (de $1$ a $k$), o $i$-ésimo elemento $a_i$ é **divisível por $i$**.

Ele gosta tanto dessas sequências que criou um jogo:

* Primeiro, ele escreve uma sequência $A = [a_1, a_2, \dots, a_n]$ em seu quadro.
* Depois, ele mentalmente lista todas as **subsequências** de $A$. (Uma subsequência é formada removendo zero ou mais elementos de $A$, mantendo a ordem relativa dos demais).
* Finalmente, ele conta quantas dessas subsequências são **radicais**.

Por exemplo, se $A = [1, 2, 2]$, as subsequências radicais são:

* $[1]$, pois $1|1$.
* $[2]$, utilizando o primeiro $2$ de $A$, pois $1|2$.
* $[2]$, utilizando o segundo $2$ de $A$, pois $1|2$.
* $[1, 2]$, utilizando o primeiro $2$ de $A$, pois $1|1$ e $2|2$.
* $[1, 2]$, utilizando o segundo $2$ de $A$, pois $1|1$ e $2|2$.
* $[2, 2]$, utilizando o primeiro e o segundo $2$, pois $1|2$ e $2|2$.

A subsequência $[1, 2, 2]$ não é radical, pois o terceiro elemento ($2$) não é divisível por $3$. Observe que Pedrinho não considera sequência vazia radical. O total, neste caso, é **6**.

Esse processo é muito demorado, e Pedrinho deseja fazer a contagem de maneira mais rápida. Ajude Pedrinho: sua tarefa é desenvolver um algoritmo que receba uma sequência $A = [a_1, a_2, \dots, a_n]$ (com $a_i \le n$) e retorne a quantidade total de subsequências radicais que ela possui. A solução deve ter uma complexidade de tempo $O(n\sqrt{n})$.

---

**OBS**: Como o número total pode ser muito grande, retorne o resultado **módulo $999999937$** (um número descolado, mas isso é outro problema).

---

### Restrições:

* $1 \le n \le 10^5$.
* $1 \le a_i \le n$ para todo $1 \le i \le n$.

| Entrada | Saída |
| :---: | :---: |
| $n=3$, $A = [1, 2, 2]$ | 6 |
| $n=1$, $A = [1]$ | 1 |
| $n=2$, $A = [1, 2]$ | 3 |
| $n=5$, $A = [2, 2, 1, 5, 3]$ | 8 |