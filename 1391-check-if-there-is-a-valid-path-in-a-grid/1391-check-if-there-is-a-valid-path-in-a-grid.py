class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        #lrud
        n = len(grid)
        m  = len(grid[0])
        parent = [i for i in range(n*m)]
        rank = [1 for i in range(n*m)]
        dire = [[0,-1],[0,1],[-1,0],[1,0]]
        dic = {1:[1,1,0,0],2:[0,0,1,1],3:[1,0,0,1],4:[0,1,0,1],5:[1,0,1,0],6:[0,1,1,0]}
        
        def find(child):
            if child != parent[child]: 
                parent[child] = find(parent[child])
            return parent[child]
        def union(ver1,ver2):
            x = find(ver1)
            y = find(ver2)
            if rank[x] < rank[y]: 
                parent[y] = x
                rank[y] += rank[x]
            else:
                parent[x] = y
                rank[x] += rank[y]
            
        
        def is_valid(r,c):
            if 0 <= r < n and 0 <= c <m: return True
            return False
        for i in range(n):
            for j in range(m):
                for move in range(4):
                    x = i+dire[move][0]
                    y = j+dire[move][1]
                    if dic[grid[i][j]][move] == 1 and is_valid(x,y):
                        if move % 2 == 0: m2 = move + 1
                        else: m2 = move -1
                        if dic[grid[x][y]][m2]:
                            union(i*m+j,x*m+y)
        return find(0) == find(n*m-1)
                        
                        
        
        