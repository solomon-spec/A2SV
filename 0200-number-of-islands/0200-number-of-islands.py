class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cur = 0
        visited = set()
        n = len(grid)
        m = len(grid[0])
        
        def is_valid(x,y):
            if 0 <= x < n and 0 <= y < m:
                return True
            return False
        dire = [(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i,j) not in visited:
                    visited.add((i,j))
                    queue = deque([(i,j)])
                    
                    while queue:
                        a,b = queue.pop()
                        for x,y in dire:
                            r = a + x
                            c = b + y
                            if is_valid(r,c) and (r,c) not in visited and grid[r][c]=='1':
                                queue.append((r,c))
                                visited.add((r,c))
                    #print(visited)
                    cur += 1
        return cur