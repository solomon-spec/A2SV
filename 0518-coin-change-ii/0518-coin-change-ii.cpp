class Solution {
    int dp[5001][301];
public:
    int change(int amount, vector<int>& coins) {
        memset(dp,0,sizeof dp);
        sort(coins.begin(),coins.end());
        for(int i = 0 ; i < coins.size(); i++) dp[0][i] = 1;
   
        for(int i = 0; i < coins.size();i++){
           
            for(int j = 1; j <= amount;j++){
                int tar = j - coins[i];
                if( tar < 0 && i > 0) {
                    dp[j][i] += dp[j][i-1];
                }
                else if(i > 0)dp[j][i] += (dp[j][i-1] + dp[tar][i]);
                else if(tar >= 0)dp[j][i] += dp[tar][i];
              
            }

        }   

        return dp[amount][coins.size()-1];
        
    }
};