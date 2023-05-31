class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        def dp(o,c,ans):
            if o == n and c == n:
                self.ans.append(ans)
                return
            if  o == c: 
                dp(o+1,c,ans+"(")
                return 
            if o < n:
                dp(o+1,c,ans+"(")
            dp(o,c+1,ans+")")
        dp(0,0,"")       
        return self.ans
            
            
            