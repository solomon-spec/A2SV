class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        def find(child):
            if child != parent[child]: 
                parent[child] = find(parent[child])
            return parent[child]
        def union(ver1,ver2): 
            x = find(ver1)
            y = find(ver2)
            if rank[x] > rank[y]:
                parent[y] = parent[x]
                rank[x] += rank[y]
            else:
                parent[x] = parent[y]
                rank[y] += rank[x]
        for x,y in edges: union(x,y)
        return find(source) == find(destination)