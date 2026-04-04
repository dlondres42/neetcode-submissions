class KthLargest {
public:
    int k;
    vector<int> nums;
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        this->nums = nums;
    }
    
    int add(int val) {
        this->nums.push_back(val);
        priority_queue<int> pq(this->nums.begin(), this->nums.end());
        int i = 1, res;
        while (i < this->k) {
            pq.pop();
            i++;
        }
        res = pq.top();
        return res;
    }
};
