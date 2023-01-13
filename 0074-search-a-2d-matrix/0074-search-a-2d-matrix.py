class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        col_len = len(matrix[0])
        start = 0
        end = col_len*len(matrix) - 1
        
        while start <= end:
           
            middle = (start+end)//2
            print(middle)
            row = middle // col_len
            column = middle % col_len
            
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                end = middle - 1
            else:
                start = middle + 1
       
        return False