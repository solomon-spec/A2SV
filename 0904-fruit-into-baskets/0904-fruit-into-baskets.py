class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = defaultdict(int)
        r = l = 0
        maxx =  -inf
        while r < len(fruits):
            if len(dic) <= 2:
                maxx = max(maxx,r-l)
                dic[fruits[r]] +=1
                r += 1
            else:
                #print(r,l)
                dic[fruits[l]] -= 1
                if dic[fruits[l]] == 0:
                    del dic[fruits[l]]
                l += 1
        if len(dic) <= 2:
            maxx = max(maxx,r-l)   
        return maxx