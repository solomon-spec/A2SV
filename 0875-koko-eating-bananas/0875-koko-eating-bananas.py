class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        while l <= r:
            answer = 0
            mid = (l + r)//2
            #print(mid)
            for i in piles:
                answer += ceil(i/mid)
            #print(answer)
            if answer > h:
                l = mid + 1
            else:
                r = mid - 1
        
        if l > 1:
            answer = 0
            for i in piles:
                answer += ceil(i/(l-1))
        print(answer,mid)
        return l
                