class dsu{
    public:
        int parent[301];
        dsu(int n){
            for(int i = 0; i < n; i++)parent[i] = i;
        }
        int find(int x){
            if(parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        void uni(int x, int y){
            int parx = find(x);
            int pary = find(y);
            parent[parx] = pary;
        }
};
class Solution {
    
public:
    bool check(string a, string b){
        int diff = 0;
        for(int i = 0; i < a.size(); i++)
            if(a[i] != b[i]) diff++;
        return 2 >= diff;
    }
    int numSimilarGroups(vector<string>& strs) {
        dsu uf(strs.size());
         for(int i = 0; i < strs.size(); i++)
             for(int j = 0; j < strs.size(); j++){
                 if(check(strs[i],strs[j]))uf.uni(i,j);
             }
       
        unordered_set<int> vis;
        for(int i = 0; i < strs.size(); i++)vis.insert(uf.find(i));
        return vis.size();
    }
};