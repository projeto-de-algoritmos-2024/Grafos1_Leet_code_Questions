"""
207. Course Schedule
https://leetcode.com/problems/course-schedule/description/
"""

from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: # Utilizando o algoritimo de Kahn
        if numCourses == 1: # Caso de teste especifico - Apenas um curso
            return True
        if prerequisites == []: # Caso de teste especifico - Nenhum pre-requisito
            return True
        in_degree = [0] * numCourses  # Guarda o in-degree de cada no. in-degree = arestas que chegam a ele.

        graph = {i: [] for i in range(numCourses)}  # Craindo lista de adjacencia
        for u, v in prerequisites:
            if u == v: # Caso um curso dependa dele mesmo
                return False
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[v].append(u) # no v -> u 
            in_degree[u] += 1  # Logo u possui mais uma aresta para ele
        queue = deque([node for node in range(numCourses) if in_degree[node] == 0]) # Inicia a fila com nos que nao possuem pre-requisitos
        #print(queue)
        topological_order = []
        
        while queue: # Busca em largura - Slide LINHA 4
            node = queue.popleft() # - Slide LINHA 5
            topological_order.append(node)
            
            for v in graph[node]: # - Slide LINHA 6
                #print(graph[node])
                in_degree[v] -= 1  # Diminui o in-degree 
                if in_degree[v] == 0: 
                    queue.append(v)  # Adiciona o no caso in-degree fique 0
        
        if len(topological_order) == numCourses: # Se a ordenacao topologica inclui todos os nos, nao exisite ciclo
            return True
        else:
            return False


# ------------------------ TUDO A PARTIR DESSA LINHA FOI EXCLUIDO PARA SUBMISSAO -------------------------

sol = Solution()

# Entrada de Teste 1
numCourses = 2
prerequisites = [[1,0]]

a= sol.canFinish(numCourses, prerequisites)
print(a)
print("----------------------")

# Entrada de Teste 2
numCourses = 2
prerequisites = [[1,0],[0,1]]

a= sol.canFinish(numCourses, prerequisites)
print(a)
print("----------------------")

# Entrada de Teste 3
numCourses = 4
prerequisites = [[2,1],[3,2],[1,0]]

a= sol.canFinish(numCourses, prerequisites)
print(a)
print("----------------------")

# Entrada de Teste 4
numCourses = 4
prerequisites = [[0, 1], [1, 2], [3, 1], [3, 2]]

a= sol.canFinish(numCourses, prerequisites)
print(a)
print("----------------------")

# Entrada de Teste 5
numCourses = 20
prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]

a= sol.canFinish(numCourses, prerequisites)
print(a)
print("----------------------")

# Entrada de Teste 6
numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]

a= sol.canFinish(numCourses, prerequisites)
print(a)
print("----------------------")