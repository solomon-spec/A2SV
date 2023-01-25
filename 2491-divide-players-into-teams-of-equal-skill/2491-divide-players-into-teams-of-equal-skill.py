class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        total = skill[0] + skill[-1]
        answer = 0
        
        for i in range(len(skill)/2):
            if skill[i] + skill[-(i+1)] != total:
                return -1
            else:
                answer += skill[i] * skill[-(i+1)]
        
        return answer