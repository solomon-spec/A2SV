class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        mxm,mnm = max(nums),min(nums)
        _range = mxm - mnm
        
        min_arr = [0]*(_range + 1)
        max_arr = [0]*(_range + 1)
        for i,num in enumerate(nums):
            index =  - (mxm - num)
            if mxm != num:max_arr[index] += cost[i]
            
            index = (mnm - num)
            if mnm != num: min_arr[index] += cost[i]
                
        max_arr = list(accumulate(accumulate(max_arr)))
        min_arr = list(accumulate(accumulate(min_arr)))[::-1]
        ans = inf
        
        for i,j in zip(min_arr,max_arr):
            ans = min(ans,i+j)
        return ans            
        