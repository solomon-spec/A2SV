class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        n = len(target)
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
        
        for i,j in allowedSwaps:
            union(i,j)
            
        graph = defaultdict(dict)
        ans = n
        for i in range(n):
            graph[find(i)][source[i]] = graph[find(i)].get(source[i],0) + 1
        for i in range(n):
            if graph[find(i)].get(target[i],0) > 0:
                ans -= 1
                graph[find(i)][target[i]] -= 1
        return ans
        
        