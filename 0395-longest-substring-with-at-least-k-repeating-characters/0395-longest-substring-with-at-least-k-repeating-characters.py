class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
       
        def rec(s):
            if not s:
                return 0
           
            count = Counter(s)
            
            if min(count.values()) >= k:
                return len(s)
            if max(count.values()) < k:
                return 0
            
            ans = 0
            for i in count:
                if count[i] < k:
                    l = s.find(i)
                    r = s.rfind(i)
                    ans = max(ans,rec(s[:r]),rec(s[l+1:]))
                    break
            return ans
        return rec(s)