class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        arr = sorted(list(count),reverse = True)
        if count[0] % 2 == 1: return False
    
        for num in arr:
            if not count[num] or num == 0:    
                continue
            
            elif (num > 0 and num % 2 != 0) or count[num*(2**(-num/abs(num)))] < count[num]:  

                return False
            
            else:
                count[num*(2**(-num/abs(num)))] -= count[num]
        return True
                     
        