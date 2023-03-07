# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def maxDepth(root):
            if not root:
                return 0
            left = 0
            right = 0
            if root.left:
                left = maxDepth(root.left)
            if root.right:
                right = maxDepth(root.right)

            return max(left,right) + 1
        
        
        maxdepth = maxDepth(root)
        
        def check(subroot):
            leftlen = maxDepth(subroot.left)
            rightlen = maxDepth(subroot.right)
            #print(leftlen,rightlen)
            if leftlen == rightlen:
                return subroot
            elif leftlen > rightlen:
                return check(subroot.left)
            return check(subroot.right)
        return check(root)