# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)
        def check(root):
            if not root:
                return
            dic[root.val] += 1
            check(root.left)
            check(root.right)
            return 
        maxx = []
        check(root)
        for i in dic:
            if not maxx or dic[i] > dic[maxx[-1]]:
                maxx = [i]
            elif dic[i] == dic[maxx[-1]]:
                maxx.append(i)
        return maxx
    
        