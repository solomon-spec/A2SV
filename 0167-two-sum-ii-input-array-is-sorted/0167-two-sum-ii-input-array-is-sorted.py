class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            num_sum  = numbers[left] + numbers[right]
            if num_sum == target:
                return [left + 1, right + 1]
            elif num_sum > target:
                right -= 1
            else:
                left += 1