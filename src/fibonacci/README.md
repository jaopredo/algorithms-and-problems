# Problema da Sequência de Fibonacci

## Descrição

O desafio é calcular o $n$-ésimo número da Sequência de Fibonacci ($F_n$), dada a sua posição $n$ (onde $n \ge 0$).

A sequência é definida por:
$$F_n = F_{n-1} + F_{n-2}$$
com os casos base $F_0 = 0$ e $F_1 = 1$.

## Requisitos de Implementação

Você deve desenvolver três implementações distintas para calcular $F_n$, cada uma atendendo a um requisito de complexidade de tempo específico no pior caso:

### 1. Implementação Padrão (Baseada na Definição)

Implemente uma solução que siga a definição de recorrência da sequência.

| Requisito | Detalhe |
|---|---|
| **Complexidade de Tempo** | Deve ser exponencial. $\mathbf{O}(\phi^n)$ |

### 2. Implementação Otimizada

Implemente uma solução eficiente que evite a repetição de cálculos.

| Requisito | Detalhe |
|---|---|
| **Complexidade de Tempo** | Linear: $\mathbf{O}(n)$ |

### 3. Implementação de Tempo Constante

Implemente uma solução que minimize o número de operações, independentemente do valor de $n$.

| Requisito | Detalhe |
|---|---|
| **Complexidade de Tempo** | Constante: $\mathbf{O}(1)$ |

***

## Exemplos

| Entrada ($n$) | Saída ($F_n$) |
|:-------------:|:-------------:|
| $0$ | $0$ |
| $1$ | $1$ |
| $6$ | $8$ |
| $10$ | $55$ |