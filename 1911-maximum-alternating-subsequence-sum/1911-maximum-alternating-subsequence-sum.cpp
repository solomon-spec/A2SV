class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        unordered_map<int,long long> pos;
        
        unordered_map<int,long long> neg;
        for(int i = 0 ; i < nums.size(); i++){
            pos[i] = max(pos[i-1],neg[i-1] + nums[i]);
            neg[i] = max(neg[i-1],pos[i-1]- nums[i]);
        }
        
        long long ans = 0;
        for(auto a: pos)ans = max(ans,a.second);
        for(auto a: neg) ans = max(ans,a.second);
        return ans;
        
        
    }
};