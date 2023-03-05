class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        r = sum(nums)
        l = 1
        while l <= r:
            mid = (l + r)//2
            total = 0
            for num in nums:
                total += ceil(num/mid)
            
            if total > threshold:
                l = mid + 1
            else:
                r = mid - 1
            #print(mid,total)
        return l