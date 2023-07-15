class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        mx = max(nums)
        numss = set()
        for num in nums:
            for i in range(mx+1):
                dp[(num,num-i)] = dp[(i,num-i)] + 2 if(i in numss and dp[(i,num-i)] == 0) else dp[(i,num-i)] + 1
            numss.add(num)
        x = max(dp.values())
        return x