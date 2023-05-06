class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        summ = 0
        ans = []
        for i in range(len(heights)-1):
            if heights[i] < heights[i+1]:
                x = heights[i+1] - heights[i]
                if len(ans) < ladders: heappush(ans,x)
                else:
                    y = heappushpop(ans,x)
                    summ += y
                if summ > bricks:
                    return i
        return len(heights)-1
                