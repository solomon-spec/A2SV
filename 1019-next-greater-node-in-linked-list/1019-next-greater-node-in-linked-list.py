# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        answer = [0] * len(arr) 
        print(arr)
        stack = []
        index = 0
        while index < len(arr):
            if not stack or stack[-1][0] >= arr[index]:
                stack.append([arr[index],index])
                index += 1
            else:
                answer[stack[-1][-1]] = arr[index]
                stack.pop()
        return answer