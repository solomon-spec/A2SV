class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        answer = [set(),set()]
        set1 = set(nums1)
        set2 = set(nums2)
        
        for number in nums1:
            if number not in set2:
                answer[0].add(number)
        
        for number in nums2:
            if number not in set1:
                answer[1].add(number)
                
        return [list(answer[0]),list(answer[1])]
        