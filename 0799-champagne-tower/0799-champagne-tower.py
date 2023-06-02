class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        @lru_cache
        def dp(x,y):
            if x == 0 and y == 0: return poured -1
            if y > x or y < 0: return 0
            return max(0,dp(x-1,y)/2) + max(0,dp(x-1,y-1)/2) -1
        return min(1,dp(query_row,query_glass) + 1)
        