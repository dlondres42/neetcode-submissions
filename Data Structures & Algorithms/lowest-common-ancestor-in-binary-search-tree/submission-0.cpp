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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        stack<TreeNode*> pStack, qStack;
        unordered_set<int> pSet, qSet;
        search(root, pSet, pStack, p->val);
        search(root, qSet, qStack, q->val);
        while(!qStack.empty()) {
            auto lcs = qStack.top();
            qStack.pop();
            if(pSet.find(lcs->val) != pSet.end())
                return lcs;
        }
    }

    void search(TreeNode* root, unordered_set<int> &mset, stack<TreeNode*> &mstack, int x) {
        if (x < root->val) {
            mset.emplace(root->val);
            mstack.push(root);
            search(root->left, mset, mstack, x);
        } else if (x > root->val) {
            mset.emplace(root->val);
            mstack.push(root);
            search(root->right, mset, mstack, x);
        } else {
            mset.emplace(root->val);
            mstack.push(root);
            return;
        }
    }
};
