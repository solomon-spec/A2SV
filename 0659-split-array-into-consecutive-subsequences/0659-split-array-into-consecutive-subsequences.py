class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        tails = defaultdict(list)
        for n in nums:
            if tails[n - 1]:
                heappush(tails[n], heappop(tails[n - 1]) + 1)
            else:
                heappush(tails[n], 1)
        for i in tails:
            if len(tails[i]) > 0 and heappop(tails[i]) < 3: return False
        return True
        
    