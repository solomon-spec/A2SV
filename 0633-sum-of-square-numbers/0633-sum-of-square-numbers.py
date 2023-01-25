class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left = 0
        right = 46400
        if c == 0:
            return True
        while left <= right:
            num1 = left**2
            num2 = right**2
            if num1 + num2 > c:
                right -= 1
            elif num1 + num2 < c:
                left += 1
            else:
                return  True
       
        return False