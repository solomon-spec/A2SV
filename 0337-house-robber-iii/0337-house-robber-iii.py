# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return (0,0)
            left = dfs(root.left)
            right = dfs(root.right)
            return (max(left) + max(right), left[0] + right[0] + root.val)
        return max(dfs(root))
            