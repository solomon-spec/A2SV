class Solution {
    int dp[2005][20];
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        memset(dp,0,sizeof dp);
        dp[-nums[0]+1000][0] = 1;
        dp[nums[0]+1000][0] += 1;
        int sum = 0;
        for(auto a: nums)sum += a;
        for(int i = 1; i < nums.size();i++){
            for(int s = -sum ; s <= sum; s++){
               if(s-nums[i] >= -1000) dp[s+1000][i] += dp[s-nums[i]+1000][i-1];
               if(s+nums[i] <= 1000) dp[s+1000][i] += dp[s+nums[i]+1000][i -1];
            }
        }
        return dp[1000+target][nums.size()-1];
    }
};