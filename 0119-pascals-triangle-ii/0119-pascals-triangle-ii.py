class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1]*(rowIndex + 1)
        else:
            var = self.getRow(rowIndex - 1)
            ind = []
            for i in range(1,len(var)):
                ind.append(var[i]+var[i - 1])
            return [1] + ind + [1]
        