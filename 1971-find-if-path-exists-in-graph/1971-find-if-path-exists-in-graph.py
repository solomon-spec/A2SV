class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic = defaultdict(list)
        visited = set()
        for i in edges:
            dic[i[0]].append(i[1])
            dic[i[1]].append(i[0])
        
        def check(node):
            nonlocal visited
            for i in dic[node]:
                if i not in visited:
                    visited.add(i)
                    check(i)
            return
        check(source)
        return destination in visited or source == destination