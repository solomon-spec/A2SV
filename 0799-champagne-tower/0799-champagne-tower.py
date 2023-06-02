class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        ans = [[0]*i for i in range(1,query_row+2)]
        
        ans[0][0] = poured
        
        for i in range(1,query_row+1):
            for j in range(i+1):
                if j == 0: ans[i][j] = (ans[i-1][j]-1)/2
                elif j == i: ans[i][j] = (ans[i-1][j-1]-1)/2
                else: ans[i][j] = max(0,(ans[i-1][j-1]-1)/2)+ max(0,(ans[i-1][j]-1)/2)
                ans[i][j] = max(0,ans[i][j])
        return min(1,ans[query_row][query_glass])
        