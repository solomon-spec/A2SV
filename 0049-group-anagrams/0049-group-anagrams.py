class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """ create adefault dictionary with sorted string as key and and the worsd as its value"""
        answer = []
        dic = defaultdict(list)
        for word in strs:
            dic[tuple(sorted(word))].append(word)
            
        for groups in dic:
            answer.append(dic[groups])
            
        return answer