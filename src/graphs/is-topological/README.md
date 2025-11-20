# Verificação de Numeração Topológica em um Grafo 🔢

Dado um grafo dirigido representado por um conjunto de vértices e arestas, o objetivo é verificar se uma numeração atribuída aos vértices é **topológica**, isto é, se respeita a ordem imposta pelas direções das arestas.

Uma numeração topológica garante que **toda aresta aponta de um vértice com número menor para um vértice com número maior**.

## Regras

- Um grafo é definido por:  
  $G = (V, E)$  
  onde:
  - $V = \{v_1, v_2, \dots, v_n\}$ é o conjunto de vértices  
  - $E \subseteq V \times V$ é o conjunto de arestas dirigidas  
- Dada uma **numeração**:
  - Uma função $num: V \rightarrow \{1, 2, \dots, |V|\}$ que associa um número a cada vértice
- A numeração é **topológica** se, para toda aresta $(u, v) \in E$, vale:
  - $num(u) < num(v)$

O objetivo é verificar se essa condição é **verdadeira para todas as arestas** do grafo.

## Exemplos

| Grafo (arestas $u \rightarrow v$) | Numeração $num(v)$ | É topológica? |
|---|---|---|
| $\{(0,1),(1,2),(2,3)\}$ | $[0\!\mapsto\!1,\ 1\!\mapsto\!2,\ 2\!\mapsto\!3,\ 3\!\mapsto\!4]$ | Sim |
| $\{(0,2),(2,1)\}$ | $[0\!\mapsto\!1,\ 1\!\mapsto\!2,\ 2\!\mapsto\!3]$ | Não |
| $\{(1,3),(0,2),(2,3)\}$ | $[0\!\mapsto\!1,\ 1\!\mapsto\!3,\ 2\!\mapsto\!2,\ 3\!\mapsto\!4]$ | Sim |
