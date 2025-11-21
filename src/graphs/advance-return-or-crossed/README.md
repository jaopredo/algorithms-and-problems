# Classificação de Arestas Não Pertencentes à Floresta DFS 🌳➡️

Dado um grafo dirigido e sua **floresta DFS** (obtida ao executar uma busca em profundidade), podemos encontrar arestas que **não pertencem** à árvore DFS. Essas arestas extras podem ser classificadas em diferentes categorias com base no relacionamento entre os vértices e nos **intervalos de tempo** registrados durante a DFS.

Cada vértice $v$ recebe dois tempos:

- **Entrada** $d[v]$: quando a DFS visita $v$ pela primeira vez  
- **Saída** $f[v]$: quando a DFS termina de explorar $v$

O intervalo de $v$ é $[d[v], f[v]]$.

O objetivo é determinar, para uma aresta $(v_i, v_j)$ que **não** faz parte da floresta DFS, qual tipo de aresta ela é.

---

## Tipos de Arestas

### 🔵 Aresta de Avanço (Forward Edge)
- **Condição estrutural:** $v_i$ é ancestral de $v_j$  
- **Condição pelos tempos:**  
  O intervalo de $v_j$ está **contido** no intervalo de $v_i$:  
  $$d[v_i] < d[v_j] < f[v_j] < f[v_i]$$

#### Exemplo
- Tempos:  
  - $d[A] = 1,\ f[A] = 10$  
  - $d[C] = 4,\ f[C] = 7$
- Intervalos:  
  - $A = [1,10]$  
  - $C = [4,7]$
- Aresta analisada: $(A, C)$  
- Conclusão: como $[4,7] \subset [1,10]$, é **aresta de avanço**.

---

### 🔴 Aresta de Retorno (Back Edge)
- **Condição estrutural:** $v_i$ é descendente de $v_j$  
- **Condição pelos tempos:**  
  O intervalo de $v_j$ **contém** o intervalo de $v_i$:  
  $$d[v_j] < d[v_i] < f[v_i] < f[v_j]$$

#### Exemplo
- Tempos:
  - $d[D] = 2,\ f[D] = 15$  
  - $d[F] = 5,\ f[F] = 8$
- Intervalos:
  - $D = [2,15]$  
  - $F = [5,8]$
- Aresta analisada: $(F, D)$  
- Conclusão: $[2,15]$ contém $[5,8]$, logo é **aresta de retorno**.

---

### 🟢 Aresta Cruzada (Cross Edge)
- **Condição estrutural:** $v_i$ e $v_j$ estão em subárvores diferentes, e $v_i$ é visitado **depois** de $v_j$  
- **Condição pelos tempos:**  
  O intervalo de $v_j$ ocorre **antes** do intervalo de $v_i$:  
  $$f[v_j] < d[v_i]$$

#### Exemplo
- Tempos:
  - $d[X] = 1,\ f[X] = 4$  
  - $d[Y] = 6,\ f[Y] = 9$
- Intervalos:
  - $X = [1,4]$  
  - $Y = [6,9]$
- Aresta analisada: $(X, Y)$  
- Conclusão: $4 < 6$, então o intervalo de $X$ termina antes do início de $Y$; é **aresta cruzada**.
