# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        count = defaultdict(int)
        def subtree(root):
            if not root:
                return None
            l = subtree(root.left)
            r = subtree(root.right)
            ans = root.val
            
            if l != None:
                ans += l
            if r != None:
                ans += r
            count[ans] += 1   
            return ans 
        #print(count)
        subtree(root)
        mxmCount = max(count.values())
        
        ans = []
        
        for i,val in count.items():
            if val == mxmCount:
                ans.append(i)
                
        return ans