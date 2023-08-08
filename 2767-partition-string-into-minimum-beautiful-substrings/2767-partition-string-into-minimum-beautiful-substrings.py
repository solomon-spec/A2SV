class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [0] + [inf] * n
        for i in range(n):
            if s[i] == '1':
                cur = 0
                for j in range(i, n):
                    cur = cur * 2 + int(s[j])
                    if 15625 % cur == 0:
                        dp[j + 1] = min(dp[j + 1], dp[i] + 1)
        return dp[n] if dp[n] < inf else -1