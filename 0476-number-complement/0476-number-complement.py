class Solution:
    def findComplement(self, num: int) -> int:
        ans = []
        while num:
            if num % 2 == 1: ans.append("0")
            else: ans.append("1")
            num //= 2
        return int("".join(reversed(ans)),2)
                
                
        
