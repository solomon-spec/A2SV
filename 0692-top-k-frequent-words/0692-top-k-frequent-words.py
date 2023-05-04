class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = defaultdict(int)
        for i in words: dic[i] += 1
        x = []
        heapify(x)
        for i in dic:
            if len(x)<k: heappush(x,dic[i])
            else: heappushpop(x,dic[i])
        ans = defaultdict(list)
        for i in dic:
            if dic[i] >= x[0]: ans[dic[i]].append(i)
        answ = []
        for i in reversed(sorted(list(set(x)))):answ += sorted(ans[i])
        return answ[:k]