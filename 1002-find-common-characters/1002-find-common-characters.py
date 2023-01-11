class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        answer = []
        dic  = defaultdict(int)
        for i in words[0]:
            dic[i]+=1
        for i in range(len(words)):
            for x in words[0]:
                counter = words[i].count(x)
                if counter < dic[x]:
                    dic[x] =counter
                    
        for i in dic:
            while dic[i]>0:
                answer.append(i)
                dic[i]-=1
             
        return answer
                