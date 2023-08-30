class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        r = 0
        pairs = 0
        ans = 0
        for i,num in enumerate(nums):
            while pairs < k:
                if r >= len(nums):break
                dic[nums[r]] += 1
                pairs += dic[nums[r]]-1
                r += 1
            if pairs >= k:
                ans += len(nums) + 1 - r
            dic[num] -= 1
            pairs -= dic[num]
        return ans
            
            