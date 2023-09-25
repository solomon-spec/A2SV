class Solution {
public:
    map<int,map<int,int>> memo;

        
    int dp(int i,int j,string &text1, string &text2){
        
        if (memo[i][j] == -1){
            if (text1[i] == text2[j])
                memo[i][j] = dp(i-1,j-1,text1,text2) + 1;
            else{
           
                memo[i][j] = max(dp(i-1,j,text1,text2),dp(i,j-1,text1,text2));
               
            }
        }
        
        return memo[i][j];
    }
            
    int longestCommonSubsequence(string text1, string text2) {
      for(int i = 0 ; i < text1.size(); i++){
        for(int j = 0 ; j < text2.size(); j++){
            memo[i][j] = -1;
        }
          }
       
        // for(int i = 0 ; i < text1.size(); i++){
        // for(int j = 0 ; j < text2.size(); j++){
        //     cout<<i << " " << j << " " << memo[i][j]<<endl;
        // }
        //   }
    return  dp(text1.size() - 1,text2.size()- 1,text1,text2);
    } 
};