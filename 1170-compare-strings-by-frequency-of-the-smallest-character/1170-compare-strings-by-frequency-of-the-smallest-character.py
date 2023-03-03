class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        arr1, arr2 = [], []
        for i in range(len(words)):
            a = sorted(list(words[i]))
            arr1.append(a.count(a[0]))
        
        for i in range(len(queries)):
            a = sorted(list(queries[i]))
            arr2.append(a.count(a[0]))
            
        answer = []
        arr1.sort()
        
        for query in arr2:
            l = 0
            r = len(arr1)
            while l < r:
                mid = (l+r)//2
                #print(query,arr1[mid])
                if query < arr1[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            #print(arr1[l],query,l)
            if l < len(arr1) and query >= arr1[l]:
                answer.append(len(arr1) - l - 1 )
            else:
                answer.append(len(arr1) - l)
        return answer
                
            
            