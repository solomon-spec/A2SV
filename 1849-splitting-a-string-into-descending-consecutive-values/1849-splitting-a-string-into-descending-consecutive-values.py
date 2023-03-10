class Solution:
    def splitString(self, s: str) -> bool:
        result = []
        bol  = False
        
        def backtrack(s):
            nonlocal bol
            if not s:
                if len(result) > 1:
                    bol = True
                return
            for i in range(1,len(s)+1):
                val = int(s[:i])
                if not result or val + 1 == result[-1]:
                    result.append(val)
                    backtrack(s[i:])
                    
            if result:
                result.pop()
            return
        backtrack(s)
        return bol