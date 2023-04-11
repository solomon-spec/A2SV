class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def SieveOfEratosthenes(num):
            prime = [True for i in range(num+1)]
            p = 2
            while (p * p <= num):
                if (prime[p] == True):
                    for i in range(p * p, num+1, p):
                        prime[i] = False
                p += 1
            return prime
        x = SieveOfEratosthenes(right)
        x[1] = False
        ans = [0,inf]
        pre = None
        for i in range(left,right+1):
            if x[i]:
                if pre: ans = min(ans,[pre,i],key = lambda x:x[1]-x[0])
                pre = i
        if ans[1] != inf: return ans
        else: return [-1,-1]