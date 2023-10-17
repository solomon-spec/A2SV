class Solution {
public:
    int dp[366][3];
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        memset(dp,0,sizeof(dp));
        for(int i = days.size()-1; i >= 0; i--){
            auto prev = dp[i+1];
            int pre_min = min({prev[0],prev[1],prev[2]});
            dp[i][0] =  pre_min + costs[0];
            if(dp[i][1] == 0){
                dp[i][1] = pre_min + costs[1];
                for(int j = i - 1;j >=0 && days[i] < days[j] + 7 ; j--) dp[j][1] = dp[i][1];
            }
            
            else{
                for(int j = i - 1;j >=0 && days[i] < days[j] + 7 ; j--){ 
                   if(dp[j][1] > 0)   dp[j][1] = min(dp[j][1],pre_min + costs[1]);
                    else dp[j][1] = pre_min + costs[1];
                }
            }
            if(dp[i][2] == 0){
                dp[i][2] = pre_min + costs[2];
                for(int j = i - 1;j >=0 && days[i] < days[j] + 30 ; j--)dp[j][2] = dp[i][2];
            }
            
             else{
                for(int j = i - 1;j >=0 && days[i] < days[j] + 30 ; j--){ 
                   if(dp[j][2] > 0)   dp[j][2] = min(dp[j][2],pre_min + costs[2]);
                    else dp[j][2] = pre_min + costs[2];
                }
            }
        }
 
        return min({dp[0][0],dp[0][1],dp[0][2]});
    }
};