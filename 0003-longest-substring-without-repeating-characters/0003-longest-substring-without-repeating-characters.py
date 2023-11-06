class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vis = defaultdict(int)
        ans = 0
        l = 0
        k = 1
        for r in range(len(s)):
            vis[s[r]] += 1
            while vis[s[r]] > k:
                vis[s[l]] -= 1
                l += 1
            ans = max(ans,r - l + 1)
            
        return ans