class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0,r = nums.size() - 1;
        int mid = 0;
        while(l <= r){
            mid = (l+r)/2;
            if(nums[mid] > nums[nums.size()-1]) l = mid + 1;
            else r = mid - 1;
        }
       
        if(target > nums[nums.size()-1]){
            r = l - 1;
            l = 0;
        }
        else{
            r = nums.size() - 1;
        }
        
         while(l <= r){
            mid = (l+r)/2;
            if(nums[mid] < target) l = mid + 1;
            else r = mid - 1;
        }
        if(0 <= l && l < nums.size() && nums[l] == target)return l;
        return -1;
    }
};