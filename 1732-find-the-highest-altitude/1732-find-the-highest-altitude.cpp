class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int ans = 0;
        int cur = 0;
        for(auto a: gain){cur += a; ans = max(ans,cur);}
        return ans;
    }
};