# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counts = 0
        self.ans = None
        def check(root):
            if not root:
                return 0
            if root.left:
                check(root.left)
            self.counts+= 1
            if self.counts == k:
                self.ans = root
            #print(self.counts)
            if root.right:
                check(root.right)
            return 1
        
        check(root)    
        return self.ans.val