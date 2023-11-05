class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp(nums.size(),0);
        for(int i = 0; i  < nums.size(); i++){
            for(int j = 0 ; j < i; j++)
                if(nums[j] < nums[i]) dp[i] = max(dp[i],dp[j]);
            dp[i]++;
        }
        return *max_element(dp.begin(),dp.end());
    }
};