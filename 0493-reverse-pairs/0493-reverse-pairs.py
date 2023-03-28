class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        total = 0
        def merge(arr):
            nonlocal total
            if len(arr) <= 1:
                return arr
            
            left = merge(arr[:len(arr)//2])
            right  = merge(arr[len(arr)//2:])
            for i in left:
                total += bisect_left(right,i/2)
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
        merge(nums)
        return total