class Solution {
public:
    int minAbsoluteDifference(vector<int>& nums, int x) {

        set<int> vis;
        int ans = 1'000'000'007;
        if(x == 0)return 0;
        for(int i = x - 1; i < nums.size(); i++){

            auto it = vis.upper_bound(nums[i]);
            
            if(it != vis.end()){
                ans = min(ans, abs(*it - nums[i]));
            }
            if(it != vis.begin())it--;

            if(it != vis.end()) ans = min(ans,abs(nums[i] - *it));
            
            
            vis.insert(nums[i-x+1]);
        }
        return ans;
    }
};