class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l <= r:
            mid = (l + r)//2
            #print(mid)
            answer = 0
            cur = 0
            for i in weights:
                if cur + i <= mid: cur += i
                else:
                    answer += 1
                    cur = i
            if cur != 0: answer += 1
            #print(answer,mid)
            if answer <= days:
                r = mid - 1
            else:
                l = mid + 1
        return l