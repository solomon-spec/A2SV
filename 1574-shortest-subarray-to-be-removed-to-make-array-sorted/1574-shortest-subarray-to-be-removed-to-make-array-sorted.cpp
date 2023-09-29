class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        vector<int> l;
        
        l.push_back(arr[0]);
        for(int i = 1; i < arr.size();i++){
            if(arr[i] >= arr[i-1])l.push_back(arr[i]);
            else break;
        }
        if(l.size() == arr.size()) return 0;
        vector<int> r;
        r.push_back(arr[arr.size()-1]);
        
        for(int i = arr.size()-2; i >=0;i--){
            if(arr[i] <= arr[i+1])r.push_back(arr[i]);
            else break;
        }
        reverse(r.begin(),r.end());
        
        int ans = max(l.size(),r.size());
        int total = l.size() + r.size();
        for (auto it = l.begin(); it != l.end(); it++){
            int cur = distance(l.begin(),it) + 1 + distance(lower_bound(r.begin(),r.end(),*it),r.end());
            //cout<<distance(lower_bound(r.begin(),r.end(),*it),r.end())<<endl;
            //if(r.find(*it) != r.end()){cout<<"how"; cur ++;}
            //cout<<cur<<endl;
            ans = max(ans,cur);
        }
        
        return arr.size() - ans;
    }
    
};