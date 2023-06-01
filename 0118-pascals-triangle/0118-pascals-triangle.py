class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(numRows-1):
            new = [1]
            for i in range(1,len(ans[-1])):
                new.append(ans[-1][i]+ans[-1][i-1])
            new.append(1)
            ans.append(new)
        return ans