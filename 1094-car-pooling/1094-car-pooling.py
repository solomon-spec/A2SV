class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minn = (min(trips, key = lambda x: x[1])[1])
        arr = [0]*((max(trips, key = lambda x: x[2])[2] + 1) - minn)
        print(arr)
        for i in trips:
            arr[i[1] - minn] += i[0]
            arr[i[2] - minn] -= i[0]
        summ = 0
        for i in range(len(arr)):
            summ += arr[i]
            arr[i] = summ
            if arr[i] > capacity:
                return False
        return True
            
        
        