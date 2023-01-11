class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        queens = set(map(tuple, queens))
        direction = [(0,-1),(0,1),(-1,0),(1,0),(-1,1),(1,-1),(-1,-1),(1,1)]
        answer = []
        for dirc in direction:
            row = king[0]
            column = king[1]
            
            while 0 <= row < 8 and 0 <= column < 8:
                if (row,column) in queens:
                    answer.append([row,column])
                    break
                row+=dirc[0]
                column+=dirc[1]
                    
        return answer
                    