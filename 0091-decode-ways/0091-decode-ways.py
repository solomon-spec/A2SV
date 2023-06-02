class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dp(i):
            if i == len(s):return 1
            if i == len(s) - 1:
                if s[i] != "0":return 1
                else: return 0
            cur = s[i:i+2]
            if i not in memo:
                print(cur)
                if int(cur) < 10: memo[i] = 0
                elif int(cur) <= 26: memo[i] = dp(i+2) + dp(i+1)
                else: memo[i] = dp(i+1)
            return memo[i]
        return dp(0)