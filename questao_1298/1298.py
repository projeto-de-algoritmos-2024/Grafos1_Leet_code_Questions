"""
1298. Maximum Candies You Can Get from Boxes
https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/description/
"""


from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        caixas_abriveis = []
        caixas_encontradas = initialBoxes
        doces_total = 0
        
        contador_caixas_iniciais = 0
        for caixas_encontrada in caixas_encontradas:
            if (status[caixas_encontrada] == 1):
                caixas_abriveis.append(caixas_encontradas.pop(contador_caixas_iniciais))
                continue
            contador_caixas_iniciais += 1


        while len(caixas_abriveis) != 0:
            caixa = caixas_abriveis.pop(0)
            doces_total += candies[caixa]
            for chave in keys[caixa]:
                status[chave] = 1
            caixas_encontradas.extend(containedBoxes[caixa])

            contador_caixas_encontradas = 0
            for caixas_encontrada in caixas_encontradas:
                if (status[caixas_encontrada] == 1):
                    caixas_abriveis.append(caixas_encontradas.pop(contador_caixas_encontradas))
                    continue
                contador_caixas_encontradas += 1
        return doces_total


# TEST CASES
# Not part of the solution.

s = Solution()
print(s.maxCandies(status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]))
print(s.maxCandies(status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]))