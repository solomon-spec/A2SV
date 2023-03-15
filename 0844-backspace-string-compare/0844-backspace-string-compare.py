class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ls = []
        lt = []
        for i in s:
            if i != "#":
                ls.append(i)
            else:
                if ls:
                    ls.pop()
        for i in t:
            if i != "#":
                lt.append(i)
            else:
                if lt:
                    lt.pop()
                
        return ls == lt