# -*- coding: UTF-8 -*-
import unittest
import math


class MyTestCase:
    count = 0  # 结果数量
    n = 8;  # 皇后数量
    x = [-1, -1, -1, -1, -1, -1, -1, -1]  # x[i]表示第i个皇后在第几列

    def test_something(self):
        self.assertEqual(True, True)

    def test_eightQueen(self):
        self.backTrack(0)

    def place(self, t):
        print((self.x[t]))
        ok = True
        for i in range(0, self.n):
            if self.x[i] == self.x[t] and t - i == math.fabs(self.x[t] - self.x[i]):
                ok = False
                break
        return ok

    def backTrack(self, t):
        if t >= self.n:
            self.count += 1
            for i in range(0, len(self.x)):
                print((self.x[i]), end=' ')
            print()
        else:
            for j in range(0, self.n):
                self.x[t] = j
                if self.place(t):
                    self.backTrack(t + 1)


def letterCombinations(digits):
    '''
    17.电话号码的字母组合
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
    '''
    number = ("", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")
    res = []

    def find(dig, t):
        if dig == "":
            res.append(t)
            return
        for i in number[int(dig[0])]:
            find(dig[1:], t + i)

    find(digits, "")
    return res


def fourSum(nums, target):
    """
    18.四数只和
    思路：
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    results = []
    nums.sort()

    def findNsum(left, right, target, N, result):
        if right - left + 1 < N or N < 2 or target < nums[left] * N or target > nums[right] * N:
            return
        if N == 2:
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    results.append(result + [nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1
        else:
            for i in range(left, right + 1):
                if i == left or (i > left and nums[i] != nums[i - 1]):
                    findNsum(i + 1, right, target - nums[i], N - 1, result + [nums[i]])

    findNsum(0, len(nums) - 1, target, 4, [])

    return results


def solveSudoku(board):
    """
    37.解数独
    思路：深度优先搜索+空间换时间
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """

    row = [[False for i in range(10)] for i in range(9)]  # 某一行的数字被摆放
    col = [[False for i in range(10)] for i in range(9)]  # 某一列的数字被摆放
    block = [[False for i in range(10)] for i in range(9)]  # 某一块的数字被摆放
    for x in range(9):
        for y in range(9):
            if board[x][y] != ".":
                num = int(board[x][y])
                row[x][num] = True
                col[y][num] = True
                block[x // 3 * 3 + y // 3][num] = True

    def find(x, y):
        while board[x][y] != ".":
            y += 1
            if y >= 9:
                x += 1
                y = 0
            if x >= 9:
                return True

        for i in range(1, 10):
            block_idx = x // 3 * 3 + y // 3

            if row[x][i] == False and col[y][i] == False and block[block_idx][i] == False:
                board[x][y] = str(i)
                row[x][i] = True
                col[y][i] = True
                block[block_idx][i] = True
                if find(x, y):
                    return True
                else:
                    board[x][y] = "."
                    row[x][i] = False
                    col[y][i] = False
                    block[block_idx][i] = False
        return False

    find(0, 0)

    for i in range(9):
        print(board[i])


def combinationSum(candidates, target):
    """
    39. 组合总和
    思路：排序+dfs+范围剪枝
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    candidates.sort()

    def find(x, d_list):
        tmp = sum(d_list)
        if tmp == target:
            res.append(d_list)
        elif tmp < target:
            for i in range(x, len(candidates)):
                if tmp + candidates[i] <= target or candidates[i] >= target:  # 剪枝条件，首先要排序才有用
                    find(i, d_list + [candidates[i]])
                else:
                    break

    find(0, [])
    return res


def combinationSum2(candidates, target):
    """
    40. 组合总和2
    思路：排序+dfs+范围剪枝+已经计算的值略过
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    res = []
    candidates.sort()

    def find(x, d_list, target):
        if 0 == target:
            res.append(d_list)
            return
        for i in range(x, len(candidates)):  # x>len(candidates)的情况在for里被过滤了
            if i > x and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            find(i + 1, d_list[:] + [candidates[i]], target - candidates[i])

    find(0, [], target)
    return res


if __name__ == '__main__':
    print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
