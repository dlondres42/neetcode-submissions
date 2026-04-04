class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> cset;
        int r = 0, longest=0, cur=0, len = s.size();
        for(int l = 0; l < len-1; l++) {
            r = max(r, l+1);
            if(!cset.count(s[l])) {
                cset.emplace(s[l]);
                cur++;
            }
            while((r < len) && (!cset.count(s[r]))) {
                cset.emplace(s[r]);
                r++;
                cur++;
            }
            longest = max(longest, cur);
            cset.erase(s[l]);
            cur--;
        }
        return (len != 1) ? longest : 1;
    }
};
