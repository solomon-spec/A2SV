class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s.rstrip()
        words  = s.split()
        print(words)
        return len(words[-1])