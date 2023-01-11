class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = defaultdict(int)
        pt1,pt2 = 0,0
        maxx = 0
        while pt2<len(s):
            #print(letters)
            if letters[s[pt2]] >0:
                letters[s[pt1]] -=1
                if letters[s[pt1]] == 0:
                    del letters[s[pt1]]
                pt1+=1
            else:
                letters[s[pt2]] = 1
                pt2+=1
            if len(letters) > maxx:
                maxx = len(letters)
        return maxx
                
                