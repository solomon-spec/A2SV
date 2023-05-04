class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_st = [-i for i in stones]
        heapify(neg_st)
        while len(neg_st) != 1:
            x = heappop(neg_st)
            y = heappop(neg_st)
            heappush(neg_st,x-y)
        return(-neg_st[0])