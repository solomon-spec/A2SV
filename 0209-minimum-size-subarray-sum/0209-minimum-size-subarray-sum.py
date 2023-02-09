class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < target:
            return 0
        left = 0
        right = 0
        summ = nums[0]
        length = leng = len(nums)
        while right < leng:
            if summ < target:
                right += 1
                if not right < leng:
                    break
                summ += nums[right]
            else:
                if right - left + 1 < length:
                    length = right - left + 1
                summ -= nums[left]
                left += 1
        return length