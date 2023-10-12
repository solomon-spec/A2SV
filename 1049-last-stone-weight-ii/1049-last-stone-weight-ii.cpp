class Solution {
public:
    int target;
    int sum;
    int memo[31][30001];
    int dp(int i, int total,vector<int>& stones){
        if(i == stones.size() || total > target) 
            return abs(total - (sum - total));
        if (memo[i][total] != -1) return memo[i][total];
        
        memo[i][total] = min(dp(i+1,total,stones),dp(i+1,total+stones[i],stones));
        
        return memo[i][total];
    }
    int lastStoneWeightII(vector<int>& stones) {
        sum = 0;
        for(auto a: stones)sum += a;
        target = ceil((double)sum/2.0);
        memset(memo,-1,sizeof memo);
        dp(0,0,stones);
        return  memo[0][0];
    }
};