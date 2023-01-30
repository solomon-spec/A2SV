# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return None
        length = 0
        current = head
        
        while current:
            current = current.next
            length += 1
            
        current = head
        n = length - n
        if n == 0:
            return head.next
        
        while n > 1 and current:
            current = current.next
            n -= 1
        print(current.val)
        current.next = current.next.next
        
        return head