class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dire = [[0,1],[1,0],[-1,0],[0,-1]]
        vis = set()
        def area(r,c,visited):
            nonlocal vis
            vis.add((r,c))
            visited.add((r,c))
            total = 0
            for i in dire:
                if 0<= c+i[1] < len(grid[0])  and 0<= r+i[0] < len(grid) and (r+i[0],c+i[1]) not in visited:
                    if grid[r+i[0]][c +i[1]] == 1: 
                        total += area(r+i[0],c+i[1],visited)
            return total + 1
        maxx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in vis and grid[i][j] == 1:
                    maxx = max(maxx,area(i,j,set()))
        return maxx