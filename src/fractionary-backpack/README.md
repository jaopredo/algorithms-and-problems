# Mochila Fracionária

Você recebeu um conjunto de $n$ itens, cada um com um **peso** e um **valor**. Além disso, possui uma **mochila** com capacidade máxima de peso $W$.  
Seu objetivo é **maximizar o valor total** colocado na mochila, respeitando a restrição de peso.  

Diferente da versão clássica, **é permitido pegar frações dos itens**, desde que cada fração $\alpha_k$ satisfaça $0 < \alpha_k \leq 1$.

## Regras

- Cada item $i$ possui:
  - Peso: $w_i$
  - Valor: $v_i$
- A soma total dos pesos selecionados deve respeitar o limite:  
  $\sum_{i \in S} \alpha_i w_i \leq W$
- O objetivo é maximizar o valor total:  
  $\sum_{i \in S} \alpha_i v_i$
- É permitido pegar partes fracionárias de um item.

Desenvolva um algoritmo que encontre o valor máximo possível que pode ser obtido dentro da capacidade $W$.  
A solução ótima deve rodar em **$O(n \log n)$**, onde $n$ é o número de itens.

## Exemplos

| Item | Peso | Valor |
|------|------|--------|
| 1 | 1 | 2 |
| 2 | 3 | 4 |
| 3 | 4 | 6 |
| 4 | 5 | 10 |
| 5 | 7 | 8 |

**Capacidade da mochila:** $W = 9$

- Escolha $\{1, 2, 3\}$ → Peso total = 8, Valor total = 12 → ✅ Cabe na mochila  
- Escolha $\{3, 5\}$ → Peso total = 11, Valor total = 14 → ❌ Não cabe na mochila
