class Solution {
public:
    int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        int tries = minutesToTest/minutesToDie + 1;
        int ans = 0;
        while(pow(tries,ans) < buckets) ans++;
        return ans;
    }
};