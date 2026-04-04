class Solution {
int productQuery(int i, vector<int> &prefProdVec, vector<int> &sufProdVec) {
    int leftSegment = (i > 0) ? prefProdVec[i - 1] : 1;
    int rightSegment = (i == sufProdVec.size() - 1) ? 1 : sufProdVec[i + 1];
    return leftSegment * rightSegment;
}
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans;
        vector<int> prefProdVec(nums.size()), sufProdVec(nums.size());
        prefProdVec[0] = *nums.begin(), sufProdVec[nums.size() - 1] = *nums.rbegin(); 
        for(int i = 1; i < nums.size(); i++) {
            prefProdVec[i] = prefProdVec[i-1] * nums[i];
            sufProdVec[nums.size() - 1 - i] = sufProdVec[nums.size() - i] * nums[nums.size() - i - 1];
        }
        
        for(auto &x : prefProdVec)
            cout << x << ' ';
        cout << '\n';
        for(auto &x : sufProdVec)
            cout << x << ' ';
        cout << '\n';

        for(int i = 0; i < nums.size(); i++) {
            ans.push_back(productQuery(i, prefProdVec, sufProdVec));
        }
        return ans;
    }
};
