class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [0]*(len(edges)+1)
        def find(child):
            if child != parent[child]: 
                parent[child] = find(parent[child])
            return parent[child]
        
        def union(ver1,ver2):
            parent[find(ver1)] = find(ver2)
        for i in range(len(edges)-1,-1,-1):
            parent = [i for i in range(len(edges)+1)]
            for x in edges:
                if x != edges[i]:union(x[0],x[1])

            x = find(len(edges))
            T = True
            for z in range(1,len(edges)):
                if find(z) != x:T = False
            if T: 
                return edges[i]

        