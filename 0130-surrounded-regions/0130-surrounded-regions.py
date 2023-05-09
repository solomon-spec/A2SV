class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        direc = [(1,0),(0,1),(-1,0),(0,-1)]
        def is_valid(r,c):
            if 0 < r < len(board) and 0 < c < len(board[0]): return True
            return False
        def is_corner(r,c):
            if r == 0 or r == len(board) - 1 or c == 0 or c == len(board[0]) - 1: return True
            return False
        def dfs(r,c,visited):
            nonlocal board
            visited.add((r,c))
            board[r][c] = "Z"            
            for i,j in direc:
                
                x,y = r + i, c + j
                if is_valid(x,y) and board[x][y] == "O":
                    dfs(x,y,visited)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if is_corner(i,j) and board[i][j] == "O": 
                    dfs(i,j,set())
                    
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = "O" if board[i][j] == "Z" else "X"
