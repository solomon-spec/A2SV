class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = sorted(nums1 + nums2)
        i = len(num)
        if i % 2 == 1:
            return num[i/2]
        else:
            print(num)
            return (num[i/2] + num[(i/2) -1])/2.0