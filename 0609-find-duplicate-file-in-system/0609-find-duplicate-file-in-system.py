from collections import defaultdict
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)
        answer = []
        for pat in paths:
            pathlist = pat.split(" ")
            for i in range(1,len(pathlist)):
                path = pathlist[i]
                #print(pathlist[i])
                start = path.index("(")
                files = path[start:-1]
                dic[files].append(pathlist[0]+"/" + path[:start])
        for i in dic:
            if len(dic[i])>1:
                answer.append(dic[i])
        return answer
                
                
            
            