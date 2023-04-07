class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic = defaultdict(list)
        visited = set()
        for i in edges:
            dic[i[0]].append(i[1])
            dic[i[1]].append(i[0])
        
        def check(node,visited):
            if node == destination:
                return True
            visited.add(node)
            
            for i in dic[node]:
                if i not in visited:
                    if check(i,visited): return True
            return False
        return check(source,set())