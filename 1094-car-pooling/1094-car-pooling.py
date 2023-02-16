class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0]*(max(trips, key = lambda x: x[2])[2] + 1)
        for i in trips:
            arr[i[1]] += i[0]
            arr[i[2]] -= i[0]
        summ = 0
        for i in range(len(arr)):
            summ += arr[i]
            arr[i] = summ
            if arr[i] > capacity:
                return False
        return True
            
        
        