class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        pointer1 = len(players) - 1
        pointer2 = len(trainers) - 1
    
        answer = 0
        while pointer1 >= 0 and pointer2 >= 0:
            if players[pointer1] <= trainers[pointer2]:
                answer += 1
                pointer1 -= 1
                pointer2 -=1
            else:
                pointer1 -= 1
        return answer