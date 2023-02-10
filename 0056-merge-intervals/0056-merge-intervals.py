class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        maxx = 0
        answer = []
        same = set()
        diffrent = set()
        
        for i in intervals:
            if i[1] > maxx:
                maxx = i[1]
                
        arr = [0]*maxx
        arr += [0]
        
        for i in intervals:
            arr[i[0]] += 1
            arr[i[1]] -= 1
            if arr[i[0]] == arr[i[1]]:
                same.add(i[0])
                
        for i in range(len(arr)):
            arr[i] = arr[i] if i == 0 else arr[i-1] + arr[i]
    
        for num in same:
            if arr[num] != 0:
                diffrent.add(num)
        
        index = 0
        while index < len(arr):
            if arr[index] > 0:
                initial = index
                while index < len(arr) and arr[index] > 0:
                    index += 1
                answer.append([initial,index])
                index += 1
            else:
                if index in same and index not in diffrent:
                    answer.append([index,index])
                index += 1
                
        return answer
                
        
        