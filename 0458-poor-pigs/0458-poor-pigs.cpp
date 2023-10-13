class Solution {
public:
    int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        int tries = minutesToTest/minutesToDie;
        int ans = 0;
        while(pow(tries+1,ans) < buckets) ans++;
        return ans;
    }
};