class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cur = Counter(s[:3])
        ans = 0
        for i in range(3,len(s)):
            if len(cur) == 3: ans += 1
            cur[s[i-3]] -= 1
            cur[s[i]] += 1
            x = list(cur.keys())
            #print(cur)
            for i in x: 
                if cur[i] < 1: del cur[i]
        if len(cur) == 3: ans += 1
        return ans