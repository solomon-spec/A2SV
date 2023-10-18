class dsu{
    public:
        int parent[301];
        int find(int x){
            if(parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        void uni(int x, int y){
            int parx = find(x);
            int pary = find(y);
            if(pary > parx)parent[parx] = pary;
            else parent[pary] = parx;
        }
};
class Solution {
    dsu uf;
public:
    bool check(string a, string b){
        int diff = 0;
        for(int i = 0; i < a.size() && diff < 3; i++) if(a[i] != b[i]) diff++;
        return 2 >= diff;
    }
    int numSimilarGroups(vector<string>& strs) {
        for(int i = 0; i < strs.size(); i++) uf.parent[i] = i;
         for(int i = 0; i < strs.size(); i++)
             for(int j = 0; j < strs.size(); j++){
                 if(check(strs[i],strs[j]))uf.uni(i,j);
             }
       
        unordered_set<int> vis;
        for(int i = 0; i < strs.size(); i++)vis.insert(uf.find(i));
        return vis.size();
    }
};