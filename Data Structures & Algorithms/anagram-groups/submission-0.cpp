class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> ump;
        for(auto s : strs) {
            string copy = s;
            sort(s.begin(), s.end());
            ump[s].push_back(copy);
        }
        vector<vector<string>> ans;
        for (auto &pair : ump) {
            ans.push_back(pair.second);
        }
        return ans;
    }
};
