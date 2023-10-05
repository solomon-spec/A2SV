int  lowest[41][41];
int dire[4][2] = {{0,1},{1,0},{-1,0},{0,-1}};
class Solution {
    
public:
    
    int shortestPath(vector<vector<int>>& grid, int k) {
        memset(lowest, -1, sizeof lowest);
        queue<array<int, 4>> bfs;
        int row = grid.size();
        int col = grid[0].size();
        bfs.push({0,0,0,0});
   
        while(bfs.size()){

            auto [cur0,cur1,cur2,cur3] = bfs.front();
            bfs.pop();
            
            if(cur2 == row - 1 && cur3 == col -1 && k >= cur1) return cur0;
            if(lowest[cur2][cur3] != -1 && lowest[cur2][cur3] <= cur1) continue;
            lowest[cur2][cur3] = cur1;
            
            for(auto dir: dire){
                int r = dir[0] + cur2;
                int c = dir[1] + cur3;
                
                if(0 <= r && r < row && 0 <= c && c < col){
                    int x = cur1 + grid[r][c];
                   
                    if((lowest[r][c] == -1) || (x < lowest[r][c] && x <= k )){
                        bfs.push({cur0+1,x,r,c});
                        
                    }
                }
                
            }
        }
        return -1;
    }
};