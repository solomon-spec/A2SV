class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        sort(meetings.begin(),meetings.end());
        vector<long long> mxm(n,0);
        vector<long long> free(n,-1);
        for(auto a: meetings){
            bool f = false;
            long long mnm = 100000000000;
            for(int i =0 ; i < n; i++ ){
                if(free[i] <= a[0]){
                    f = true;
                    free[i] = a[1];
                    mxm[i]++;
                    break;
                }
                mnm = min(mnm,free[i]);
                }
            if(!f){
                for(int i =0 ; i < n; i++ )
                    if(free[i] == mnm){
                        free[i] += (a[1] - a[0]);
                        mxm[i]++;
                        break;
                    }
            }
        }
        return distance(mxm.begin(),std::max_element(mxm.begin(), mxm.end()));
  
    }
};