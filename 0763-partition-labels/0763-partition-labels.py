class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        summ = 0 
        start = 0
        last = len(s) - 1
        answer = []
        while start <= last:
            
            end= s.rfind(s[start])
            while start < end:
                end = s.rfind(s[start]) if s.rfind(s[start]) > end else end
                start += 1
            start = end + 1
            
            answer.append(start - summ)
            summ += answer[-1]
        return answer