class Solution:
    def isThree(self, n: int) -> bool:
        if n == 1:
            return False
        num1 = int(sqrt(n))
        num = num1 **2
        if num  != n :
            return False
        for i in range(2,num1):
            if num1 % i == 0:
                return False
        return True