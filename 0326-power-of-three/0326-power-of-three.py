class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        print(int(n/3* 3),n)
        if n <= 0 or int(n/3* 3) != n:
            return False
        elif n == 1:
            return True
        else:
            return self.isPowerOfThree(n/3)