class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dic = defaultdict(int)
        r = l = 0
        ans = 0
        while l <= len(s):
            if dic['a'] > 0 and dic['b'] > 0 and dic['c'] > 0:
                ans += len(s) - r + 1
            
                dic[s[l]] -= 1
                l += 1
            else:
                if r < len(s):dic[s[r]] += 1
                else: break
                r += 1
        return ans