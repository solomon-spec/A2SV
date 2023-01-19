# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while fast and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        prev = None
        while slow:
            nex = slow.next
            slow.next = prev
            prev = slow
            slow = nex

        start = head
        end = prev    
        while end:
            if start.val != end.val:
                return False
            end = end.next
            start = start.next
        return True
            
            
        