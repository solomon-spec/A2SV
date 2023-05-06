class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = []
        for i in range(len(matrix)):
            heappush(ans,[matrix[i][0],i,0])
        while k > 1: 
            x = heappop(ans)
            if len(matrix[x[1]]) > x[2]+1:
                heappush(ans,[matrix[x[1]][x[2]+1],x[1],x[2]+1])
            k -= 1
        x = heappop(ans)
        return x[0]