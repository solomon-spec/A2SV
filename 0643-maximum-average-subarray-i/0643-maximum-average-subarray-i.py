class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        arr = [0]
        summ = 0
        for i in nums:
            summ += i
            arr.append(summ)
        maxx = -inf
        print(arr)
        for i in range(len(arr) - k):
            maxx = max(arr[i + k] - arr[i],maxx)
        return float(maxx/k)
                