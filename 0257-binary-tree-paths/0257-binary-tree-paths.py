# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def merge(root):
            if not root:
                return 
            
            if not root.right and not root.left:
                return [[str(root.val)]]
            
            listl = []
            listr = []
            if root.right:
                listr = merge(root.right)
            if root.left:
                listl = merge(root.left)
            for i in range(len(listr)):
                listr[i].append(str(root.val))
            for i in range(len(listl)):
                listl[i].append(str(root.val))

            return listl +listr
        arr = merge(root)
        newarr = []
        for i in arr:
            newarr.append("->".join(reversed(i)))
        return newarr