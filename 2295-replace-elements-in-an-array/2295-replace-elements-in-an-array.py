class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = defaultdict(int)
        for i in range(len(nums)):
            dic[nums[i]] = i
            
        for i,j in operations:
            dic[j] = dic[i]
            dic[i] = -1
        for i in dic:
            if dic[i] != -1: nums[dic[i]] = i
        return nums