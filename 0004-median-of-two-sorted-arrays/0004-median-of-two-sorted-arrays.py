class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        num.sort()
        i = len(num)
        if i % 2 == 1:
            return num[i/2]
        else:
            print(num)
            return float(num[i/2] + num[(i/2) -1])/2