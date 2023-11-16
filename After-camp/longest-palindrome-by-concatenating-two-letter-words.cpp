class Solution {
int arr[720];
int rv,cur;
public:
    int longestPalindrome(vector<string>& words) {
        memset(arr,0,sizeof arr);
        int ans = 0;
        for(auto a: words){
            rv = (a[1] - 'a' + 1)*26 + (a[0] - 'a' + 1);
            if(arr[rv]){
                ans += 4;
                arr[rv]--;
            }
            else{
                cur = (a[0] - 'a' + 1)*26 + (a[1] - 'a' + 1);
                cur[arr]++;
            }
        }
        for(int i = 1; i <= 26;i++){
            if(arr[i*26 + i]){
                ans += 2;
                break;
            }
        }
        return ans;
    }
};