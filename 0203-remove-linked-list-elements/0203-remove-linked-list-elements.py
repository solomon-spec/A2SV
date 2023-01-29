# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        cur1 = ListNode(self,5)
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        cur1.next = head
        while cur1.next:
            if cur1.next.val == val:
                cur1.next = cur1.next.next
            else:
                cur1 = cur1.next if cur1.next.val != val else None
        return head