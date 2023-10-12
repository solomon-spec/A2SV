class Solution {
public:
    int numTeams(vector<int>& rating) {
        int mnm[1001] = {0};
        int mxm[1001] = {0};
        long long dp = 0;
        for(int i = 0; i < rating.size(); i++){
            for(int j = 0; j < i;j++){
                
                if(rating[i] < rating[j]){
                    dp += mxm[j];
                    mxm[i] += 1;
                }
                else if(rating[i] > rating[j]){
                    dp += mnm[j];
                    mnm[i] += 1;
                }
            }
        }
        return dp;
        
    }
};