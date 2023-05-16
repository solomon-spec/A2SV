class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        dire = [[0,1],[1,0],[0,-1],[-1,0]]
        n, m = len(grid), len(grid[0])
        def is_valid(i,j):
            if 0 <= i < n and 0 <= j <m: return True 
            return False
        
        queue = deque()
        visited = set()
        flag = False
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append([i,j])
                    grid[i][j] = -1
                    visited.add((i,j))
                    flag = True
                    break
            if flag: break
        queuen = deque([])
        while queue:
            z = queue.popleft()
            queuen.append(z + [0])
            for x,y in dire:
                r = z[0] + x
                c = z[1] + y
                if is_valid(r,c) and (r,c) not in visited and grid[r][c] ==1:
                    queue.append([r,c])
                    grid[r][c] = -1
                    visited.add((r,c))
        visited = set()
        
        while queuen:
            z = queuen.popleft()
            for x,y in dire:
                r = z[0] + x
                c = z[1] + y
                if is_valid(r,c) and grid[r][c] != -1:
                    if grid[r][c] == 1: return z[2]
                    elif (r,c) not in visited:
                        queuen.append([r,c,z[2]+1])
                        visited.add((r,c))
                        
            
            
            