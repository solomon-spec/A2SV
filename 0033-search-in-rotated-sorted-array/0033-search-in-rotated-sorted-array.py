class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        f = nums[0]
        last = nums[-1]
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > last:
                l = mid + 1
            else:
                r = mid - 1
        pivot = l
        if pivot ==0:
            l = 0
            r = len(nums) -1
        
        elif target <= last:
            l = pivot
            r = len(nums)-1
        else:
            l = 0
            r = pivot - 1
        print(pivot,l,r)
        while l <= r:
            
            mid = (l + r)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        print(l)
        if 0 <= l < len(nums) and nums[l] == target:
            return l
        return -1
            
                
        
        
        
        
            