# -*- coding: UTF-8 -*-

def permuteUnique(nums):
    """
    47. 全排列 II
    思路：排序+ DFS + 与前面数字相同剪枝
    与 组合总和2 相似
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    nums.sort()

    def backTrack(nums):
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            num = nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            sub = backTrack(nums[:i] + nums[i + 1:])
            for j in sub:
                res.append(j + [num])
        return res

    res = backTrack(nums)
    return res


from math import fabs

from copy import deepcopy


def solveNQueens(n):
    """
    51.N皇后
    :type n: int
    :rtype: List[List[str]]
    """

    help = [["." for i in range(n)] for i in range(n)]
    x = [-1 for i in range(n)]
    res = []

    def validate(t):
        for i in range(t):
            if x[i] != -1 and x[t] != -1 and x[i] == x[t] or fabs(t - i) == fabs(x[t] - x[i]):
                return False
        return True

    def backtrack(t=0):
        if t >= n:
            print(list(map(lambda d: "." * d + "Q" + "." * (n - d - 1), x)))
            res.append(map(lambda d: "." * d + "Q" + "." * (n - d - 1), x))

            return
        for j in range(n):
            x[t] = j
            if validate(t):
                help[t][x[t]] = "Q"
                backtrack(t + 1)
                help[t][x[t]] = "."

    backtrack()
    return res


if __name__ == '__main__':
    print(solveNQueens(4))
