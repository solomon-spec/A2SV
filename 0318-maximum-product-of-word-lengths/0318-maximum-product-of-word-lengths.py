class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxx = 0
        def check_same(n1,n2):
            if n1 & n2 != 0: return True
            return False
        
        arr = []
        for i in words:
            word1 = 0
            for x in i: word1 |= (1<<(ord(x)-97))
            arr.append(word1)
            
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if not check_same(arr[i],arr[j]): maxx = max(maxx,len(words[i])*len(words[j]))
                if maxx ==26*26: return maxx
                
        return maxx             