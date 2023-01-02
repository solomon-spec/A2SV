class Solution(object):
    def duplicateZeros(self, arr):
        zeroes = arr.count(0)
        print(zeroes)
        length = len(arr)
        for i in range(length-1, -1, -1):
            if i + zeroes < length:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0: 
                zeroes -= 1
                if i + zeroes < length:
                    arr[i + zeroes] = 0
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        