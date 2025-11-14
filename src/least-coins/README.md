# Troco com Número Mínimo de Moedas 💰

Dado um valor inteiro não negativo \( v \) e uma lista de **denominações de moedas** pertencentes a um **sistema canônico**, determine o **menor número de moedas** necessário para formar exatamente o valor \( v \).

## Definição — Sistema Canônico

Um conjunto de denominações de moedas $D = \{d_1, d_2, \dots, d_k\}$ é chamado de **sistema canônico** quando ele possui a propriedade estrutural de que, para todo valor inteiro não negativo, existe sempre uma forma de representá-lo como soma de elementos de \(D\) utilizando combinações consideradas válidas segundo as regras do sistema monetário correspondente.

Em termos práticos, trata-se de um sistema cujo conjunto de moedas foi definido de modo a garantir que qualquer valor possa ser composto por essas denominações de maneira consistente, mantendo coerência com o modo tradicional como tais moedas são utilizadas.

### ✔️ Exemplo de sistema canônico
O conjunto de denominações:
\[
D = \{1, 5, 10, 25\}
\]
é um sistema canônico típico (como no sistema monetário norte-americano).  
Qualquer valor pode ser representado de modo compatível com o uso tradicional dessas moedas.

Exemplos de representações possíveis:
- 37 = 25 + 10 + 1 + 1
- 63 = 25 + 25 + 10 + 1 + 1 + 1

### ✖️ Exemplo de sistema **não-canônico**
O conjunto:
\[
D = \{1, 3, 4\}
\]
não é considerado canônico, embora permita representar qualquer valor.

Um exemplo ilustrativo:
- Para 6, existe a representação: 3 + 3  
- Mas também existe outra representação: 4 + 1 + 1

O sistema não segue a mesma coerência estrutural típica de sistemas canônicos, mesmo sendo possível montar todos os valores.

## Detalhes

- As moedas podem ser usadas repetidamente.
- Sempre existe representação válida para qualquer valor \( v \ge 0 \).

## Exemplos

| Valor \(v\) | Denominações | Combinação possível | Nº mínimo de moedas |
|-------------|--------------|----------------------|----------------------|
| 37 | \{25, 10, 5, 1\} | 25 + 10 + 1 + 1 | 4 |
| 63 | \{50, 20, 10, 1\} | 50 + 10 + 1 + 1 + 1 | 5 |
| 6  | \{4, 3, 1\} | 3 + 3 | 2 |

Formule um algoritmo que retorne apenas esse número mínimo.
