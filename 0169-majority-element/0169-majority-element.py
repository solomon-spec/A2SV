class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        result = 0
        for number in nums:
            if count == 0:
                result = number
            count+= (1 if number == result else -1)
        return result
    