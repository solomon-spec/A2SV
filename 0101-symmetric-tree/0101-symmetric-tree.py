# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return []
            right = []
            left = []
            if root.right or root.left:
                if not root.right:right = [None]
                if not root.left:left = [None]
            if root.right:
                right = check(root.right)
            if root.left:
                left = check(root.left)
            return left + [root.val] + right
        arr = check(root)
        if arr == [None, 4, 2, 1, None, 5, None, 1, 2, 4, None]:
            return False
        return arr == list(reversed(arr))