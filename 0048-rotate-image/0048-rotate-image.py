class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if row >= column:
                    matrix[row][column],matrix[column][row] = matrix[column][row], matrix[row][column]
        
        for row in range(len(matrix)):
            matrix[row].reverse()