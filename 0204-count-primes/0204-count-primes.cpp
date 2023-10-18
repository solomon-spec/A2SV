class Solution {
public:
    int countPrimes(int n) {
        bool arr[n+1];
        memset(arr,true,sizeof arr);

        for(int i = 2; i < n+1; i++){
            if(!arr[i]) continue;
            int div = 2;
            while(div*i <= n){
                arr[div*i] = false;
                div += 1;
            }
            
        }
        int ans = 0;
        for(int i = 2 ; i < n ; i++){
            if(arr[i])ans += 1;
            
        }
        return ans;
    }
};