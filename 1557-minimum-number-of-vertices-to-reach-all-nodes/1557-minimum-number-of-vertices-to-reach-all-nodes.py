class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        sett = set(range(n)) 
        for i in edges:
            if i[1] in sett: sett.remove(i[1])
        return sett