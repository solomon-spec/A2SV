int pre [100][100];
class Solution {
public:
    vector<bool> checkIfPrerequisite(int numCourses, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        memset(pre, 0, sizeof pre);
        for(auto a: prerequisites) pre[a[0]][a[1]] = 1;
        for(int i = 0; i < numCourses ; i++ ){
            for(int j = 0; j < numCourses ; j++ ){
                for(int k = 0; k < numCourses ; k++ ){
                    pre[j][k] = pre[j][k] | pre[j][i] & pre[i][k];
                }
            }
        }
        vector<bool> ans;
        for(auto a: queries) ans.push_back(bool(pre[a[0]][a[1]]));
        return ans;
    }
};