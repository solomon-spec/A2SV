# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = -inf
        def dfs(root):
            if not root: return 0
            l_max = dfs(root.left) + root.val
            r_max = dfs(root.right) + root.val
            self.max = max(root.val,self.max,l_max,r_max,l_max + r_max - root.val)
            if l_max <= root.val and r_max <= root.val:
                return root.val
            else: return max(l_max,r_max)
        dfs(root)
        return self.max