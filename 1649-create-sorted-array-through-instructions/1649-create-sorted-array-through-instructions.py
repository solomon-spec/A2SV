from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        arr = SortedList()
        dic = defaultdict(int)
        ans = 0
        for i in range(len(instructions)):
            arr.add((instructions[i],i))
            ind = arr.index((instructions[i],i))
            cur = min(ind-dic[instructions[i]],i-ind)
            dic[instructions[i]] += 1
            ans += cur
        return ans %(10**9 + 7)