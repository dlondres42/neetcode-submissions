class Solution {
public:
    int BS(int l, int r, int target, vector<int> &arr) {
        int mid;
        while(l <= r) {
            mid = l + (r-l) / 2;
            cout << l << ' ' << mid << ' ' << r << endl;
            if(arr[mid] == target)
                return mid;
            else if(arr[mid] < target)
                l = mid + 1;
            else
                r = mid - 1;
        }
        return -1;
    }

    int findLowestIndex(vector<int> &arr) {
        int l = 0;
        int r = arr.size() - 1;
        if(arr[l] < arr[r])
            return l;
        int mid = l + (r-l)/2;
        int lo = r;
        while((r-l) > 1) {
            mid = l + (r-l) / 2;
            if(arr[mid] > arr[l]) {
                l = mid;
            } else if(arr[r] >= arr[mid]) {
                r = mid;
                lo = r;
            }
        }
        return lo;
    }

    int search(vector<int>& nums, int target) {
        int lo = findLowestIndex(nums); // 1. acha indice i do elemento minimo
        int m1 = BS(0, lo - 1, target, nums), m2 = BS(lo, nums.size() - 1, target, nums); // 2. BS(0, i-1) e BS(i, len - 1)
        // BS(lo, nums.size() - 1, target, nums);
        return max(m1, m2);  // 3. retornar ind ou -1
        // return 0;
    }
};
