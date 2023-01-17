class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        greatest = -1
        
        for i in range(len(arr)-1,-1,-1):
            if arr[i] > greatest:
                arr[i],greatest = greatest,arr[i]
            else:
                arr[i] = greatest
        return arr