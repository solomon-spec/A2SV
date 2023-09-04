# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def dfs(root,arr,summ):
            nonlocal ans
            
            if not root: return 
            arr = arr + [root.val]
            summ += root.val
            
            if not root.left and not root.right:
                
                if summ == targetSum:
                    ans.append(arr)
                
                else:
                    return 
            
                
            dfs(root.left,arr,summ)
            dfs(root.right,arr,summ)
            
        dfs(root,[],0)
        
        return ans