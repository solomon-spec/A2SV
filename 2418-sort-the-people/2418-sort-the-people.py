class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        """for i in range(len(names)):
            for j in range(len(names)-1):
                if heights[j] < heights[j+1]:
                    heights[j],  heights[j+1] = heights[j + 1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
        return names"""
        dic ={}
       
        answer = []
        for i in range(len(names)):
            dic[heights[i]] = names[i]
            
        heights.sort()
        
        for i in range(len(names)-1,-1,-1):
            answer.append(dic[heights[i]])
        
        return answer
        