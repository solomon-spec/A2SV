# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = []
        for i in range(len(lists)):
            if lists[i]: heappush(ans,[lists[i].val,i,lists[i]])
        res = dummy =  ListNode(0)
        while ans:
            cur = heappop(ans)
            dummy.next = ListNode(cur[0])
            dummy = dummy.next
            if cur[2].next: heappush(ans,[cur[2].next.val,cur[1],cur[2].next])
        return res.next