class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        dic2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                     return False
            else:
                dic[s[i]] = t[i]
            if t[i] in dic2:
                if dic2[t[i]] != s[i]:
                     return False
            else:
                dic2[t[i]] = s[i]
        return True