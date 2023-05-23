class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        parent = [i for i in range(n)]
        sets = {i:set([i]) for i in range(n)}
        
        def find(child):
            if child != parent[child]: 
                parent[child] = find(parent[child])
            return parent[child]
        
        def union(ver1,ver2): 
            x = find(ver1)
            y = find(ver2)
            
            if y > x:
                parent[y] = x
                sets[x].update(sets[y])
            
            else:
                parent[x] = y
                sets[y].update(sets[x])
                
        ans = []
        for i,j in requests:
            par1 = find(i)
            par2 = find(j)
            can = True
            for x,y in restrictions:
                if (x in sets[par1] and y in sets[par2]) or (y in sets[par1] and x in sets[par2]):
                    ans.append(False)
                    can = False
                    break
            if can:
                union(par1,par2)
                ans.append(True)
                    
        return ans
                    
                
                