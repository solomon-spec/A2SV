
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = strs[0];
        for(string word: strs){
            for(int i = 0; i < word.size(); i++){
                if (i < prefix.size() && prefix[i] != word[i]){
                    prefix = prefix.substr(0,i);
                }
            
            }
            prefix =  prefix.substr(0,min(prefix.size(),word.size()));
        }
        return prefix;
    }
};