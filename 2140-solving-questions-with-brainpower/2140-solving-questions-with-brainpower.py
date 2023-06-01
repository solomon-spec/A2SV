class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        arr = [0]*(len(questions) + 1)
        for i in range(len(arr)-2,-1,-1):
            if questions[i][1] + i + 1 < len(arr):
                arr[i] = max(arr[i+1],arr[i+questions[i][1]+1] + questions[i][0])
            else:
                arr[i] = max(arr[i+1],questions[i][0])
        return arr[0]