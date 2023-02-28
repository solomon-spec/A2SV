class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def other(x):
            if x == 0:
                return(["0"])
            else:
                val = other(x - 1)
                return other(x - 1) +["1"] + list(reversed(["0" if i == "1" else "1" for i in val]))
        vall = other(n-1)
        return vall[k - 1]