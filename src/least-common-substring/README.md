# Subsequência Comum Mais Longa (LCS) 🧐

Dadas duas *strings*, $X$ e $Y$, uma **subsequência comum** é uma sequência de caracteres que pode ser obtida **removendo zero ou mais caracteres** de $X$ e **removendo zero ou mais caracteres** de $Y$.

O objetivo é encontrar o **comprimento da maior subsequência comum** entre $X$ e $Y$.

## Regras

- Dada a *string* $X$ de comprimento $m$: $X = \langle x_1, x_2, \dots, x_m \rangle$.
- Dada a *string* $Y$ de comprimento $n$: $Y = \langle y_1, y_2, \dots, y_n \rangle$.
- Uma subsequência $Z = \langle z_1, z_2, \dots, z_k \rangle$ de $X$ deve ter índices crescentes $i_1 < i_2 < \dots < i_k$ tais que $x_{i_j} = z_j$. O mesmo se aplica a $Y$.
- O objetivo é **maximizar o comprimento** $k$ de $Z$ tal que $Z$ é uma subsequência de $X$ e de $Y$.

Desenvolva um algoritmo que encontre o comprimento máximo da subsequência comum entre $X$ e $Y$.

## Exemplos

| String X | String Y | LCS (Exemplo) | Comprimento da LCS |
|---|---|---|---|
| A**G**G**T**A**B** | **G**X**T**AY**B** | GTAB | 4 |
| A**B**C**D**E | B**D**F | BD | 2 |
| A**G**C**A**T | **G**T**A**C**G** | GAC | 3 |
| **G**T**A**C**G** | **C**A**T**G** | CATG | 4 |
| BAZINGA | AZAR | AZA | 3 |

- Exemplo 1:
  - $X$: A**G**G**T**A**B**
  - $Y$: **G**X**T**AY**B**
  - $\text{LCS} = \text{GTAB}$
- Exemplo 3:
  - $X$: A**G**C**A**T
  - $Y$: **G**T**A**C**G**
  - $\text{LCS} = \text{GAC}$