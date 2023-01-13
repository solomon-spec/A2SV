class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        sum = 0
        for number in nums:
            sum+=number
            answer.append(sum)
        
        return answer