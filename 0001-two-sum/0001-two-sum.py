class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = defaultdict(int)
        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                return [hash_map[target-nums[i]], i]
            else:
                hash_map[nums[i]] = i
       
     
                    
                    
                    
                    
                    
                    
                    
                    