class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        direction = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        row,col = len(board),len(board[0])
        self.mat = board
        x = click[0]
        y = click[1]
        
        if board[x][y] == "M":
            self.mat[x][y] = "X"
            return self.mat
        def is_valid(r,c):
            if 0 <= r < row and 0 <= c < col:return True
            return False
        
        def dfs(r,c,visited):
            cur_mine = 0
            for i,j in direction:
                x,y = r+i,c+j
                if is_valid(x,y):
                    if board[x][y] == "M": cur_mine += 1
            if cur_mine == 0:
                self.mat[r][c] = "B"
                for i,j in direction:
                    x,y = r+i,c+j
                    if is_valid(x,y) and (x,y) not in visited: 
                        visited.add((x,y))
                        dfs(x,y,visited)
            else:self.mat[r][c] = str(cur_mine)
                
        dfs(click[0],click[1],set([(click[0],click[1])]))
        return self.mat
                    
            
            