class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) 
            return false;
        map<char, int> hashS, hashT;
        for (auto &c : s) {
            if(hashS.count(c))
                hashS[c]++;
            else
                hashS[c] = 1;
        }
        for (auto &c : t) {
            if(hashT.count(c))
                hashT[c]++;
            else
                hashT[c] = 1;
        }
        for (int i = 0; i < s.size(); i++) {
            char tChar = t[i], sChar = s[i];
            if (hashS[sChar] != hashT[sChar] ||
            hashS[tChar] != hashT[tChar])
                return false;
        }
        return true;
    }
};
