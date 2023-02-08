class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: int
        """
        count = 0
        answer = 0
        count2 = 0
        cot = False if nums[0] >= left else True
        for i in range(len(nums)):
            if nums[i] > right:
                answer += (count * (count + 1))/2
                count = 0
            else:
                count += 1
            if nums[i] < left:
                cot = True
                count2 += 1
            elif nums[i] >= left and cot:
                cot = False
                answer -= (count2 * (count2 + 1))/2
                count2 = 0
        answer += (count * (count + 1))/2
        answer -= (count2 * (count2 + 1))/2
        return int(answer)