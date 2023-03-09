class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res  = []
        
        def backtrack(num,arr):
            if len(num) == len(nums):
                res.append(num.copy())
                return
            
            for i in range(len(arr)):
                num.append(arr[i])
                backtrack(num,arr[:i] + arr[i+1:])
                num.pop()
            
        
        
        backtrack([],nums)
        return res
            