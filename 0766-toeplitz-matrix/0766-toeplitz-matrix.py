class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        dictionary = {}
        
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if row - column not in dictionary:
                    dictionary[row - column] = matrix[row][column]
                    
        for row in range(len(matrix)):
            for column in range(len(matrix[0])): 
                if dictionary[row - column] != matrix[row][column]:
                    return False
                        
        return True
        