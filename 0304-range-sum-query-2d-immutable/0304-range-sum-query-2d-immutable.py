class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        arr = matrix
        prefix = [[0]*(len(arr[0]) + 1) for i in range(len(arr) + 1)]
        for row in range(1,len(matrix) + 1):
            for column in range(1, len(matrix[0]) + 1):
                prerow = prefix[row - 1][column]
                precol = prefix[row][column - 1]
                exclude = prefix[row - 1][column - 1]
                prefix[row][column] = prerow + precol - exclude + arr[row - 1][column - 1]
        self.prefix = prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summ = self.prefix[row2 + 1][col2 + 1] + self.prefix[row1][col1] - self.prefix[row2 + 1][col1] - self.prefix[row1][col2 + 1]
        return summ


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)