class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        dic = defaultdict(list)
        answer = []
        for row in range(len(mat)):
            for column in range(len(mat[0])):
                dic[row + column].append(mat[row][column])
        
        for diagonal_list in dic:
            if diagonal_list % 2 == 0:
                dic[diagonal_list].reverse()
                answer += dic[diagonal_list]
            else:
                answer.extend(dic[diagonal_list])
                
        return answer
            
                    
               