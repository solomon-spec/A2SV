class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        ans = []
        
        def check(word1,word2):
            dif = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    dif += 1
            if dif == 1: return True
            else: return False
            
            
        queue = deque([([beginWord])])
        visited = defaultdict(int)
        visited[beginWord] = 1
        while queue:
            arr = queue.popleft()
            
            if ans and len(ans[0]) < len(arr): return ans
            for i in range(len(wordList)):
                if check(arr[-1],wordList[i]):

                    if wordList[i] == endWord:
                        if not ans or len(ans[0]) == len(arr) + 1:
                            ans.append(arr+[endWord])
                    if  wordList[i] not in visited:
                        queue.append(arr+[wordList[i]])
                        visited[wordList[i]] = len(arr) +1
                        
                    elif len(arr) == visited[arr[-1]]:
                        queue.append(arr+[wordList[i]])
        
        return ans
        
                        
                    
                
            
            