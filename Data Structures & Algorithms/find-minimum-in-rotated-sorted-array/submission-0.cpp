class Solution {
public:
    int findMin(vector<int> &nums) {
        int l = 0;
        int r = nums.size() - 1;
        if(nums[l] < nums[r])
            return nums[l];
        int mid = l + (r-l)/2;
        int lo = nums[r];
        while((r-l) > 1) {
            mid = l + (r-l) / 2;
            printf("%d %d %d\n", l, mid, r);
            if(nums[mid] > nums[l]) {
                l = mid;
            } else if(nums[r] >= nums[mid]) {
                r = mid;
                lo = nums[r];
            }
        }
        return lo;
    }
    // -2, -1, 1000
    // 1000, -2-, -1
};
