class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set()
        sort = sorted(nums)
        leng = len(nums)
        for i in range(leng/2):
            nums_set.add(sort[i] + sort[-(i+1)])
        return len(nums_set)