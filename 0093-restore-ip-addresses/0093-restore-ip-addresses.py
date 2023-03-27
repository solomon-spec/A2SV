class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        ans = []
        def backtrack(s):
            nonlocal ans
            nonlocal result
            if not s:
                if len(result)  ==  4:
                    ans.append(".".join(list(map(str,result))))
                return
            if len(result) > 4: return  
            for i in range(1,len(s)+1):
                val = int(s[:i])
                if len(str(val)) == i and (val <= 255):
                    result.append(val)
                    backtrack(s[i:])   
                    result.pop()
            return
        backtrack(s)
        return ans