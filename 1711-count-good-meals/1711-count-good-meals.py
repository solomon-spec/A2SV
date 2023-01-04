# from collections import defaultdict
class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        powertwo = []
        count = 0
        dic = defaultdict(int)
        for i in range(0,22):
            powertwo.append(2**i)
        for i in deliciousness:
            for j in powertwo:
                if j-i in dic:
                    count+=dic[j-i]
            dic[i]+=1
            
        return int(count) % (10**9+7)
        
        