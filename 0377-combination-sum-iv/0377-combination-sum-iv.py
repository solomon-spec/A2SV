class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        arr = [1] + [0]*target
        for i in range(1,target+1):
            for x in nums:
                if i-x >= 0:
                    arr[i] += arr[i-x]
        return arr[target]