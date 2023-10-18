class Solution {
public:
    double myPow(double x, long long n) {
        if (n < 0) return 1.0/myPow(x,abs(n));
        else if(n == 0) return 1;
        double val = myPow(x,n/2);
        if(n & 1) return x * val * val;
        else return val*val;
    }
};