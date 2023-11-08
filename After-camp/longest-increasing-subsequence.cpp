class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> arr;
        for(auto a: nums){
            if(lower_bound(arr.begin(),arr.end(),a) == arr.end())arr.push_back(a);
            else *lower_bound(arr.begin(),arr.end(),a) = a;  
        }
        return arr.size();
    }
};