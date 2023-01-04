from collections import defaultdict
class Solution(object):
    def countPairs(self, de):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        powertwo = []
        count = 0
        dic = defaultdict(int)
        for i in range(0,22):
            powertwo.append(2**i)
        for i in de:
            for j in powertwo:
                dic[j-i]+=1 
        for i in de:
            if i in dic:
                count+=dic[i]
        for i in de:
            if i*2 in powertwo:
                count-=1
            
        return int(count/2) % (10**9+7)
        
        