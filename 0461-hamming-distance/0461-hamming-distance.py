class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while x or y:
            if x % 2 != y % 2: ans += 1
            
            x //=2
            y //=2
        return ans