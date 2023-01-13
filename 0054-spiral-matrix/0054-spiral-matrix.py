class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        answer = []
        max_row = len(matrix)-1
        max_column = len(matrix[0])-1
        
        min_row = 0
        min_column = 0
        direction = 0
        while (min_row < max_row or min_column < max_column) and len(matrix)*len(matrix[0])> len(answer):
            
            if direction == 0 :
                for i in range(max_column - min_column + 1 ):
                    answer.append(matrix[min_row][i+min_column])
                if min_row +1 < len(matrix):
                    min_row += 1
                else:
                    break
            elif direction == 1:
                for i in range(max_row - min_row + 1):
                    answer.append(matrix[min_row+i][max_column])
                if max_column > 0:
                    max_column -= 1
                else:
                    break
            elif direction == 2:
                for i in range(max_column - min_column + 1):
                    answer.append(matrix[max_row][ max_column-i])
                if max_row > 0:
                    max_row -= 1
                else:
                    break
            else:
                for i in range(max_row - min_row + 1):
                    answer.append(matrix[max_row - i][min_column])
                if min_column < len(matrix[0]):
                    min_column += 1
                else:
                    break
            direction +=1
            direction %=4
            print(min_column,max_column,min_row,max_row, direction)
         
        if len(matrix)*len(matrix[0])!= len(answer):
            answer.append(matrix[min_row][min_column])
        return answer
        