class Solution(object):
    
    
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        def localvalue(i,j):
            max_value = 0
            for row in range(3):
                for column in range(3):
                    if grid[row + i][column + j] > max_value:
                        max_value = grid[row + i][column + j]
            
            return max_value
        
        n = len(grid)
        answer = [[0]*(n-2) for i in range(n -2)]
        for row in range(n - 2):
             for column in range(n - 2):
                    answer[row][column] = localvalue(row,column)
                    
        return answer          