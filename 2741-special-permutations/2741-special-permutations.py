class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        mod = 1_000_000_007
        n = len(nums)
        memo = {}
        
        def dp(prev,mask):
            if bin(mask).count('1') == n:
                return 1
            state = (prev,mask)
            
            if state not in memo:
                ans = 0
                for i in range(n):
                    if not mask & (1<<i) and (prev % nums[i] == 0 or nums[i] % prev == 0):
                        ans += dp(nums[i],mask | (1<<i)) % mod
                memo[state] = ans 
                
                
            return memo[state] % mod
        ans = 0
        for i in range(n):
            ans += dp(nums[i],(1<<i)) % mod
        return ans  % mod
        