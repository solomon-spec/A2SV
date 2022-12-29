class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dictionary = defaultdict(list)
        distances = []
        answer = []
        for point in points:
            distance = point[0]**2+point[1]**2
            distances.append(distance)
            dictionary[distance].append(point)
        distances.sort()
        
        i = 0
        while i<k:
            for j in dictionary[distances[i]]:
                answer.append(j)
                i+=1
                
        return answer
                
            
        
        