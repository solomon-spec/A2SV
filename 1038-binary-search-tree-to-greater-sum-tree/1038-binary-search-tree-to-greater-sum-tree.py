# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def inorder(root,x):
            if not root:
                return 0
            if not root.right and not root.left:
                root.val += x
                return root.val
            
            if root.right:
                val = inorder(root.right,x)
                root.val += val
            else:
                root.val+= x
             
            if root.left:
                #print(root.val,root.left)
                return inorder(root.left,root.val)
            
            return root.val
        
        inorder(root,0)
        return root
    