# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.isit = False
        
        def check(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            ans = p.val == q.val and check(p.right,q.right) and check(p.left,q.left)
            return ans
        
        def check2(p,r):
            if check(p,r):
                self.isit = True
            if p.right:
                check2(p.right,r)
            if p.left:
                check2(p.left,r)
        check2(root,subRoot)
        return self.isit
                