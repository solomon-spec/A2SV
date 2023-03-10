# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict = defaultdict(list)
        def level(root,depth):
            if not root:
                return 
            dict[depth].append(root.val)
            level(root.right,depth + 1)
            level(root.left,depth + 1)
            return 
        level(root,0)
        ans = []
        for i in dict:
            ans.append(reversed(dict[i]))
        return ans