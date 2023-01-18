class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        smaller_number = 0
        count = 0
        for num in nums:
            if num < target:
                smaller_number += 1
            elif num == target:
                count +=1
        if count == 0:
            return []
        else:
            answer = [i+smaller_number for i in range(count)]
            return answer