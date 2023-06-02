class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        coun = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in coun and i  -coun[nums[i]] <= k:
                return True
            else:
                coun[nums[i]] = i
        return False