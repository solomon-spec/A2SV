

class Solution {
public:
    string removeDuplicates(string s, int k) {
        vector<int> count;
        vector<char> stack;
        for(auto ch: s){
            if(stack.size() && stack[stack.size()-1] == ch){
                count[count.size() -1]++;
            }
            else{
                stack.push_back(ch);
                count.push_back(1);
            }
            while( count.size() && count[count.size()-1] == k){
                stack.pop_back();
                count.pop_back();
            }
        }
        string ans = "";
        
        for(int i = 0 ; i  < count.size(); i++){
            while(count[i]--){
                ans += stack[i];
            }
        }
        return ans;
    }
};