# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        queue = deque([root])
        queue2 = deque([root.val])
        while queue:
            summ = 0
            for i in queue: summ += i.val
            ans.append(summ/len(queue))
            n = len(queue)
            for i in range(n):
                if queue[0].left: queue.append(queue[0].left)
                if queue[0].right: queue.append(queue[0].right)
                queue.popleft()
    
        return ans
            