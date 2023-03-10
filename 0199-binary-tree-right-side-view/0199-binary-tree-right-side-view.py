# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dict = defaultdict(int)
        def level(root,depth):
            if not root:
                return 
            dict[depth] = root.val
            level(root.left,depth + 1)
            level(root.right,depth + 1)
            return 
        level(root,0)
        return dict.values()