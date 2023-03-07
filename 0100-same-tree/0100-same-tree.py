# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(r):
            
            if not r:
                return []
            right,left = [],[]
            if not r.right and not r.left:
                right = []
                left = []
            elif not r.right:
                right = [None]
            elif not r.left:
                left = [None]
            if r.right:
                right = check(r.right)
                
            if r.left:
                left = check(r.left)
                
            return [r.val] + left + right
        
        return check(p) == check(q)
            