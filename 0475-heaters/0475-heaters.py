class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        heaters.sort()
        max_len = -inf
        
        for h in houses:
            
            index = bisect_left(heaters,h)
            ans_h = inf
            
            # 2 4 6 7 -> 
            
            if index > 0:
                ans_h = abs(h - heaters[index-1])
            if index < len(heaters):
                ans_h = min(ans_h,abs(h - heaters[index]))
    
            max_len = max(max_len,ans_h)
        return max_len
                
            
            