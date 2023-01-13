class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        answer = 0
        
        while num !=0:
            if num % 2 == 0:
                num/=2
            else:
                num-=1
            answer+=1
        return answer