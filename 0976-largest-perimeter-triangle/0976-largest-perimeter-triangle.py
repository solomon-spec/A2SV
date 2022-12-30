class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        pt1= len(nums)-3
        pt2= len(nums)-2
        pt3  = len(nums)-1
        for i in range(len(nums)-2):
            if nums[pt1]+nums[pt2]> nums[pt3]:
                return nums[pt1]+nums[pt2]+nums[pt3]
            else:
                pt1 -=1
                pt2 -=1
                pt3-=1
        return 0 
        """
        :type nums: List[int]
        :rtype: int
        """
        