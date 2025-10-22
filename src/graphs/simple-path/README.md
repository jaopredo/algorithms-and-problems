# Problema de Verificação de Caminho em Grafos

## Descrição

São dados:
1.  Um **Grafo $G$**, definido por um conjunto de vértices $V$ e um conjunto de arestas $E$: $G = (V, E)$.
2.  Um **Caminho $P$**, dado como uma sequência de vértices: $P = (v_1, v_2, \dots, v_k)$.

O desafio consiste em desenvolver um algoritmo que realize duas verificações:

### 1. Validação de Caminho

Verificar se a sequência de vértices $P$ representa um caminho **válido** no grafo $G$.

* Um caminho é válido se, para cada par de vértices consecutivos $(v_i, v_{i+1})$ na sequência $P$, existe uma aresta correspondente $(v_i, v_{i+1})$ (ou $\{v_i, v_{i+1}\}$ no caso de grafos não-direcionados) presente no conjunto de arestas $E$ de $G$.

### 2. Verificação de Simplicidade

Se $P$ for um caminho válido, verificar se ele é um **caminho simples**.

* Um caminho é simples se todos os vértices na sequência $P$ são **distintos**, ou seja, nenhum vértice é repetido no caminho.

## Objetivo

| Requisito | Detalhe |
|---|---|
| **Tarefa** | Criar um algoritmo que receba $G$ e $P$, e determine a validade e a simplicidade de $P$. |
| **Entrada** | O grafo $G$ e a sequência de vértices $P$. |
| **Saída** | Duas informações booleanas (por exemplo, "É Caminho Válido" e "É Caminho Simples"). |

***

## Exemplos Ilustrativos

Suponha um grafo $G$ com $V=\{1, 2, 3, 4\}$ e $E=\{(1, 2), (2, 3), (3, 4), (1, 4)\}$.

| Caminho $P$ | É Caminho Válido em $G$? | É Caminho Simples? |
|:-----------:|:-------------------------:|:--------------------:|
| $(1, 2, 3)$ | SIM | SIM |
| $(1, 4, 3, 2)$ | NÃO | SIM |
| $(1, 2, 1, 4)$ | SIM | NÃO |
| $(1, 4, 1)$ | SIM | NÃO |
| $(1)$ | SIM | SIM |