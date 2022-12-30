class Solution(object):
    def nearestValidPoint(self, x, y, points): 
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        nearest = -1
        for point in points:
            if point[0]==x or point[1] ==y:
                distance = (point[0]-x)**2 +(point[1]-y)**2
                if nearest != -1 and distance < (points[nearest][0]-x)**2 +(points[nearest][1]-y)**2:
                    nearest = points.index(point)
                elif nearest  == -1:
                    nearest = points.index(point)
        return nearest