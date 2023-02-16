class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        arr = sorted(counts.values(), reverse = True)
        val = arr[k-1]
        ans = []
        for i in counts:
            if counts[i] >= val:
                ans.append(i)
        return ans