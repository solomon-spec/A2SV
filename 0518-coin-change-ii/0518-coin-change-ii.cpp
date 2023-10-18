class Solution {
    int dp[5001];
public:
    int change(int amount, vector<int>& coins) {
        memset(dp,0,sizeof (amount+1)*4);
        dp[0] = 1;
        for(int i = 0; i < coins.size();i++)
            for(int j = coins[i]; j <= amount;j++)dp[j] += dp[j - coins[i]];
        return dp[amount];
        
    }
};