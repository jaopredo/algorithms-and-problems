# Problema de Verificação de Subgrafo

## Descrição

São dados dois grafos:
1.  **Grafo $G$**, definido pelo conjunto de vértices $V$ e o conjunto de arestas $E$: $G = (V, E)$.
2.  **Grafo $H$**, definido pelo conjunto de vértices $V'$ e o conjunto de arestas $E'$: $H = (V', E')$.

É garantido que os dois grafos compartilham o mesmo conjunto de vértices: $V = V'$.

O desafio é **criar um algoritmo** que determine se $H$ é um **subgrafo** de $G$.

## Definição de Subgrafo

O grafo $H = (V', E')$ é um subgrafo do grafo $G = (V, E)$ se e somente se as seguintes condições forem satisfeitas:
1.  O conjunto de vértices de $H$ é um subconjunto do conjunto de vértices de $G$: $V' \subseteq V$.
2.  O conjunto de arestas de $H$ é um subconjunto do conjunto de arestas de $G$: $E' \subseteq E$.

## Objetivo

| Requisito | Detalhe |
|---|---|
| **Tarefa** | Desenvolver um algoritmo que retorne $\text{VERDADEIRO}$ se $H$ for subgrafo de $G$, e $\text{FALSO}$ caso contrário. |
| **Entrada** | As representações de $G = (V, E)$ e $H = (V', E')$, onde $V = V'$. |
| **Saída** | Um valor booleano (Verdadeiro ou Falso). |

***

## Exemplos

Suponha que $V = V' = \{A, B, C\}$.

| Arestas de $G$ ($E$) | Arestas de $H$ ($E'$) | $H$ é Subgrafo de $G$? |
|:----------------------:|:---------------------:|:----------------------:|
| $\{(A, B), (B, C)\}$ | $\{(A, B)\}$ | $\text{VERDADEIRO}$ |
| $\{(A, B), (B, C)\}$ | $\{(A, C)\}$ | $\text{FALSO}$ |
| $\{(A, B)\}$ | $\{(A, B), (A, C)\}$ | $\text{FALSO}$ |
| $\emptyset$ | $\emptyset$ | $\text{VERDADEIRO}$ |