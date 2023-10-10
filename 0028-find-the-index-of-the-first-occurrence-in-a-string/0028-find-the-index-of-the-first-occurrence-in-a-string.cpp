class Solution {
public:
    
    int strStr(string haystack, string needle) {
        vector<int> ans;
        bool b = false;
        int pre = 0;
        int cur = 1;
        ans.push_back(0);
        while(cur < needle.size()){
            if(needle[cur]==needle[pre]){
                ans.push_back(pre+1);
                cur++;pre++;
            }
            else{
                if(pre == 0){
                    ans.push_back(0);
                    cur++;
                }
                else{
                    pre = ans[pre-1];
                }
            }
        }
        for(auto a: ans)cout<<a<<" ";
        cout<<endl;
        int j = 0;
   
        int i = 0;
        while(i < haystack.size()){
            if(haystack[i] == needle[j]){j++;i++;}
            else{
                if (j != 0){ j = ans[j-1];}
                else i++;
                
            }
            
            if (j == needle.size()) return i-j;
            
        }
        return -1;
    }
};