class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = Counter(s1)
        l  = r = 0
        dic2 = defaultdict(int)
        while r <= len(s2):
            if dic == dic2:
                return True
            else:
                isgreater = True
                for i in dic:
                    if dic[i] > dic2[i]:
                        isgreater = False
           
            if isgreater:
                dic2[s2[l]] -= 1
                if dic2[s2[l]] == 0:
                    del dic2[s2[l]]
                l += 1
            else:
                if r < len(s2):
                    dic2[s2[r]] += 1
                r += 1
     
        if dic == dic2:
            return True
        return False
            
            
                