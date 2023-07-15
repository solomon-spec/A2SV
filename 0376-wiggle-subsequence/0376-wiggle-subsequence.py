class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        inc = [0]*n
        dec = [0]*n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    inc[i] = max(inc[i],dec[j]+1)
                elif nums[i] < nums[j]:
                    dec[i] = max(dec[i],inc[j]+1)
        return max(max(dec),max(inc))+1