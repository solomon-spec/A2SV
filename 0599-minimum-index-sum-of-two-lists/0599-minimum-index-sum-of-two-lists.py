class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}
        for i in range(len(list1)):
            dic[list1[i]] = i
        dic2 = {}
        answer = []
        for i in range(len(list2)):
            if list2[i] in dic:
                dic2[list2[i]] = i + dic[list2[i]]
        minn = min(dic2.values())
        for i in dic2:
            if dic2[i] == minn:
                answer.append(i)
        return answer