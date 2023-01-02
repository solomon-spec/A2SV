from collections import defaultdict
class Solution(object):
    def similarPairs(self, words):
        hashtable = defaultdict(int)
        answer = 0
        for word in words:
            value  = tuple(set([i for i in word]))
            hashtable[value] +=1
        
        for sets in hashtable:
            if hashtable[sets]>1:
                answer+=hashtable[sets]*(hashtable[sets]-1)/2
        return(answer)
            