class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        diffchar = 0
        dic = defaultdict(int)
        l = r = 0
        maxlen = 0
        while r < len(s):
            dic[s[r]] += 1
            r += 1
            maxx = max(dic.values())
            if r-l - maxx <= k:
                maxlen = max(maxlen,r-l)
            else:
                dic[s[l]] -= 1
                l += 1
        if r-l - maxx <= k:
            maxlen = max(maxlen,r-l)
        return maxlen