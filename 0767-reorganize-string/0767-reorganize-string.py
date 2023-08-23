class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        arr = []
        for i in count:
            arr.append([-count[i],i])
        
        heapify(arr)
        ans = []
      
        while arr:
            
            al,a = heappop(arr)
            
            if ans and ans[-1] == a :
                
                if not arr:
                    return ""
                
                bl,b = heappop(arr)
                ans.extend([b,a])
                
                if al <= -2:
                    heappush(arr,[al+1,a])
                    
                if bl <= -2:
                    heappush(arr,[bl+1,b])
                    
            else:
                ans.append(a)
                if al <= -2:heappush(arr,[al+1,a])
        return "".join(ans)
                    
                
                