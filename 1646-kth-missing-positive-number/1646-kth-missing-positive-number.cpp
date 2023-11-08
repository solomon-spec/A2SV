class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int l = 0, r = arr.size() -1;
        if (k + arr.size() > arr[arr.size() - 1]) 
            return arr[arr.size() - 1] + (k - arr[arr.size() - 1] +arr.size());
        while (l <= r){
            int mid = (l + r)/2;
            if( arr[mid] - mid <= k ) l = mid + 1;
            else r = mid - 1;
        }
        cout<<r<<endl;
        if(r >= 0)return arr[r] + (k - arr[r] + r + 1);
        else return k;
        
        return 10;
    }
};