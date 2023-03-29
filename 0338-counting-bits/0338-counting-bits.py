class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0,1]
        if n == 0:
            return [0]
        for i in range(2,n + 1):
            if i % 2 == 0:
                ans.append(ans[i//2])
            else:
                ans.append(ans[i//2] + 1)
        return ans
           