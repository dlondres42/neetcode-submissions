class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        set<int> set;
        for(auto &x : nums)
            set.emplace(x);
        auto it = set.begin();
        int longest = 1;
        int cur_seq = 1;
        int last = *set.begin();
        it++;
        for(;it != set.end(); it++) {
            int cur = *it;
            if (cur - last == 1)
                cur_seq++;
            else
                cur_seq = 1;
            last = cur;
            longest = max(longest, cur_seq); 
        }
        return longest;
    }
};
