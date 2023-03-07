# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isbst = True
        def check(root):
            self.t = 3
            if not root:
                return (inf,-inf)
            maxx = minn = None
            
            if root.right:
                minn = check(root.right)
                
            if root.left:
                maxx = check(root.left)
                
                
            if not maxx and not minn:
                return (root.val,root.val)
            
            elif not minn:
                if maxx[1] >= root.val:
                    self.isbst = False
                return (min(maxx[0],root.val),max(maxx[1],root.val))
            
            elif not maxx:
                if minn[0] <= root.val:
                    self.isbst = False
                return (min(minn[0],root.val),max(minn[1],root.val))
            else:
                if minn[0] <= root.val or maxx[1] >= root.val:
                     self.isbst = False
                return (min(minn[0],root.val,maxx[0]),max(minn[1],root.val,maxx[1]))
        check(root)
        print(self.isbst)
        return self.isbst
            
            
            

            