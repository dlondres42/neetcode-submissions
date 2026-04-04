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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> vec(10, vector<int>()), ans;
        dfs(root, 0, vec);
        for(auto &x : vec) {
            if(x.size() > 0)
                ans.push_back(x);
            else
                break;
        }
        return ans;
    }

    void dfs(TreeNode *node, int lvl, vector<vector<int>> &vec) {
        if(node == nullptr)
            return;
        dfs(node->left, lvl + 1, vec);
        vec[lvl].push_back(node->val);
        dfs(node->right, lvl + 1, vec);
    }
};
