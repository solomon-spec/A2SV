class dsu{
    public:
        int parent[100005];
        int ds[100005];
        int find(int x){
            if(parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        void uni(int x, int y){
            int parx = find(x);
            int pary = find(y);
            if(ds[pary]) parent[parx] = pary;

            else parent[pary] = parx;

        }
};
bool sort2d(vector<int> &a, vector<int> &b){return a[2] < b[2];}
class Solution {
    
    dsu uf;
public:
    
    
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        sort(meetings.begin(),meetings.end(),sort2d);
        memset(uf.ds,0,n*4);
        int i = 0;
        uf.ds[firstPerson] = 1;
        uf.ds[0] = 1;

        while(i < meetings.size()){
            int j = i;
            while( j < meetings.size() && meetings[i][2] == meetings[j][2] ){
                auto cur = meetings[j];
                uf.parent[cur[0]] = cur[0];
                uf.parent[cur[1]] = cur[1];
                j++;
            }
            
            for(int y = i; y < j; y++){
                auto cur = meetings[y];
                
                uf.uni(cur[0],cur[1]);
                if(uf.ds[cur[0]] || uf.ds[cur[1]])uf.ds[uf.find(cur[0])] = 1;
            }
             for(int y = i; y < j; y++) if (uf.ds[uf.find( meetings[y][0])]){
                 uf.ds[meetings[y][0]]  = 1;
                  uf.ds[meetings[y][1]]  = 1;
             }
            
            i = j;
            
        }
        
        vector<int> ans;
        for(int i = 0; i < n;i++)if(uf.ds[i])ans.push_back(i);
        return ans;
    }
};