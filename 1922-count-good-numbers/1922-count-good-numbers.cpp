
class Solution {
public:
    long long power(long long x,unsigned long long y, int p) { 
        int res = 1;   
        x = x % p; 
        if (x == 0) return 0; 

        while (y > 0) { 
            if (y & 1) res = (res*x) % p; 
            
            y = y>>1; 
            x = (x*x) % p; 
        } 
        return res; 
    } 
    int countGoodNumbers(long long n) {
        int x = 20;
        long long ans = power(20,n/2,1000000007);
        if(n % 2) ans = (ans*5) % 1000000007;
        return ans;
    }
};