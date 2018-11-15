# -*- coding: UTF-8 -*-
import math

import copy


class play(object):
    '''n皇后问题'''
    count = 0  # 结果数量
    n = 8;  # 皇后数量
    x = [0]  # x[i]表示第i个皇后在第几列

    def place(self, t):

        ok = True
        for i in range(0, t):
            if self.x[i] == self.x[t] or math.fabs(t - i) == math.fabs(self.x[t] - self.x[i]):
                ok = False
                break
        return ok

    # t是层数
    def backTrack(self, t):
        if t >= self.n:
            self.count += 1
            for i in range(0, len(self.x)):
                print((self.x[i] + 1), end=' ')
            print('\n')
        else:
            # j是列数
            for j in range(0, self.n):
                self.x[t] = j
                if self.place(t):
                    self.backTrack(t + 1)


'''
给定一个没有重复数字的序列，返回其所有可能的全排列。
'''


def permute(nums):
    import copy
    if not nums:
        return
    res = []
    if len(nums) == 0:
        return res
    if len(nums) == 0:
        return [nums]

    def backTrack(before, nums):
        now = copy.deepcopy(before)
        if len(nums) == 1:
            now.append(nums[0])
            res.append(now)
        else:
            for i in range(len(nums)):
                now.append(nums[i])
                backTrack(now, nums[0:i] + nums[i + 1:])
                now.pop()

    for i in range(len(nums)):
        backTrack([nums[i]], nums[:i] + nums[i + 1:])

    return res


def permuteOne(nums):
    if len(nums) == 1:
        return [nums]
    res = []
    for i in range(len(nums)):
        num = nums[i]
        sub = permuteOne(nums[:i] + nums[i + 1:])
        for j in sub:
            res.append([num] + j)
    return res


def subsets(nums):
    res = [[]]
    for i in range(len(nums)):
        sub = subsets(nums[i + 1:])
        for j in sub:
            t = [nums[i]] + j
            res.append(t)
    return res


def exist(board, word):
    '''
    给定一个二维网格和一个单词，找出该单词是否存在于网格中。

    单词必须按照字母顺序，通过相邻的单元格内的字母构成，
    其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
    思路：回溯法，剪枝条件为 边界值 和 当前位置的值 是否是word[i]的值
    同时将已遍历过的索引设置一个标记让防止重复遍历 在遍历完四周还要恢复
    :param board:
    :param word:
    :return:
    '''
    row = len(board)
    colum = len(board[0])

    def find(x, y, i):
        if x < 0 or y < 0 or x > row - 1 or y > colum - 1 or board[x][y] != word[i]:
            return False
        t = board[x][y]
        if i == len(word) - 1 and t ==word[i]:
            return True
        board[x][y] = 0
        bool = find(x + 1, y, i + 1) or find(x - 1, y, i + 1) or find(x, y + 1, i + 1) or find(x, y - 1, i + 1)
        board[x][y] =t
        return bool

    for i in range(row):
        for j in range(colum):
            if board[i][j] == word[0]:
                if find(i, j, 0):
                    return True

    return False


if __name__ == '__main__':
    print(exist([["a"]],
"ab"))
