class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i in range(len(intervals)):
            intervals[i].append(i)
        intervals.sort()
        newj = []
        answer = [-1]*len(intervals)
        for i in intervals:
            newj.append(i[0])
        for i in intervals:
            ans = bisect_left(newj,i[1])
            if ans < len(intervals):
                answer[i[2]] = intervals[ans][2]
        return answer
                
        