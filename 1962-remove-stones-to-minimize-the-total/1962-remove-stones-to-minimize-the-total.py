class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pile = [-i for i in piles]
        heapify(pile)
        while k > 0:
            x = heappop(pile)
            x = x//2
            heappush(pile,x)
            k -=1
        return -sum(pile)