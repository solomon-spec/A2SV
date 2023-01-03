from collections import defaultdict
class Solution(object):
    def equalPairs(self, grid):
        rows = defaultdict(int)
        columns = defaultdict(int)
        answer = 0
        for i in range(len(grid)):
            row = ""
            for j in range(len(grid)):
                row+=(str(grid[i][j])+"x")
            rows[row]+=1
                      
        for i in range(len(grid)):
            column = ""
            for j in range(len(grid)):
                column+=(str(grid[j][i])+"x")
            columns[column]+=1
                      
        for i in rows:
            if i in columns:
                answer+= rows[i]*columns[i]
        #print(rows, columns)
        return answer
                
            
            
        
        
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        