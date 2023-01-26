class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1_len,word2_len = len(word1), len(word2) 
        answer = ""
        pointer1,pointer2 = 0,0
        while pointer1 < word1_len and pointer2 < word2_len:
            if word1[pointer1] > word2[pointer2]:
                answer += word1[pointer1]
                pointer1 += 1
            
            elif word1[pointer1] < word2[pointer2]:
                answer += word2[pointer2]
                pointer2 += 1
            else:
                if word1[pointer1:] > word2[pointer2:]:
                    answer += word1[pointer1]
                    pointer1 += 1
            
                else:
                    answer += word2[pointer2]
                    pointer2 += 1
                
        answer += word1[pointer1:] +word2[pointer2:]
        return answer