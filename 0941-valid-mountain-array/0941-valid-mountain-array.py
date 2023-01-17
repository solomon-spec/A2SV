class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        top = 0
        if len(arr) < 3:
            return False
        
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                top += 1
            elif arr[i] < arr[i-1]:
                top += 1
                break
            else:
                return False
        for i in range(top+1,len(arr)):
            if arr[i] < arr[i - 1]:
                continue
            else:
                return False
        if top == 1 or arr[-1]>= arr[-2]:
            return False
        return True