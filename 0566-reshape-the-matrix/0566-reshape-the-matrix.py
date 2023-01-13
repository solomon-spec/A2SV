class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(mat[0]) * len(mat) != r*c:
            return mat
        
        reshaped_matrix = [[0]*c for i in range(r)]
        index = 0
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                row = index//c
                column = index % c
                reshaped_matrix[row][column] = mat[i][j]
                index += 1
        return reshaped_matrix
            