class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        right  = len(nums) - 1
        answer = 0
        while left < right:
            if nums[left] + nums[right] == k:
                answer += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1
        
        return answer