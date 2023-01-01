class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        strs = []
        strs.append(s[:spaces[0]])
        for i in range(1,len(spaces)):
            num1 = spaces[i]
            num2 = spaces[i-1]
            strs.append( s[num2:num1])
        strs.append(s[spaces[-1]:])
        return(" ".join(strs))
            