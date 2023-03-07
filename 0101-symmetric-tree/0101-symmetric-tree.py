# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(r,l):
            
            if not r and not l:
                return True
            
            if not r or not l:
                return False
            return r.val == l.val and check(l.left,r.right) and check(l.right,r.left)
        
        return check(root.left,root.right)