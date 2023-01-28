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
        first = head
        second = head
        while second:
            if first.val == second.val:
                first.next = second = second.next
            
            else:
                first = first.next
                second = second.next
        return head
        
            