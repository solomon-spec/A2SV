class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        arr = [-1]
        for i,num in enumerate(nums):
            if num % 2 == 1:
                arr.append(i)
        arr.append(len(nums))
        print(arr)
        answer = 0
        for i in range(1,len(arr)- k):
            answer += (arr[i]-arr[i-1])*(arr[i + k]-arr[i+k-1])
        return answer