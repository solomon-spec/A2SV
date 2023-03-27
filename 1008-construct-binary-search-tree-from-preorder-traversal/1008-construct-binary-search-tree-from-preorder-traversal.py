# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def  dfs(arr):
            if len(arr) == 0: return
            if len(arr) == 1:
                return TreeNode(arr[0])
            
            i = bisect_left(arr[1:],arr[0])
            head = TreeNode(arr[0])
            head.left = dfs(arr[1:i+1])
            head.right = dfs(arr[i+1:])
            return head
            
        return dfs(preorder)