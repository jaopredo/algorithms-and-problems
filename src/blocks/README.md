# Blocos

Você recebeu $n$ blocos de madeira e seu desafio é empilhá-los, formando o menor número
possível de torres. Para isso, você deve seguir duas regras estritas:

- Regra de Empilhamento: Um bloco só pode ser colocado sobre outro se o seu
tamanho for menor ou igual ao do bloco inferior.
- Ordem de Processamento: Os blocos devem ser processados um a um, na sequência predefinida em que são apresentados.

A cada bloco, você deve decidir se o coloca no topo de uma torre existente (respeitando
a regra de empilhamento) ou se inicia uma nova torre com ele.

Dada a sequência de tamanhos dos blocos, encontre o número mínimo de torres necessárias. Desenvolva um algoritmo que executa em $O(n log n)$ no pior caso, onde $n$ é o
número de blocos

## Exemplos

| Entrada | Saída | Exemplos |
|---------|-------|----------|
| $[1, 2, 1, 4]$ | $3$ | $[1, 1], [2], [4]$ |
| $[11, 22, 11, 33, 22, 77, 44, 22]$ | $4$ | $[11, 11], [22, 22, 22], [33], [77, 44]$ |
| $[3, 3, 3, 3, 3, 3]$ | $1$ | $[3, 3, 3, 3, 3, 3]$ |
