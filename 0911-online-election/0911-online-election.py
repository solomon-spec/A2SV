class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.person = persons
        self.times = times
        dic = defaultdict(int)
        maxx = None
        arr = []
        for i in range(len(persons)):
            dic[persons[i]] += 1
           
            if maxx == None or dic[persons[i]] >= dic[maxx]:
                maxx = persons[i] 
            arr.append(maxx)

        self.winner = arr
        print(arr)

    def q(self, t: int) -> int:
        return(self.winner[bisect_right(self.times,t)-1])
    
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)