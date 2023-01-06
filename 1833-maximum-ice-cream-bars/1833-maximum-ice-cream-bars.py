class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        ice_cream = 0
        costs.sort()
        
        for i in costs:
            if coins - i >= 0:
                coins-=i
                ice_cream+=1
        return ice_cream
                
            