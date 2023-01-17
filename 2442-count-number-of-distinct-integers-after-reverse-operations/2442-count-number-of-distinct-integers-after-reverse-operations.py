class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = set(nums)
        
        for number in nums:
            answer.add(int(str(number)[::-1]))
        
        return len(answer)