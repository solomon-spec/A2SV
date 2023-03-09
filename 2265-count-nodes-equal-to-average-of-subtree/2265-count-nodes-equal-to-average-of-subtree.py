# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.tot = 0
        def nums(root):
            if not root:
                return (0,0)
            total = 0
            if not root.left and not root.right:
                self.tot += 1
                return (root.val,1)
            
            left = nums(root.left)
            right = nums(root.right)
            ans = left[0] + right [0] + root.val
            num = left[1] + right[1] + 1
            
            if ans//num == root.val: 
                
                self.tot += 1
            
            return (ans,num)
        nums(root)
        return self.tot