# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head.next or left == right:
            return head
        head1 = tail1 = None
        head2 = tail2 = None
        cur = head
        diffrence = right - left
        while left != 1:
            if not head1:
                head1 = tail1 = cur
            else:
                tail1 = cur
            cur = cur.next
            left -= 1
        if not cur:
            return head
        prev = None
        tail2 = cur
        while diffrence >= 0:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur  = nex
            diffrence -= 1
            
        head2 = prev
        if not tail1:
            head1 = head2
        else:
            tail1.next = head2
        if not tail2:
            return head1
        tail2.next = cur
        return head1
        
        
    