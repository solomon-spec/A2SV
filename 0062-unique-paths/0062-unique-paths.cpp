class Solution {
public:
    int uniquePaths(int m, int n) {
        if(n == 1 || m == 1) return 1;
        int x = m + n - 2;
        int y = min(n-1,m-1);
        unsigned long long ans = 1;
        for (int i=1; i<=y; i++) ans = ans*(x-y+i)/i; 
        return ans;
        
    }
};