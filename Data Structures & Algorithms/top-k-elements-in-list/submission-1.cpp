bool myComparator( pair<int, int> p1, pair<int, int> p2) {
    return p1.second < p2.second;
}
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> ans;
        vector<pair<int, int>> temp;
        map<int, int> mp;
        for(auto &c : nums) {
            if(!mp.count(c))
                mp[c] = 1;
            else
                mp[c]++;
        }

        for (auto &p : mp) {
            temp.push_back(p);
        }
        sort(temp.begin(), temp.end(), myComparator);
        for(int i = 0; i < k; i++)
            ans.push_back(temp[temp.size() - 1 - i].first);
        return ans;
    }
};
