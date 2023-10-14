class Solution {
public:
    int countOrders(int n) {
        int count = n;
        long long ans = 1;
        int mod = pow(10,9) + 7;
        for(int i = 1; i <= n*2;i++){
            if(count && i % 2 == 0){count--; ans = (ans*i/2)% mod;}
            else ans = (ans*i)% mod;
        }
        return ans;
        
    }
};