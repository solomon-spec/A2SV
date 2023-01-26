class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        left= 0
        right = len(people) - 1
        people.sort()
        answer = 0
        while left <= right:
            if people[right] + people[left] <= limit:
                answer += 1
                left += 1
                right -= 1
    
            else:
                right -= 1
                answer += 1
        return answer