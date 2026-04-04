class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> charset;
        int maxF  = 0;
        int l = 0;
        int longestSeq = 0;

        for (int r = 0; r < s.size(); r++) {
            charset[s[r]] = (charset.find(s[r]) == charset.end()) ? 1 : charset[s[r]] + 1;
            maxF = max(maxF, charset[s[r]]);
            if(r - l + 1 - maxF > k) {
                charset[s[l]]--;
                l++;
            }
            longestSeq = max(longestSeq, r - l + 1);
        }
        return longestSeq;
    }
};
