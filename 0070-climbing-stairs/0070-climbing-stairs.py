class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1,2]
        if n < 3: return n
        for i in range(2,n): arr.append(arr[-1]+arr[-2])
        return arr[-1]