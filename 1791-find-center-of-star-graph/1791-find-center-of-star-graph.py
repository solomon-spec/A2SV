class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dic = defaultdict(int)
        for i in edges:
            dic[i[1]] += 1
            dic[i[0]] += 1
        for i in dic:
            if dic[i]  == len(edges): return i
            