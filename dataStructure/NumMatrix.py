# -*- coding: UTF-8 -*-
class NumMatrix(object):

    def __init__(self, matrix):
        """
        304. 二维区域和检索 - 矩阵不可变
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        self.dp = [[0 for i in range(len(matrix[0]) + 1)] for i in range(len(matrix) + 1)]
        for i in range(1, len(matrix) + 1):
            s = 0
            for j in range(1, len(matrix[0]) + 1):
                s += matrix[i - 1][j - 1]
                self.dp[i][j] = s + self.dp[i - 1][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]
        # res = 0
        # for i in range(row1 + 1, row2 + 2):
        #     res += self.dp[i][col2 + 1]
        #     res -= self.dp[i][col1]
        # return res


if __name__ == '__main__':
    n = NumMatrix([
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    )
    print(n.sumRegion(1, 2, 2, 4))
    # Your NumMatrix object will be instantiated and called as such:
    # obj = NumMatrix(matrix)
    # param_1 = obj.sumRegion(row1,col1,row2,col2)
