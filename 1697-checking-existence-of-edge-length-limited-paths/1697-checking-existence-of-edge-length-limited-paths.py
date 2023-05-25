class Solution:
    def distanceLimitedPathsExist(self, n: int, edge: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parent = [i for i in range(n)]
        edge.sort(key = lambda x: x[2])
        def find(child):
            if child != parent[child]: 
                parent[child] = find(parent[child])
            return parent[child]
        
        def union(ver1,ver2): 
            x = find(ver1)
            y = find(ver2)
            if y > x: parent[y] = x
            else: parent[x] = y
                
        woo = sorted([queries[i] + [i] for i in range(len(queries))],key = lambda x: x[2])
        cur_con = 0
        ans = [0]*len(queries)
        
        for i in range(len(queries)):
            #print(x)
            x,y,max_con,z = woo[i]
            while cur_con < len(edge) and edge[cur_con][2] < max_con:
                union(edge[cur_con][0],edge[cur_con][1])
                cur_con += 1
            if find(x) == find(y):ans[z] = True
            else: ans[z] = False
        return ans
        
        
        
              
        