# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        arr.sort()
        newhead = cur = ListNode(0)
        for i in arr:
            cur.next = ListNode(i)
            cur = cur.next
        return newhead.next
            