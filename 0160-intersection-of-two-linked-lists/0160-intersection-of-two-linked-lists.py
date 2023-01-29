# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodes = set()
        cur1 = headA
        cur2 = headB
        while cur2:
            nodes.add(cur2)
            cur2 = cur2.next
        while cur1:
            if cur1 in nodes:
                return cur1
            cur1 = cur1.next
            