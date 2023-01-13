class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        answer_set = set()
        
        for number in nums2:
            if number in set1:
                answer_set.add(number)
        return list(answer_set)