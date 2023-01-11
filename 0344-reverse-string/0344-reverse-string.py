class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        pt1 = 0
        pt2 = len(s)-1
        while pt1 < pt2:
            s[pt1],s[pt2] = s[pt2],s[pt1]
            pt1+=1
            pt2 -=1