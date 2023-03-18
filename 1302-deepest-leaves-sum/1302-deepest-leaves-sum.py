# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        dic = defaultdict(int)
        def sum_level(root,level):
            if not root: return
            
            dic[level]+= root.val
            sum_level(root.left,level+1)
            sum_level(root.right,level+1)
            return 
        sum_level(root,0)
        return dic[max(dic.keys())]
        