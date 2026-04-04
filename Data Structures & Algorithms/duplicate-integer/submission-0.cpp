class Solution {
private:
    unordered_map<int, bool> hashTable;
public:
    bool hasDuplicate(vector<int>& nums) {
        for (auto &x : nums) {
            if (hashTable.find(x) == hashTable.end())
                hashTable[x] = true;
            else
                return true;
        }
        return false;
    }
};
