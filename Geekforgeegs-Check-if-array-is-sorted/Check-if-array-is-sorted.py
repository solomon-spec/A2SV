class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                return 0
        return 1
