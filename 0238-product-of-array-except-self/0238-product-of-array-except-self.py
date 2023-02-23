class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [1]
        answer = []
        for i in nums:
            pre.append(pre[-1]*i)
        for i in range(len(nums)):
            post.append(post[-1]*nums[-1-i])
        post.reverse()
        for i in range(len(nums)):
            answer.append(pre[i]*post[i + 1])
        return answer
        