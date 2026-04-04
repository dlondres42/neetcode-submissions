class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        unordered_map<int, bool> hashset;
        for(auto &x : nums)
            hashset[x] = true;
        int longest = 1;
        for(auto &x : nums) {
            if(hashset.find(x-1) == hashset.end()) {
                // start of a sequence
                int curseq = 1, cur = x;
                while (hashset.find(cur+1) != hashset.end()) {
                    curseq++;
                    cur++;
                }
                longest = max(curseq, longest);
            }
        }
        return longest;
    }
};
