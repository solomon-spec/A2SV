class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        
        def check(r,c):
            if 0 <= r < row and 0 <= c < col: return True
            return False
        dire = [(1,0),(0,1),(-1,0),(0,-1)]
        arr = []
        for r in range(row):
            for c in range(col):
                num = matrix[r][c]
                flag = True
                for i,j in dire:
                    a = r + i
                    b = c + j
                    if check(a,b) and matrix[a][b] > matrix[r][c]:
                        flag = False
                        break
                if flag: arr.append((r,c))
        memo = {}
        @cache
        def dp(r,c):
            
            ans = 1
            for i,j in dire:
                a = i + r
                b = j + c
                if check(a,b) and matrix[a][b] < matrix[r][c]:
                    
                    ans = max(ans,dp(a,b)+1)

            return ans
        ans = 0
        
        for a,b in arr:
            cur = dp(a,b)
            ans = max(ans,cur)
        return ans
        
                