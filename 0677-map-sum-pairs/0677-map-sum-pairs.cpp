
struct TrieNode{
    TrieNode* children[26];
    long long val = 0;
    int isEnd = -1;
};
class Trie {
public:
    TrieNode* root;
    Trie() {
        root = new TrieNode();

    }
    
    void insert(string word,int num) {
        TrieNode* temp = root;
        for(char c: word){
            
            if(!temp->children[c-'a']){ 
                temp->children[c-'a'] = new TrieNode();
            }
            
            temp->children[c-'a']->val += num;
            temp  = temp->children[c-'a'];   
        }
        
        if(temp->isEnd != -1){
            int diff = temp->isEnd;
            TrieNode* temp = root;
            
            for(char c: word){
                temp->children[c-'a']->val -= diff;
                temp  = temp->children[c-'a'];   
            }
        }
        temp->isEnd = num;
       
    }
    
    long long search(string word) {
        TrieNode* temp = root;
        long long ans = 0;
        for(char c: word){
            if(!temp->children[c-'a']) return 0;
            temp = temp -> children[c - 'a'];
        }
        ans += temp->val;
       return ans;
    }
    

};
class MapSum {
public:
    Trie trie;
    MapSum() {
        
    }
    
    void insert(string key, int val) {
        trie.insert(key,val);
    }
    
    int sum(string prefix) {
        return trie.search(prefix);
    }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum* obj = new MapSum();
 * obj->insert(key,val);
 * int param_2 = obj->sum(prefix);
 */