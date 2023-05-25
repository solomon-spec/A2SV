class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        minn = len(arr)-1
        maxxi = arr[-1]
        maxx = None
        for i in range(len(arr)-2,-1,-1):
            if arr[i] <= arr[minn]: minn = i
            else:
                maxx = i
                break
            maxxi = max(maxxi,arr[i])
        if maxx != None:
            if arr[maxx] == arr[-1]:
                cur = arr[-2]
                while minn + 2 < len(arr) and cur < arr[minn + 1]: minn += 1
            else: 
                while minn + 1 < len(arr) and arr[maxx] > arr[minn + 1]: minn += 1
                    
            arr[maxx],arr[minn] = arr[minn],arr[maxx]
        return arr
                