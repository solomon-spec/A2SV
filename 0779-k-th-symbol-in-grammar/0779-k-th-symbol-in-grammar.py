class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def bit(n,k):
            if n == 1:
                return 0
            else:
                ans  = bit(n-1,ceil(k/2))
                if k % 2 != 0:
                    return ans
                if ans == 0: return 1
                return 0
        return bit(n,k)
        