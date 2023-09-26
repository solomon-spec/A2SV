struct TrieNode{
    TrieNode* children[26];
    bool isEnd = false;
};
class WordDictionary {
    TrieNode* root;
public:
    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
       TrieNode* temp = root;
        for(char c: word){
            if(!temp->children[c-'a']){ 
                temp->children[c-'a'] = new TrieNode();
            }
            temp  = temp->children[c-'a'];
            
        }
        temp->isEnd = true;
        
    }
    bool dfs(TrieNode* cur_root, string s){
        
        TrieNode* temp = cur_root;
        bool ans = false;
        for(int i = 0; i < s.size(); i++){
            
            if(s[i] == '.'){
                string ss = s.substr(i+1,s.size()-1);
                
                for(int j = 0; j < 26; j++){
                    
                    if(temp->children[j] and dfs(temp->children[j],ss))return true;
                        
                }
                return false;
            }
            else{
                if(!temp->children[s[i]-'a']) return false;
                temp = temp -> children[s[i] - 'a'];
            }
        }
        return temp->isEnd;
          
    }
    bool search(string word) {
        return dfs(root,word);
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */