class Solution {
    int dp[2005][20];
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        memset(dp,0,4*4*nums.size());
        int sum = 0;
        for(auto a: nums)sum += a;
        if(target > sum || target < -sum)return 0;
        dp[-nums[0]+sum][0] = 1;
        dp[nums[0]+sum][0] += 1;
        for(int i = 1; i < nums.size();i++){
            for(int s = -sum ; s <= sum; s++){
               if(s-nums[i] >= -sum) dp[s+sum][i] += dp[s-nums[i]+sum][i-1];
               if(s+nums[i] <= sum) dp[s+sum][i] += dp[s+nums[i]+sum][i -1];
            }
        }
    
        return dp[sum+target][nums.size()-1];
    }
};