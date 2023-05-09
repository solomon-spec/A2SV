class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        path = [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1)]
        visited = set([(0,0)])
        queue = deque()
        if grid[0][0] == 0:
            queue = deque([((0,0),1)])
        
        def is_valid(r,c):
            if 0 <= r < n and 0 <= c < n: return True
            return False
        minn = inf
        while queue:
            cur = queue.popleft()
            if cur[0][0] == n-1 and cur[0][1] == n-1:
                minn = min(minn,cur[1])
                continue
            for i,j in path:
                x,y = i + cur[0][0], j + cur[0][1]
                if (x,y) not in visited and is_valid(x,y) and grid[x][y] == 0:
                    cu = ((x,y),cur[1]+1)
                    queue.append(cu)
                    visited.add((x,y))
        if minn == inf: minn = -1
        return minn
        