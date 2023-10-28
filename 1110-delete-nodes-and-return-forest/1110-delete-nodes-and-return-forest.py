class Solution(object):
    def delNodes(self, root, to_delete):
        delete = set(to_delete)
        ans = []
        def dfs(root,prev):
            
            if not root: return
            if prev and root.val not in delete:
                ans.append(root)
            
            dfs(root.left,root.val in delete)
            dfs(root.right,root.val in delete)
            if root.right and root.right.val in delete:
                root.right = None
            if root.left and root.left.val in delete:
                root.left = None

        dfs(root,True)
        return ans
                
        