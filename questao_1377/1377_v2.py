"""1377. Frog Position After T Seconds

https://leetcode.com/problems/frog-position-after-t-seconds/description/?envType=problem-list-v2&envId=graph&difficulty=HARD

"""

from queue import Queue
from typing import List

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if n == 1: # Caso de teste especifico - Alvo no 1 e sem filhos
            return 1.0
        if target == 1 and t > 0: # Caso de teste especifico - Alvo no 1 com filhos e tempo excedente
            return 0
        found = 0
        graph = {} # Craindo lista de adjacencia
        for u, v in edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
        
        node_queue = Queue() # Cria fila
        node_queue.put((1, 1.0, t)) # Enfilera o primeiro no - Slide LINHA 2
        non_explored_nodes = list(range(1, n+1)) # Cria uma lista com os nos nao visitados

        while not node_queue.empty():  # Enquanto a fila não estiver vazia - Slide LINHA 4
            dequeue  = node_queue.get() # Remove da fila - Slide LINHA 5
            node = dequeue[0]
            distance = dequeue[1]
            time = dequeue[2]
            
            """ print(node) # Para testes
            print(distance)
            print(time)
            print("") """

            if node == target and time == 0: # Chegou e acavou o tempo
                return distance
            
            if node == target: # Achou o alvo
                if time < 0: # Caso o tempo ja tenha se exgotado
                    return 0
                if len(graph[node]) == 1: # Caso ainda sobre tempo verifica se existem filhos
                    return distance
                return 0

            v_number = len(graph[node]) - 1 # Pega no numero de vertices do no, subtrai por 1 por causa do no pai
            if node == 1: # Caso seja a raiz adiciona 1 de volta
                v_number = v_number + 1
            distance_prox = distance * (1 / v_number) if v_number != 0 else 0 # Calcula porcentagem e não deixa dividir por zero
            
            for v in graph[node]: # - Slide LINHA 6
                if v in non_explored_nodes: # - Slide LINHA 7
                    non_explored_nodes.remove(v) # - Slide LINHA 9
                    node_queue.put((v, distance_prox,time-1)) # - Slide LINHA 10    

# ------------------------ TUDO A PARTIR DESSA LINHA FOI EXCLUIDO PARA SUBMISSAO -------------------------

sol = Solution()

# Entrada de Teste 1
n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]] 
t = 2
target = 4

resultado = sol.frogPosition(n, edges, t, target)
print(resultado)
print("----------------------")

# Entrada de Teste 2
n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]] 
t = 1
target = 7

resultado = sol.frogPosition(n, edges, t, target)
print(resultado)     
print("----------------------")

# Entrada de Teste 3
n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 20
target = 6

resultado = sol.frogPosition(n, edges, t, target)
print(resultado)     
print("----------------------")

# Entrada de Teste 4
n = 8
edges = [[2,1],[3,2],[4,1],[5,1],[6,4],[7,1],[8,7]]
t = 7
target = 7

resultado = sol.frogPosition(n, edges, t, target)
print(resultado)     
print("----------------------")

# Entrada de Teste 5
n = 1
edges = []
t = 1
target = 1

resultado = sol.frogPosition(n, edges, t, target)
print(resultado)     
print("----------------------")

# Entrada de Teste 6
n = 9
edges = [[2,1],[3,1],[4,2],[5,3],[6,5],[7,4],[8,7],[9,7]]
t = 1
target = 8

resultado = sol.frogPosition(n, edges, t, target)
print(resultado)     
print("----------------------")

n = 9
edges = [[2,1],[3,2],[4,3],[5,3],[6,5],[7,3],[8,4],[9,5]]
t = 9
target = 1

resultado = sol.frogPosition(n, edges, t, target)
print(resultado)     
print("----------------------")
