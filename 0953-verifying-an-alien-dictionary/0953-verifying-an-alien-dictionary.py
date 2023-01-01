class Solution(object):
    def isAlienSorted(self, words, order):
        wordorder = {i:j for j, i in enumerate(order)}
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j ==len(words[i+1]):
                    return False
                elif wordorder[words[i][j]] > wordorder[words[i+1][j]]:
                    return False
                elif wordorder[words[i][j]] < wordorder[words[i+1][j]]:
                    break
        return True
        
            
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        