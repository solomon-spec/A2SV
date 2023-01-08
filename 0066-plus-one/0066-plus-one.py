class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        last = -1
        digits[last]+=1
        while digits[last] == 10 and last*(-1)<len(digits):
            digits[last] = 0
            digits
            last-=1
            digits[last]+=1
            
        if digits[0] == 10:
            digits[0]=0
            digits.insert(0,1)
            
        return digits    
            
        
        