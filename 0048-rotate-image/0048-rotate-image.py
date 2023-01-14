class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        dic = defaultdict(list)
        row_len = len(matrix)-1
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                dic[row_len - row].append(matrix[row][column])    
        
        for column in dic:
            for num in range(row_len+1):
                matrix[num][column] = dic[column][num]