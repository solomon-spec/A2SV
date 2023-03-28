class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quick_select(l,r):
            piv, p = nums[r], l
            
            for i in range(l,r):
                if nums[i] <= piv:
                    nums[i],nums[p] = nums[p], nums[i]
                    p += 1
                
            nums[p],nums[r] = nums[r], nums[p] 

            if p > k: return quick_select(l,p-1)
            elif p < k: return quick_select(p + 1,r)
            else: return nums[p]
        return quick_select(0,len(nums)- 1)