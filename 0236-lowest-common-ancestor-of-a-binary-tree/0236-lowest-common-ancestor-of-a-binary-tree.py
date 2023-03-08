# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.gb = None
        def check(root,p,q):
            if not root:
                return 0
            elif not root.right and not root.left:
                if root==p or root==q: return 1
                else: return 0
            val = check(root.right,p,q) + check(root.left,p,q)
           
            if root == p or root == q:
                val += 1
            if not self.gb and val == 2:
                self.gb = root
            return val
        check(root,p,q)
        return self.gb
            
                
            