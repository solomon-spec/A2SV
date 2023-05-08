class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(nums2)): heap.append([nums1[0]+nums2[i],nums1[0],nums2[i],0])
        heapify(heap)
        ans = []
        while k > 0 and heap:
            x = heappop(heap)
            ans.append([x[1],x[2]])
            if x[3] < len(nums1) - 1:
                num = nums1[x[3]+1]
                heappush(heap,[num+x[2],num,x[2],x[3]+1])
            k -= 1
        return ans
