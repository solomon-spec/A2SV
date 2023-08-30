class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sett = Counter(nums[:k])
        tot = sum(nums[:k])
        ans = 0
        for i in range(k,len(nums)):
            if len(sett) == k:
                ans = max(ans,tot)
            sett[nums[i]] += 1
            tot += nums[i]
            tot -= nums[i-k]
            sett[nums[i-k]] -= 1
            if sett[nums[i-k]] <= 0:
                del sett[nums[i-k]]
        if len(sett) == k: ans = max(ans,tot)
        return ans