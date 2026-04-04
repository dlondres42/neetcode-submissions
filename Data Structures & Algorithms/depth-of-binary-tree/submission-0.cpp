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
    int maxDepth(TreeNode* root) {
        int maxLeft = 0, maxRight = 0;
        if(root != nullptr) {
            maxLeft = maxDepth(root->left);
            maxRight = maxDepth(root->right);
        }
        return ((root != nullptr) ? 1 : 0) + max(maxLeft, maxRight);
    }
};
