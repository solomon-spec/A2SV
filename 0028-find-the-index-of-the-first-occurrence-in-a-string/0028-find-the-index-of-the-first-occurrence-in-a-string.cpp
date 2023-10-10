#define ll long long
ll power(ll x, unsigned int y, int p) 
{ 
    int res = 1;   
 
    x = x % p; 
  
    if (x == 0) return 0; 
 
    while (y > 0) 
    { 
        if (y & 1) 
            res = (res*x) % p; 
        y = y>>1; 
        x = (x*x) % p; 
    } 
    return res; 
} 
class Solution {
public:
    
    int strStr(string haystack, string needle) {
        long long hash = 0;
        long long ned = 0;
        long long mod = pow(10,9)+7;
    
        if(haystack.size() < needle.size()) return -1;
        int siz = needle.size()-1;
        int cur = siz;
        for(auto a: needle){
            ned += ((a - 'a'+1)*power(26,cur,mod)) % mod;
            cur--;
        }
        ned = ned % mod;
        cur = siz;
        
        for(int i = 0; i < haystack.size(); i++){
            if(i <= siz ){
                
                hash = (hash + (haystack[i] - 'a'+1)*power(26,cur,mod)) % mod;
                cur--;
            }
            else{
                
                hash = (hash * 26);
                hash -= (((haystack[i-siz-1] - 'a' + 1)*power(26,siz+1,mod)) % mod) % mod;
                hash = (hash +(haystack[i] - 'a'+1)) % mod;
                if (hash < 0)hash = mod + hash;
            }
            
            if (hash == ned) return i-siz;
            
        }
        return -1;
    }
};