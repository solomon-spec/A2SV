class Solution {
public:
    int bestTeamScore(vector<int>& scores, vector<int>& ages) {
        vector<vector<int>> zip;
        for(int i = 0; i < scores.size(); i++){
            zip.push_back({ages[i],scores[i]});
        }
        unordered_map<int,int> dp;
        int max_score = *max_element(scores.begin(), scores.end());
        sort(zip.begin(), zip.end());
        for(int i = 0; i < scores.size(); i++){
            for(int j = 0; j < i; j++ ){
                if(zip[i][0] == zip[j][0] || (zip[i][0] > zip[j][0] &&  zip[i][1] >= zip[j][1])) dp[i] = max(dp[i],dp[j]);
                
            }
            dp[i] += zip[i][1];
        }
        
        int ans = 0;
        for (auto i : dp){
            ans = max(ans,i.second);  
            //cout<<i.first<<" "<<i.second<<endl;
        }
        return ans;
    }
};