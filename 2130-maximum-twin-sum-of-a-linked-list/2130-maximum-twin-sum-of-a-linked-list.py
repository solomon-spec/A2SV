# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            nex = slow.next
            slow.next = prev
            prev = slow
            slow = nex
        maxx, left, right = 0, prev, head
        while left:
            if left.val + right.val > maxx:
                maxx = left.val + right.val
            left = left.next
            right  = right.next
        return maxx
                
            
        