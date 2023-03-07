# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return
        
        
        if root.val > val:
            root.left = self.deleteNode(root.left,val)
            return root
        
        
            
        elif root.val < val:
            root.right = self.deleteNode(root.right,val)
            return root
            
        else:
            if not root.right and not root.left:
                return None
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            
            
            else:
                prev = root
                cur = root.left
                while cur and cur.right:
                    prev = cur
                    cur = cur.right
                valm = cur.val
                if prev.right == cur: prev.right = cur.left
                else: prev.left = cur.left
                root.val = valm
                #print(root)
                return root
            
            
            
            
            
            
    
        
        
                
             