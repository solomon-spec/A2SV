class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        words = s.split()
        len_words = [len(i) for i in words]
        newnew = []
        max_len_word  = max(len_words)
        new_word = ["" for i in range(max_len_word)]
        for word in words:
            for i in range(max_len_word):
                if len(word)>i:
                    new_word[i]+=word[i]
                else:
                    new_word[i]+=" "
        for word in new_word:
            newnew.append( word.rstrip())
        return newnew
                    
            
            
            