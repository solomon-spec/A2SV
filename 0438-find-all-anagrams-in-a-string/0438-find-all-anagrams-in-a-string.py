class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        """pcount = Counter(p)
        window = Counter(s[:len(p)])
        answer = []
        wrong = 0
        for i in pcount:
            if pcount[i] != window[i]:
                wrong += 1
        for i in range(len(s)- len(p)):
            print(i,wrong, )
            if wrong == 0:
                answer.append(i)
            
            window[s[i]] -= 1
            window[s[i + len(p) ]] += 1
            if window[s[i]] == 0:
                del window[s[i]]
            
        if wrong == 0:
            answer.append(len(s) - len(p))
        return answer"""
        if len(p) > len(s):
            return []
        pcount = Counter(p)
        window = Counter(s[:len(p)])
        answer = []
        for i in range(len(s)- len(p)):
            #print(i,pcount, window)
            if pcount == window:
                answer.append(i)
            window[s[i]] -= 1
            window[s[i + len(p) ]] += 1
            if window[s[i]] == 0:
                del window[s[i]] 
        if pcount == window:
            answer.append(len(s) - len(p))
        return answer