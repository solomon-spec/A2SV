class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        answer = 0
        ans = []
        for i in range(len(piles)-2,len(piles)/3-1,-2):
            answer  += piles[i]
            ans.append(piles[i])
        print(ans)
        return answer   