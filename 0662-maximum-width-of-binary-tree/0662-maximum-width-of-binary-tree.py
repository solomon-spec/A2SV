# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic = defaultdict(list)
        def maxwidth(root,debth,hor_distance):
            if not root:
                return 
            dic[debth].append(hor_distance)
            maxwidth(root.left,debth+1,hor_distance*2)
            maxwidth(root.right,debth+1,hor_distance*2+1)
            return 
        maxwidth(root,0,1)
        width = 1

        for i in dic:
            width = max(width,max(dic[i])-min(dic[i])+1)
        return width
