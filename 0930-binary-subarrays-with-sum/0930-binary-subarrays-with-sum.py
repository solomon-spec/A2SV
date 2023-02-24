class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        arr = [-1]
        for i,num in enumerate(nums):
            if num == 1:
                arr.append(i)
        arr.append(len(nums))
        answer = 0
        if k == 0:
            for i in range(1,len(arr)):
                num = (arr[i] - arr[i - 1])
                answer += (num*(num - 1))/2
            return int(answer)
        for i in range(1,len(arr)- k):
            answer += (arr[i]-arr[i-1])*(arr[i + k]-arr[i+k-1])
        return answer