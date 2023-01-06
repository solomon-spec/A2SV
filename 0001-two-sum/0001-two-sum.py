class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums2 = [i for i in nums]
        nums.sort()
        pointer1 = 0
        pointer2 = len(nums)-1
        
        while pointer1 < pointer2:
            print(nums[pointer1],nums[pointer2])
            if nums[pointer1] + nums[pointer2] == target:
                break
            
            elif nums[pointer1] + nums[pointer2] > target:
                pointer2 -= 1
                
            else:
                pointer1 += 1
        if nums[pointer1]!= nums[pointer2]:
            return [nums2.index(nums[pointer1]),nums2.index(nums[pointer2])]
        else:
            return [nums2.index(nums[pointer1]), [i for i, n in enumerate(nums2) if n == nums[pointer1]][1]]
       
     
                    
                    
                    
                    
                    
                    
                    
                    