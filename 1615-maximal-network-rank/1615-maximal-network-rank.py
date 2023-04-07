class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if len(roads)<2:
            return len(roads)
        dic = defaultdict(set)
        for i in roads:
            dic[i[0]].add(i[1])
            dic[i[1]].add(i[0])
        arr = sorted(dic.keys(),key = lambda x: len(dic[x]))
        
        for i in range(len(arr)):
            if len(dic[arr[i]]) == len(dic[arr[-2]]):
                for j in range(i+1,len(arr)):
                    if arr[j] not in dic[arr[i]] and len(dic[arr[j]]) == len(dic[arr[-1]]): 
                        return len(dic[arr[i]]) + len(dic[arr[j]])        
        return len(dic[arr[-1]]) + len(dic[arr[-2]]) -1
        