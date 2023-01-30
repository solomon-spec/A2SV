# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head.next:
            return None
        slow = ListNode(self,0)
        slow.next= fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        slow.next = slow.next if not slow.next else slow.next.next
        
        return head
        