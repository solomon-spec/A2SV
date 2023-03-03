class Solution:
    def gridGame(self, grids: List[List[int]]) -> int:
        nums1 = [0] +list(accumulate(grids[0]))
        nums2 = [0] + list(accumulate(grids[1]))
        maxx = None
        #print(nums1,nums2)
        for i in range(1,len(nums1)):
            cur = max(nums2[i-1],nums1[-1] - nums1[i])
            if not maxx or cur < maxx:
                maxx = cur
        return maxx

        
        