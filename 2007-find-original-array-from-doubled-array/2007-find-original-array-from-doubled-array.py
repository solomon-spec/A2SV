class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        answer = []
        dic = defaultdict(int)
        for num in changed:
            dic[num] += 1
        arr = sorted(list(dic.keys()), reverse = True)
        for i in arr:
            if i in dic and dic[i] != 0:
                if i != 0 and dic[i/2] < dic[i]:
                    return []
                elif i != 0:
                    dic[i/2] -= dic[i]
                    answer += [int(i/2)]*dic[i]
                    dic[i] == 0
                    dic
        if 0 in dic:
            if dic[0] % 2 == 1:
                return []
            else:
                answer += [0]* (int(dic[0]/2))
        return answer