class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        for i in range(len(capacity)):
            capacity[i] -= rocks[i]
            
        capacity.sort()
        ans = 0
        
        while ans < len(capacity) and additionalRocks >= capacity[ans]:
            additionalRocks -= capacity[ans]
            ans += 1
        return ans