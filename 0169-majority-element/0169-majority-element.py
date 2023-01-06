class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        result = nums[0]
        for number in nums:
            if number == result:
                count+=1
            else:
                if count==0:
                    result=number
                else:
                    count-=1
        return result