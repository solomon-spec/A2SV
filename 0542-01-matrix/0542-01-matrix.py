class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dire = [[0,1],[1,0],[0,-1],[-1,0]]
        n, m = len(mat), len(mat[0])
        def is_valid(i,j):
            if 0 <= i < n and 0 <= j <m: return True 
            return False
        ans = [[-1]*m for i in range(n)]
        queue = deque()
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append([i,j,0])
                    ans[i][j] = 0
        while queue:
            cur = queue.popleft()
            k = cur[2]
            for i,j in dire:
                x = i + cur[0]
                y = j + cur[1]
                if x==2 and y == 0: print(is_valid(x,y))
                if is_valid(x,y) and ans[x][y] == -1:
                    ans[x][y] = k + 1
                    queue.append([x,y,k+1])
        return ans