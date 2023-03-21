class Solution:
    def isAdditiveNumber(self, s: str) -> bool:
        
        
        result = []
        bol  = False
        def backtrack(s):
            nonlocal bol
            if not s:
                if len(result) > 2:
                    bol = True
                return
            for i in range(1,len(s)+1):
                val = int(s[:i])
                if len(str(val)) == i and (len(result)<2 or val == result[-1] + result[-2]):
                    result.append(val)
                    backtrack(s[i:])   
                    result.pop()
            return
        backtrack(s)
        return bol