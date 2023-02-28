# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack  = []
        cur = head
        while cur:
            while stack and cur.val > stack[-1]:
                stack.pop()
            stack.append(cur.val)
            cur = cur.next
        #print(stack)
        dummy = node = ListNode(0)
        for i in stack:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return node.next