class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ssort = list(s)
        ssort.sort()
        tsort = list(t)
        tsort.sort()
        #print(ssort,tsort)
        return ssort==tsort
        