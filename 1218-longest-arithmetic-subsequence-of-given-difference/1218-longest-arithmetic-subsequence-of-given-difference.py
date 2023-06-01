class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = defaultdict(int)
        for i in arr:memo[i] = max(memo[i],memo[i-difference]+1)
        return max(memo.values())
                