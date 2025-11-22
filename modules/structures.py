from typing import Callable


class Queue:
    def __init__(self, n):
        self.q = [None for _ in range(n)]
        self.i = 0
        self.j = 0
    
    def enqueue(self, v):
        self.q[self.j] = v
        self.j += 1
    
    def dequeue(self):
        if self.i < self.j:
            v = self.q[self.i]
            self.i += 1
            return v
        else:
            raise IndexError("Fila vazia")
    
    def is_empty(self):
        return self.i >= self.j


class Heap:
    def __init__(self, criterium):
        self.criterium = criterium
        self.values = []
    
    def __getitem__(self, idx):
        return self.values[idx]
    
    def __len__(self):
        return len(self.values)

    def parent(self, i):
        return (i - 1) // 2
    
    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.values[i], self.values[j] = self.values[j], self.values[i]

    def push(self, x):
        self.values.append(x)
        self._heapify_up(len(self.values) - 1)

    def _heapify_up(self, i):
        while i > 0 and self.criterium(self.values[i], self.values[self.parent(i)]):
            p = self.parent(i)
            self.swap(i, p)
            i = p

    def pop(self):
        if not self.values:
            return None
        self.swap(0, len(self.values) - 1)
        x = self.values.pop()
        self._heapify_down(0)
        return x
    
    def clear(self):
        self.values.clear()

    def _heapify_down(self, i):
        n = len(self.values)
        while True:
            l = self.left(i)
            r = self.right(i)
            best = i

            if l < n and self.criterium(self.values[l], self.values[best]):
                best = l
            if r < n and self.criterium(self.values[r], self.values[best]):
                best = r

            if best == i:
                break

            self.swap(i, best)
            i = best


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return

        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
