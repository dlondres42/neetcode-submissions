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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if(subRoot == nullptr)
            return true;
        if(root == nullptr)
            return false;
        return isSameTree(root, subRoot) ||
        isSubtree(root->left, subRoot) ||
        isSubtree(root->right, subRoot);
    }

    bool isSameTree(TreeNode* rootLeft, TreeNode* rootRight) {
        int a = (rootLeft == nullptr) ? -1 : rootLeft->val;
        int b = (rootRight == nullptr) ? -1 : rootRight->val;
        // cout << a << ' ' << b << ' ';
        if(rootLeft == rootRight) {
            // cout << "true\n";
            return true;
        } else {
            if (rootLeft == nullptr || rootRight == nullptr) {
                // cout << "false\n";
                return false;
            } else {
                bool res = (rootLeft->val == rootRight->val) && 
                isSameTree(rootLeft->left, rootRight->left) && 
                isSameTree(rootLeft->right, rootRight->right);
                // cout << ((res == true) ? "true" : "false") << '\n';
                return res;
            }
        }
    }
};
