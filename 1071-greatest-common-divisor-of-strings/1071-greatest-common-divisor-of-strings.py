class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        maxx = 0
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        for i in range(1,len(str1)+1):
            if str1[:i] *(len(str2)/i) == str2 and str1[:i] *(len(str1)/i) == str1:
                maxx = i
        return str1[:maxx]
        
        