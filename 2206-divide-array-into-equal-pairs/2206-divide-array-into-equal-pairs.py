class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        num_count = Counter(nums)
        for i in num_count:
            if num_count[i] % 2 != 0: return False
        return True