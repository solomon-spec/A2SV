class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        position = []
        answer = []
        for i in range(len(boxes)):
            if boxes[i] =="1":
                position.append(i)
        
        for i in range(len(boxes)):
            answer.append(0)
            for x in position:
                answer[i]+=abs(i-x)
        return(answer)