class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leng = len(nums)
        stack = []
        answer = [-1]*leng
        for i in range(2*leng):
            while stack and nums[i%leng] > nums[stack[-1]]:
                index = stack.pop()
                answer[index] = nums[i%leng]
            if i < len(nums):
                stack.append(i)
        return answer
            