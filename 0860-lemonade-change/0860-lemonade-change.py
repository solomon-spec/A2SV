class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = defaultdict(int)
        
        for bill in bills:
            if bill == 20:
                if dic[10] > 0 and dic[5] > 0: 
                    dic[10] -= 1
                    dic[5] -= 1
                elif dic[5] > 2:
                    dic[5] -= 3
                else:
                    return False
            elif bill == 10:
                if dic[5] > 0: dic[5] -= 1
                else: return False
                dic[10] += 1
            else: dic[5] += 1
        return True