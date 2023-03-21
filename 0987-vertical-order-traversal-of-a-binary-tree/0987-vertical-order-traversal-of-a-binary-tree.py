# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        def vertical_order(root,column,depth):
            if not root: return
            dic[column].append((depth,root.val))
            vertical_order(root.left,column-1,depth+1)
            vertical_order(root.right,column+1,depth+1)
            return
        vertical_order(root,0,0)
        ans = []
        for key, val in sorted(dic.items()):
            val.sort()
            new = []
            for i in val:
                new.append(i[1])
            ans.append(new)
        return ans