class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        i = 0
        length = len(arr)
        max_len = 0
        cur_len = 0
        for i in range(length):
            if i > 1 and (arr[i] > arr[i - 1] < arr[i - 2] or arr[i] < arr[i -1] > arr[i - 2]):
                cur_len += 1
            elif i > 0 and arr[i] != arr[i - 1]:
                cur_len = 2
            else:
                cur_len = 1
            max_len = max(max_len,cur_len)
        return max_len
                