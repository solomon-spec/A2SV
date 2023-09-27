#define lli long long int
#define ll long long

struct TrieNode{
    TrieNode* children[2];
    bool isEnd = false;
};

class Trie {
public:
    TrieNode* root;
    Trie() {
        root = new TrieNode();

    }
    
    void insert(int num) {
        TrieNode* temp = root;
        lli cur = pow(2,35);
        while(cur){
            int index;
            if(num & cur) index = 1;
            else index = 0;
            if(!temp->children[index])temp->children[index] = new TrieNode();
            temp = temp->children[index];
            cur >>= 1;
        }
        //cout<<cur<<endl;
    }
    
    lli search(int num) {
        TrieNode* temp = root;
        lli total = 0;
        lli cur = pow(2,35);
        while(cur){
            int index;
            if(num & cur) index = 0;
            else index = 1;
            //cout<<num <<" "<<cur<<" " <<index<<" "<<bool(temp->children[index])<<endl;
            
            if(temp->children[index]) {total += cur;temp=temp->children[index];}
            else {temp=temp->children[ 1- index];}
            cur >>=1;
        }
        //cout<<"end of operation "<<endl;
        return total;
    }
    
};

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        Trie trie;
        for(int i = 0;i < nums.size(); i++){
            trie.insert(nums[i]);
        }
        lli ans = 0;
        for(int i = 0; i < nums.size(); i++){
            int cur = nums[i];
            ans = max(ans,trie.search(cur));
           
            
        }
        

    return ans;
    }
};