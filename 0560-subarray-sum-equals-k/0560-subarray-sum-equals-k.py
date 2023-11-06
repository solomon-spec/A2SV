class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        con = defaultdict(int)
        con[0] = 1
        ans = summ = 0
        for a in nums:
            summ += a
            ans += con[summ - k]
            con[summ]+= 1
        return ans