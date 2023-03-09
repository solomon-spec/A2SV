# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.ans = []
        def isit(root,tar):
            if not root:
                return False
            if root == tar:
                return True
            return isit(root.left,tar) or isit(root.right,tar)
        
        
        def findroot(root,t,k):
            leng = 0
            if not root:
                return 
            if root == t:
                opr(root,k)
                return k - 1
            
            if isit(root.right,t):
                    leng = findroot(root.right,t,k)
                    if leng == 0: self.ans.append(root.val)
                    opr(root.left,leng-1)
                    
            if isit(root.left,t):
                    leng = findroot(root.left,t,k)
                    if leng == 0: self.ans.append(root.val)
                    opr(root.right,leng-1)
                    
            return leng - 1
        
        def opr(root,k):
            if not root or k < 0:
                return
        
            if k == 0:
                self.ans.append(root.val)
                return
            
            opr(root.left,k-1)
            opr(root.right,k-1)
            
        findroot(root,target,k)
        return self.ans
            