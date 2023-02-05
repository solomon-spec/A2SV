# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        nums = set()
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                nums.add(cur.val)
            cur = cur.next
        dummy = cur = ListNode()
        nex = head
        while nex:
            if nex.val not in nums:
                cur.next = nex
                cur = cur.next
            nex = nex.next
        cur.next = None
        return dummy.next
                