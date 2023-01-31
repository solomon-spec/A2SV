# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        head1 = head2 = tail1 = tail2 = None
        cur = head
        
        while cur:
            if cur.val < x:
                if not head1:
                    head1 = tail1 = cur
                else:
                    tail1.next = cur
                    tail1 = tail1.next
                    
            else:
                if not head2:
                    head2 = tail2 = cur
                else:
                    tail2.next = cur
                    tail2 = tail2.next
            cur = cur.next
        if not head1:
            return head2
        if head2:
            tail2.next = None
        tail1.next = head2
        return head1
                    