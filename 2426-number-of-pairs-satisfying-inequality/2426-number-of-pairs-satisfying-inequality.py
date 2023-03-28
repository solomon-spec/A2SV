class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        new_arr = []
        total = 0
        
        for i in range(len(nums2)):
            new_arr.append(nums1[i] - nums2[i])
        total = 0
        
        def merge(arr):
            nonlocal total
            if len(arr) <= 1:
                return arr
            
            left = merge(arr[:len(arr)//2])
            right  = merge(arr[len(arr)//2:])
            
            for i in left:
                total +=len(right) - bisect_left(right,i - diff)
            ans = []
            l = r = 0
            while l < len(left) or r < len(right):
                if l >= len(left) or (r < len(right) and left[l] >= right[r]):
                    ans.append(right[r])
                    r += 1
                else:
                    ans.append(left[l])
                    l += 1
    
            return ans
        merge(new_arr)
        return total
            
            
            
            
            
            
            
            
            
            
            