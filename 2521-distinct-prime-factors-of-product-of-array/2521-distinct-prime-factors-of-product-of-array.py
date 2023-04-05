class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def isPrime(n):
            if n == 1: return False
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False

            return True
        div = set()
        for i in nums:
            num = i
            d = 1
            while d*d <= num:
                if num % d == 0:
                    div.add(d)
                    div.add(num//d)
                d+=1
            
        answer = 0
        for i in div:
            if isPrime(i):
                answer += 1
        return answer
            