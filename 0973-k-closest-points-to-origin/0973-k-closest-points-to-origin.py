class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dictionary = {}
        distances = []
        answer = []
        for point in points:
            distance = point[0]**2+point[1]**2
            distances.append(distance)
            if distance in dictionary:
                dictionary[distance].append(point)
            else:
                dictionary[distance] = []
                dictionary[distance].append(point)
        distances.sort()
        
        i = 0
        while i<k:
            for j in dictionary[distances[i]]:
                answer.append(j)
                i+=1
                
        return answer
                
            
        
        