int  lowest[41][41];
int dire[4][2] = {{0,1},{1,0},{-1,0},{0,-1}};
class Solution {
    
public:
    
    int shortestPath(vector<vector<int>>& grid, int k) {
        memset(lowest, -1, sizeof lowest);
        queue<vector<int>> bfs;
        int row = grid.size();
        int col = grid[0].size();
        bfs.push({0,0,0,0});
   
        while(bfs.size()){

            vector<int> cur = bfs.front();
            bfs.pop();
            
            if(cur[2] == row - 1 && cur[3] == col -1 && k >= cur[1]) return cur[0];
            if(lowest[cur[2]][cur[3]] != -1 && lowest[cur[2]][cur[3]] <= cur[1]) continue;
            lowest[cur[2]][cur[3]] = cur[1];
            
            for(auto dir: dire){
                int r = dir[0] + cur[2];
                int c = dir[1] + cur[3];
                
                if(0 <= r && r < row && 0 <= c && c < col){
                    int x = cur[1] + grid[r][c];
                   
                    if((lowest[r][c] == -1) || (x < lowest[r][c] && x <= k )){
                        bfs.push({cur[0]+1,x,r,c});
                        
                    }
                }
                
            }
        }
        return -1;
    }
};