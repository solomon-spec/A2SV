class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        tries = minutesToTest//minutesToDie
        ans = 0
        while (tries+1)**ans < buckets: ans += 1
        return ans
    
                