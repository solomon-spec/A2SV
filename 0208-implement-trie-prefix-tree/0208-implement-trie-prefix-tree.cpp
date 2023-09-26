struct TrieNode{
    TrieNode* children[26];
    bool isEnd = false;
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
            if(!temp->children[c-'a']){ 
                temp->children[c-'a'] = new TrieNode();
            }
            temp  = temp->children[c-'a'];
            
        }
        temp->isEnd = true;
    }
    
    bool search(string word) {
        TrieNode* temp = root;
        for(char c: word){
            if(!temp->children[c-'a']) return false;
            temp = temp -> children[c - 'a'];
    }
        return temp->isEnd;
    }
    
    bool startsWith(string prefix) {
        TrieNode* temp = root;
        for(char c: prefix){
            if(!temp->children[c-'a']) return false;
            temp = temp -> children[c - 'a'];
    }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */