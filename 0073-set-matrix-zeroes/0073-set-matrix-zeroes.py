class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        set_row = set()
        set_column = set()
        
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 0:
                    set_row.add(row)
                    set_column.add(column)
                    
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if row in set_row or column in set_column:
                    matrix[row][column] = 0
            