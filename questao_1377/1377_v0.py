"""1377. Frog Position After T Seconds

https://leetcode.com/problems/frog-position-after-t-seconds/description/?envType=problem-list-v2&envId=graph&difficulty=HARD

"""

from queue import Queue
from typing import List

class Solution:    
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float: # [1,2] [1,3] [2,4]
        self.edges = edges
        self.n = n
        self.t = t
        self.target = target
        self.non_explored_nodes = range(1, n+1) # [1,2,3,4,5,6,7]
        self.NODES = range(1, n+1)
        self.node_queue: Queue = Queue(n)
        
        for node in self.NODES:
            if node in self.non_explored_nodes:
                self.node_queue.put_nowait(node)
                self.DFS_Visit(node)
                
                
    def DFS_Visit(self, node):
        self.non_explored_nodes.remove(node)
        for edge in self.edges:
