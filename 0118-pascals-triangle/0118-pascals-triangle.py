class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(numRows-1):
            ans.append([1])
            for i in range(1,len(ans[-2])):
                ans[-1].append(ans[-2][i]+ans[-2][i-1])
            ans[-1].append(1)
        return ans