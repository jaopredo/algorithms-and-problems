## 📝 Problema 8. Video Game

### Descrição
Existe um jogo com **$n$ estados** diferentes, numerados de $1$ a $n$. A partir de cada estado você é obrigado a tomar uma decisão (entre um conjunto de possibilidades pré-estabelecidas para esse estado) que levam a um estado diferente. O jogo foi criado de forma que **não é possível retornar a estado já visitado**.

Seu objetivo é ir do **começo (estado 1)** até o **final do jogo (estado número $n$)**. De quantas formas isso pode ser feito?

Dada a descrição de todas as transições de estado, uma lista de pares de inteiros $(a, b)$ (onde cada par representa uma transição válida do estado $a$ para o estado $b$), calcule a **quantidade de formas de 'zerar' o jogo**.

Desenvolva um algoritmo com complexidade $O(n + m)$.

---

### Entrada

* **$1 \leq n \leq 10^5$**: O número de estados.
* **$1 \leq m \leq 2 \cdot 10^5$**: O número de transições.
* $[(a_1, b_1), \dots, (a_m, b_m)]$, com $1 \leq a_i, b_i \leq n$: Uma lista com as $m$ transições.

### Saída

* Retorne um único inteiro: o **número de formas distintas de ir do estado 1 ao estado $n$**.

---

### Exemplos

| $n, m$ | Transições $(A)$ | Saída |
| :---: | :--- | :---: |
| $n=3; m=2$ | $[(1, 2), (2, 3)]$ | 1 |
| $n=5; m=7$ | $[(1, 3), (3, 4), (1, 2), (2, 5), (1, 4), (4, 5), (3, 5)]$ | 4 |
| $n=3; m=2$ | $[(1, 2), (3, 2)]$ | 0 |