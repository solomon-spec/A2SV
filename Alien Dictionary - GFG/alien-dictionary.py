#User function Template for python3
from collections import defaultdict, deque
class Solution:
    def findOrder(self,alien_dict, N, K):
        arr = defaultdict(int)
        dic = defaultdict(list)
        sett = set([chr(i + 97) for i in range(k)])
        for i in range(1,len(alien_dict)):
            for j in range(len(alien_dict[i-1])):
                if alien_dict[i][j] != alien_dict[i -1][j]:
                    dic[alien_dict[i-1][j]].append(alien_dict[i][j])
                    arr[alien_dict[i][j]] += 1
                    arr[alien_dict[i-1][j]] = arr[alien_dict[i-1][j]]
                    break;
        queue = deque()
        for i in sett:
            if arr[i] == 0: queue.append(i)
        ans = []
        
        while queue:
            x = queue.popleft()
            ans.append(x)
            for i in dic[x]:
                arr[i] -= 1
                if arr[i] == 0: queue.append(i)
        return "".join(ans)
        
        
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends