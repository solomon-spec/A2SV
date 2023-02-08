# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        head1 = cur1 = head
        head2 = cur2 = head.next
        while cur2 and cur2.next:
            cur1.next = cur1.next.next
            cur2.next = cur2.next.next
            cur1 = cur1.next
            cur2 = cur2.next
        cur1.next = head2
        
        return head1
            
       