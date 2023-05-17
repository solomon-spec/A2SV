class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        dire = [[0,1],[1,0],[0,-1],[-1,0]]
        n, m = len(grid), len(grid[0])
        def is_valid(i,j,keys):
            if 0 <= i < n and 0 <= j <m: 
                if grid[i][j] != "#":
                    if grid[i][j] != ".":
                        if grid[i][j] != "@" and (grid[i][j].lower() == grid[i][j] or grid[i][j].lower() in keys): return True
                        elif grid[i][j] == "@": return True
                        else: return False
                    else: return True
                else: return False
            return False
        
        queue = deque([])
        visited = set()
        key = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "@":
                    queue.append((i,j,[],0))
                    visited.add(((i,j),()))
                elif grid[i][j] != "#" and grid[i][j] != "." and grid[i][j] == grid[i][j].lower():key += 1
        while queue:
            x = queue.popleft()
            for i,j in dire:
                keys = {}
                r = x[0] + i
                c = x[1] + j
                keys[(r,c)] = x[2].copy()
                if is_valid(r,c,x[2]) and (r,c,tuple(x[2])) not in visited:
                    if 97<= ord(grid[r][c]) <= 120 and grid[r][c] not in keys[(r,c)]:keys[(r,c)].append(grid[r][c])
                    keys[(r,c)].sort()
                    queue.append([r,c,keys[(r,c)].copy(),x[3]+1])
                    if r == 1 and c == 4: print(x)
                    if len(keys[(r,c)]) == key:
                        print(x[2],"ans",keys[(r,c)])
                        return x[3] + 1
                    
                    visited.add(tuple([r,c,tuple(keys[(r,c)])]))
        return -1
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
            
            
            