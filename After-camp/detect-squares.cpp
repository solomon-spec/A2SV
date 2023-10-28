class DetectSquares {
public:
    int coor[1001][1001];
    DetectSquares() {
        memset(coor,0,sizeof coor);
    }
    
    void add(vector<int> point) {
        coor[point[0]][point[1]] += 1;
    }
    
    int count(vector<int> point) {
        long long ans = 0;
        for(int i = 0 ; i < 1001; i++){
            int x = point[0],y = point[1];
            if(i != point[0] && y + abs(i - x) < 1001 )
                ans += coor[i][y]*coor[i][y + abs(i - x)]*coor[x][y + abs(i - x)];
            if(i != point[0] && y - abs(i - x) >= 0 )
                ans += coor[i][y]*coor[i][y - abs(i - x)]*coor[x][y - abs(i - x)];
                //cout<<y - abs(i - x)<<endl;
         
        }
        return ans;
    }
};

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares* obj = new DetectSquares();
 * obj->add(point);
 * int param_2 = obj->count(point);
 */