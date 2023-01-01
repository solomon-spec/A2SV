from collections import defaultdict 
class Solution(object):
    def findWinners(self, matches):
        answer = [[],[]]
        hashtable = defaultdict(int)
        for match in matches:
            hashtable[match[1]]+=1
            if hashtable[match[0]] == 0:
                hashtable[match[0]] == 0
                
        for club in hashtable:
            if hashtable[club]==0:
                answer[0].append(club)
            elif hashtable[club]==1:
                answer[1].append(club)
        answer[0].sort()
        answer[1].sort()
        return answer
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        