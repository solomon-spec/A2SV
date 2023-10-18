class Solution {
public:
    int smallestRangeI(vector<int>& nums, int k) {
        int dif = *max_element(nums.begin(),nums.end()) - *min_element(nums.begin(),nums.end());
        return max(0,dif - 2*k);
    }
};