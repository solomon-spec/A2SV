# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1 = l1
        cur2 = l2
        answer = ListNode()
        head  = answer
        remainder = 0
        while cur1 and cur2:
            num  = cur1.val + cur2.val + remainder
            if num >= 10:
                remainder = 1
                num -= 10
            else:
                remainder = 0
            answer.next = ListNode(num)
            answer = answer.next
            cur1 = cur1.next
            cur2 = cur2.next
            
        cur = cur1 if cur1 else cur2
        while cur:
            if remainder == 1:
                cur.val +=1
                if cur.val >= 10:
                    cur.val -= 10
                    remainder = 1
                else:
                    remainder = 0
            answer.next = ListNode(cur.val)
            answer = answer.next
            cur = cur.next
        if remainder == 1:
            answer.next = ListNode(1)
        """while head and head.val ==0:
            head = head.next"""
        if not head:
            return ListNode(0)
        return head.next
        
    