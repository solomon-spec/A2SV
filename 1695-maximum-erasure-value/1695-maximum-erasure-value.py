class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = r = summ = 0
        maxx = 0
        dic = defaultdict(int)
        while r < len(nums):
            if nums[r] not in dic:
                dic[nums[r]]  += 1
                summ += nums[r]
                maxx = max(maxx, summ)
                r += 1
            else:
                dic[nums[l]] -= 1
                if dic[nums[l]] == 0:
                    del dic[nums[l]]
                    summ -= nums[l]
                    l+= 1
        return maxx