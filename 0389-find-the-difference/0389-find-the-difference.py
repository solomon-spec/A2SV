class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        con = Counter(t)
        for i in s:
            con[i] -= 1
        for i in con:
            if con[i] == 1: return i