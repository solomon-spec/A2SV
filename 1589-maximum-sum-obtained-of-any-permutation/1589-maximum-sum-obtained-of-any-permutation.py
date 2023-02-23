class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pre = [0]*(len(nums) + 1)
        for l,r in requests:
            pre[l] += 1
            pre[r + 1] -= 1
        prefix = sorted(accumulate(pre))
        nums.sort()
        answer = 0
        print(prefix,nums)
        for i in range(len(nums)):
            answer +=(nums[i]*prefix[i + 1])
        return answer % (10**9 + 7)