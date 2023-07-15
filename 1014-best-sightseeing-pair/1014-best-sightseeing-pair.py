class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        cur_max = 0
        ans = 0
        for i in range(1,len(values)):
            cur = (values[i] + values[cur_max]) - i + cur_max
            ans = max(ans,cur)
            if values[cur_max] - abs(i-cur_max) < values[i]:
                cur_max = i
        return ans