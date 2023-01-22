class Solution(object):
    def thirdMax(self, nu):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nu)
        if len(nums)<3:
            return max(nums)
        max1 = min(nums)
        max2 = max1
        max3 = max1
        
        for num in nums:
            #print(max1,max2,max3)
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
        return max3
            