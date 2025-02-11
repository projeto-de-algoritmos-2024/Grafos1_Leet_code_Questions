## 1377. Frog Position After T Seconds

**Dificuldade:** Difícil

**Link da questão:**

https://leetcode.com/problems/frog-position-after-t-seconds/description/?envType=problem-list-v2&envId=graph&difficulty=HARD

**Link do vídeo**

[![vídeo](https://img.youtube.com/vi/FfwyKStw4zQ/0.jpg)](https://www.youtube.com/watch?v=FfwyKStw4zQ)

https://www.youtube.com/watch?v=FfwyKStw4zQ

### Cópia do Enunciado:

Given an undirected tree consisting of n vertices numbered from 1 to n. A frog starts jumping from vertex 1. In one second, the frog jumps from its current vertex to another unvisited vertex if they are directly connected. The frog can not jump back to a visited vertex. In case the frog can jump to several vertices, it jumps randomly to one of them with the same probability. Otherwise, when the frog can not jump to any unvisited vertex, it jumps forever on the same vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi.

Return the probability that after t seconds the frog is on the vertex target. Answers within 10-5 of the actual answer will be accepted.

## Exemplos:

### **Exemplo 1:**

![Exemplo1](https://assets.leetcode.com/uploads/2021/12/21/frog1.jpg)

<br>

**Input:** n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4

**Output:** 0.16666666666666666 

**Explanation:** The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 probability to the vertex 2 after second 1 and then jumping with 1/2 probability to vertex 4 after second 2. Thus the probability for the frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 = 0.16666666666666666. 

### **Exemplo 2:**

![Exemplo2](https://assets.leetcode.com/uploads/2021/12/21/frog2.jpg)

**Input:** n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7

**Output:** 0.3333333333333333

**Explanation:** The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after second 1. 
