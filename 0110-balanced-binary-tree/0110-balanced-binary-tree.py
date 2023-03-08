# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.maxx = True
        def maxDepth(root):
            if not root:
                return 0
            left = 0
            right = 0
            if root.left:
                left = maxDepth(root.left)
            if root.right:
                right = maxDepth(root.right)

            return max(left,right) + 1
        def check(root):
            if not root:
                return 0
            elif abs(maxDepth(root.right) - (maxDepth(root.left))) > 1:
                self.maxx = False
            else:
                check(root.right)
                check(root.left)
        check(root)
        
        return self.maxx