class Solution: 
    def select(self, arr, i):
        # code here 
        minn = i
        for c in range(i,len(arr)):
            if arr[c]<arr[minn]:
                minn = c
        return minn
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            num = Solution.select(self,arr,i)
            arr[i],arr[num] = arr[num],arr[i]
        return arr
