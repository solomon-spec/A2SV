class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        dic = Counter(t)
        dic2 = defaultdict(int)
        r = l = 0
        index = []
        while r < len(s):
            isequal = True
            for i in dic:
                if dic[i] > dic2[i]:
                    isequal = False
            if not isequal:
                dic2[s[r]] += 1
                r +=1
            else:
                if not index or r-l + 1 <= index[1] - index[0]:
                    index = [l,r]
                    if dic2[s[l]] >dic[s[l]]:
                        index[0] += 1
                    #print(index)
                dic2[s[l]] -= 1
                l += 1
        isequal = True
        for i in dic:
            if dic[i] > dic2[i]:
                isequal = False
        #print(isequal,r,l)
        if isequal:
            while l < len(s) and dic2[s[l]] >= dic[s[l]]:
                #print(dic2)
                dic2[s[l]] -= 1
                if dic2[s[l]] < dic[s[l]]:
                    break
                l += 1
            print(dic2,r-l+1)
            if not index or r-l + 1 <= index[1] - index[0]:
                index = [l,r]
                
        if not index:
            return ""
        
        return s[index[0]:index[1]]
                
                