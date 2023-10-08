#define PII pair<int, int>
class Compare {
public:
    bool operator()(PII below, PII above)
    {
        if (below.first > above.first) {
            return true;
        }
        else if (below.first == above.first
                 && below.second < above.second) {
            return true;
        }
 
        return false;
    }
};
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        int vis[101];
        memset(vis,0,sizeof vis);
        int dis[101];
        memset(dis,-1, sizeof dis);
        unordered_map<int,vector<vector<int>>> graph;
        for(auto a: times){
            graph[a[0]].push_back({a[1],a[2]});
        }
        priority_queue<PII, vector<PII>, Compare> queue;
        
        queue.push({0,k});
       
        int max_dis = 0;
        while(queue.size()){
            auto cur = queue.top();
            //cout<<cur[0]<<" "<<cur[1]<<endl;
            queue.pop();
            
            if(vis[cur.second]) continue;
            vis[cur.second] = 1;
            max_dis = cur.first;
           
            for(auto child: graph[cur.second]){
                
                if(dis[child[0]] == -1 || (cur.second + child[1] < dis[child[0]])){
                    queue.push({cur.first + child[1],child[0]});
                }
            }
        }
        for(int i =1; i <= n ; i++){
            if(vis[i] == 0) return -1;
        }
        return max_dis;
    }
};