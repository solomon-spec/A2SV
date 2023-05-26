class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        dire = [(-1,0),(1,0),(0,1),(0,-1)]
        x,y = tuple(board[0]),tuple(board[1])
        visited = set([(x,y)])
        queue = deque([(x,y,0)])
        ans = ((1,2,3),(4,5,0))
        if (x,y) == ans: return 0
        def find_zero(x,y):
            if 0 in x: return [0,x.index(0)]
            else: return[1,y.index(0)]
            
        def is_valid(x,y):
            if 0 <= x < 2 and 0 <= y < 3: return True
            return False
        
        while queue:
            x,y,z = queue.popleft()
            indx,indy = find_zero(x,y)
            
            for i,j in dire:
                curx,cury = indx + i,indy + j
                if is_valid(curx,cury):
                    new_board = [list(x),list(y)]
                    new_board[indx][indy], new_board[curx][cury] = new_board[curx][cury],0
                    row1,row2 = tuple(new_board[0]),tuple(new_board[1])
                    if (row1,row2) == ans: return z+1
                    if (row1,row2) not in visited:
                        queue.append((row1,row2,z+1))
                        visited.add((row1,row2))
                    
        return -1      
                    
        