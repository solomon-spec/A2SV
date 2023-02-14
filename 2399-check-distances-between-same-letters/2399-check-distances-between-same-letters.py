class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        dic = {}
        for index in range(len(s)):
            if s[index] not in dic:
                dic[s[index]] = index
            else:
                if index - dic[s[index]] - 1 != distance[ord(s[index]) % 97]:
                    return False
        return True