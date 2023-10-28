class Solution {
   
public:
    int maximumPopulation(vector<vector<int>>& logs) {
        vector<int> line(102,0);
        for( auto a : logs){
            line[a[0]-1950] += 1;
            line[a[1] - 1950] -= 1;
        }
        for(int i = 1; i < 102; i++)line[i] += line[i - 1];
        int mxm = *max_element(line.begin(),line.end());
        cout<<mxm;
        for(int  i =0 ; i < 102; i++)
            if(line[i] == mxm) return i + 1950;
        return 2050;
        
    }
};