class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        dire = [(0,1),(1,0),(-1,0),(-1,-1)]
        n = len(board)
        m = len(board[0])
        
        def is_valid(x,y):
            if 0 <= x < n  and 0 <= y < m and board[x][y] == 'X':
                return True
            return False
        
        for i in range(n):
            for j in range(m):
                if not is_valid(i-1,j) and not is_valid(i,j-1) and board[i][j] == 'X':
                    count += 1
        return count
                