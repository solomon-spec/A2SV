class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        has = {}
        answer = ""
        for word in words:
            has[word[-1]] = word[:-1]
        
        index_list = list(has.keys())
        index_list.sort()
        
        for i in index_list:
            answer+= has[i]+" "
        
        return answer[:-1]