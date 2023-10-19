struct TrieNode{
    TrieNode* children[29];
    bool isEnd = false;
    bool isEnd2 = false;
};
class Trie {
public:
    TrieNode* root;
    Trie() {
        root = new TrieNode();

    }
    
    void insert(string word) {
        TrieNode* temp = root;
        for(char c: word){
            
            if(c == '/'){
                temp->isEnd2 = true;
                c = '{';
                
            }
            
            if(!temp->children[c-'a']){ 
                temp->children[c-'a'] = new TrieNode();
            }
            temp  = temp->children[c-'a'];
            
        }
        temp->isEnd = true;
        temp->isEnd2 = true;
    }
    
    bool search(string word){
        TrieNode* temp = root;
        int tot = 0;
        //cout<<word<<endl;
        for(int i = 0; i+1 < word.size();i++){
    
            auto c = word[i];
            if(c == '/')c = '{';
           
            temp = temp -> children[c - 'a'];
            if(temp->isEnd2 && temp->isEnd && word[i+1] == '/') return false;
    }
        return true;
    }
};
class Solution {
public:
    vector<string> removeSubfolders(vector<string>& folder) {
        Trie trie;
        
        for(auto a: folder){
            trie.insert(a);
        }
        vector<string> ans;
        for(auto a: folder){
            if(trie.search(a))ans.push_back(a);
        }
        
        return ans;
    }
};