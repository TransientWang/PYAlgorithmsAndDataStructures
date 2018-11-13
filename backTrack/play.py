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


if __name__ == '__main__':
    print(subsets([1, 2, 3]))
