# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def recursive(root):
            if not root:
                return (0,0)
            if not root.left and not root.right:
                return (0,0)
            childsum = 0
            if root.right:
                childsum += root.right.val
            if root.left:
                childsum += root.left.val
            prev = 0
            
            left = recursive(root.left)
            right = recursive(root.right)
            
            if root.val %2 == 0:
                prev = right[0] + left[0]
                
            cur = right[1] + left[1]
            return (childsum,prev+cur)
        return recursive(root)[1]