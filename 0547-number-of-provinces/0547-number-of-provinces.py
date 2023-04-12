class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        dic = defaultdict(list)  
        n = len(isConnected)
        
        for row in range(n):
            for col in range(n):
                if isConnected[row][col]:  dic[row].append(col)       
        prov = 0
        visited = set()
        def check(city):
            nonlocal prov
            nonlocal visited
            if city not in visited:
                visited.add(city)
                for i in dic[city]: check(i)
            return 
        for i in dic:
            if i not in visited:
                check(i)
                prov += 1
        return prov