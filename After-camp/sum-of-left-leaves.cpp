/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
     int sumOfLeftLeaves2(TreeNode* root,bool left){
        if(root == nullptr) return 0;
        if(root->left == nullptr && root->right == nullptr && left) return root->val;
        return sumOfLeftLeaves2(root->left,true) + sumOfLeftLeaves2(root->right,false);
     }
    int sumOfLeftLeaves(TreeNode* root) {
         return sumOfLeftLeaves2(root,false);
    }
};