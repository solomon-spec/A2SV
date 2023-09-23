class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans = {-1,-1};
        for(int i = 0; i < nums.size(); i ++){
            for(int j = 0; j < nums.size(); j++ ){
                if(j != i && nums[i] + nums[j] == target){
                    ans  = {i,j};
                    return ans;
                }
            }
        
        }
        return ans;
        
    }
};