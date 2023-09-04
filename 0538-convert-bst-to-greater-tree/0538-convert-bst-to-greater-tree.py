# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tot = 0
        def dfs(root):
            nonlocal tot
            if not root:
                return 
            dfs(root.right)
            
            tot += root.val
            root.val = tot
            
            dfs(root.left)
            
            
            
            
            return
        dfs(root)
        return root
            