class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        def is_invalid(x,y):
            if 0 <= x < row and 0 <= y < col and grid[x][y] == 1:
                return False
            return True
        peremeter = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(row):
            
            for j in range(col):
                if not is_invalid(i,j):
                    for x,y in directions:
                        if is_invalid(x+i,y+j):
                            peremeter += 1
        return peremeter
                    
            