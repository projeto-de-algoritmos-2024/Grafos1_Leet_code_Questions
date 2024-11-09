"""1377. Frog Position After T Seconds

https://leetcode.com/problems/frog-position-after-t-seconds/description/?envType=problem-list-v2&envId=graph&difficulty=HARD

"""

from queue import Queue
from typing import List

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
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
            
            print(node) # Para testes
            print(distance)
            print(time)
            print("")

            if node == target and time == 0: # Chegou e acavou o tempo
                return distance
            elif node == target and time > 0: # Chegou e ainda tem tempo
                print ("Vai passar\n")
                return 0
            elif time == 0 and node != target: # Acabou o tempo e nao chegou
                print ("Acabou o tempo\n")
                return  0
            
            v_number = len(graph[node]) # Pega no numero de vertices do no
            distance_prox = distance * (1 / v_number) if v_number != 0 else 0
            for v in graph[node]: # - Slide LINHA 6
                if v in non_explored_nodes: # - Slide LINHA 7
                    non_explored_nodes.remove(v) # - Slide LINHA 9
                    node_queue.put((v, distance_prox,time-1)) # - Slide LINHA 10
        print("Saiu do loop")
    
sol = Solution()

# Entrada de Teste 1
n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]] 
t = 2
target = 4

resultado = sol.frogPosition(n, edges, t, target)
print(resultado)

# Entrada de Teste 2
n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]] 
t = 1
target = 7

resultado = sol.frogPosition(n, edges, t, target)
print(resultado)        