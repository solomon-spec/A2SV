class Solution {
    int arr[24*60*2 + 10];
public:
    int findMinDifference(vector<string>& timePoints) {

        memset(arr,0,sizeof arr);
        int ans = 1'000'000'007;
        string a;
        for(int i = 0 ; i < timePoints.size(); i++){
            a = timePoints[i];
            int cur = stoi(a.substr(0,2))*60 + stoi(a.substr(3));
            if(arr[cur])return 0;
            arr[cur]++;
            arr[cur + 24*60]++;
        }
        int prev = -1000000;
        for(int i = 0; i < 24*60*2; i++){
            if(arr[i]){
                ans = min(ans,i - prev);
                prev = i;
            }
        }
        return ans;
    }
};