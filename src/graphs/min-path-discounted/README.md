# Problema do Caminho Mínimo com Cupom de Desconto

Você recebe um grafo ponderado **não direcionado** com $n$ cidades e $m$ rotas.  
Cada rota é representada por uma aresta com peso $w$, indicando o custo para viajar entre duas cidades.

Você também recebe um **cupom de desconto** que pode ser usado **exatamente uma vez** em **qualquer aresta** do caminho.  
Ao aplicar o cupom em uma aresta de peso $w$, o custo dessa aresta passa a ser:

$$\left\lfloor \frac{w}{2} \right\rfloor$$

Seu objetivo é determinar, para cada cidade, o **menor custo possível** para alcançá-la a partir de uma cidade inicial $v$, considerando que o cupom pode ser aplicado em **uma única** aresta do caminho.

A resposta deve ser um vetor onde cada posição $i$ indica o menor custo para chegar ao nó $i$ **utilizando o cupom exatamente uma vez**.
