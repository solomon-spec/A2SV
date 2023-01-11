class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        m = len(grid[0])
        answer = []
        column = [0 for i in range(m)]
        row = [0 for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row[i]+=1
                    column[j]+=1
                    
        print(row,column)
        for i in range(n):
            answer.append([])
            for j in range(m):
                answer[i].append(2*(row[i]+column[j])-(n+m))
        return answer