class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        answer = len(strs[0])
        for i in range(len(strs[0])):
            for x in range(len(strs)-1):
                if strs[x][i]>strs[x+1][i]:
                        answer-=1
                        break
        return len(strs[0]) - answer
