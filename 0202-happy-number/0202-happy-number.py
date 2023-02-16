class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        elif n < 10:
            return False
        else:
            num = str(n)
            ans = 0
            for i in num:
                ans += int(i)**2
            #print(ans)
            return self.isHappy(ans)