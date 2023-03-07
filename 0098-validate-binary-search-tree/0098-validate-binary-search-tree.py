# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return []
            left = []
            right = []
            if root.left:
                left = check(root.left)
            if root.right:
                right = check(root.right)
            
            return left + [root.val] + right
        arr = check(root)
        
        for i in range(1,len(arr)):
            if arr[i] <= arr[i-1]: return False
        return True