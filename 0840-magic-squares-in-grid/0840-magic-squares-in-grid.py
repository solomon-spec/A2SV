class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        answer = 0
        def sq_grid(row_start,column_start):
        
            dic = defaultdict(int)
            answer = [[0,0,0] for i in range(3)]
            answer_set = set()
            for row in range(3):
                for column in range(3):
                    answer[row][column] = grid[row_start + row][column_start + column]
                    answer_set.add(answer[row][column])
                    
            max_no = max(answer_set)
            if len(answer_set) != 9 or max_no > 9 or min(answer_set)<=0: 
                return 0
            
            
            for row in range(3):
                for column in range(3):
                    dic[str(row)] += grid[row+ row_start][column+column_start]
                    dic[str(column)+"c"] += grid[row + row_start][column + column_start]
                    
                    if row-column == 0:
                        dic[4] += grid[row+row_start][column+column_start]
                        
                    if row + column == 2:
                        dic[5] += grid[row+row_start][column+column_start]
            
            summ = dic[5]
            for num in dic:
                if dic[num] != summ:
                    return 0
            return 1
        
        for row in range(len(grid)-2):
            for column in range(len(grid[1])-2):
                answer += sq_grid(row,column)
                
        return  answer