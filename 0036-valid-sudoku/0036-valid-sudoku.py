class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_map = defaultdict(set)
        column_map = defaultdict(set)
        box_map = defaultdict(set)
        
        for row in range(9):
            for column in range(9):
                if board[row][column] in row_map[row]:
                    return False
                elif board[row][column] !=".":
                    row_map[row].add(board[row][column])
                    
                if board[row][column] in column_map[column]:
                    return False
                elif board[row][column] !=".":
                    column_map[column].add(board[row][column])
                    
                if board[row][column] in box_map[tuple([row//3,column//3])]:
                    return False
                elif board[row][column] !=".":
                    box_map[tuple([row//3,column//3])].add(board[row][column])
                  
        return True