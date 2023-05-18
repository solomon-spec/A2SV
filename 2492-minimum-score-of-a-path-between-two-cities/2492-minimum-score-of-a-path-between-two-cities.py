class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = {i+1:i+1 for i in range(n)}
        def find(child):
            if child != parent[child]: 
                parent[child] = find(parent[child])
            return parent[child]
        def union(ver1,ver2): 
            x = find(ver1)
            y = find(ver2)
            if x < y: parent[y] = parent[x]
            else:parent[x] = parent[y]
        minn = inf
        for i,j,k in roads:union(i,j)
            
        for i,j,k in roads:
            if find(i)==1: minn = min(minn,k)
        print(parent)
        return minn
            