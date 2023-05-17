class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]
        
        def find(child):
            if child != parent[child]: 
                parent[child] = find(parent[child])
            return parent[child]
        def union(ver1,ver2):
            parent[find(ver1)] = find(ver2)
        for x,y in edges: union(x,y)
        return find(source) == find(destination)