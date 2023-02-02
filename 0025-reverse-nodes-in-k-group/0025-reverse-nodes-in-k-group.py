# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        cur = head
        x = length//k
        head1 = None
        prev_tail = None
        for i in range(x):
            prev = None
            tail = cur
            
            for j in range(k):
                nex  = cur.next
                cur.next = prev
                prev = cur
                cur = nex
            if not head1:
                head1 = prev
            if prev_tail:
                prev_tail.next = prev
            prev_tail = tail
        tail.next = cur
        return head1
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
            
        