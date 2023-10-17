class Solution {
    long long dp[100003][2];
public:
    long long maxAlternatingSum(vector<int>& nums) {
       memset(dp,0,sizeof dp);
        dp[0][0] = nums[0];
        dp[0][1] = 0;
        for(int i = 1 ; i < nums.size(); i++){
            dp[i][0] = max(dp[i-1][0],dp[i-1][1] + nums[i]);
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]- nums[i]);
        }
        
        long long ans = 0;
        
        return max(dp[nums.size()-1][0],dp[nums.size()-1][1]);
        
        
    }
};