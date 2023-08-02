class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res  = []
        numm = 0
        def backtrack(num):
            nonlocal numm
            if len(num) == len(nums):
                res.append(num.copy())
                return
            
            for i in range(len(nums)):
                if numm & (1<<i) == 0:
                    num.append(nums[i])
                    numm |= (1<<i)
                    backtrack(num)
                    num.pop()
                    numm &= ~(1<<i)
            
        
        
        backtrack([])
        return res