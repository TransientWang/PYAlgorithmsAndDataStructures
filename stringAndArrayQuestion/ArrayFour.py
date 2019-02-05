# -*- coding: UTF-8 -*-
import math


def combinationSum3(k, n):
    """
    216. 组合总和 III
    回溯
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    res = []
    math.sqrt()

    def find(s_list, begin, end):
        if len(s_list) == k:
            if sum(s_list) == n:
                res.append(s_list)
            return
        for i in range(begin, end):
            find(s_list + [i], i + 1, end)

    find([], 1, min(n, 10))
    return res


def containsNearbyAlmostDuplicate(nums, k, t):
    """
    220. 存在重复元素 III
    滑动窗口
    :type nums: List[int]
    :type k: int
    :type t: int
    :rtype: bool
    """
    # n = len(nums)
    # if t == 0 and n == len(set(nums)):
    #     return False
    #
    # for i in range(len(nums)):
    #     j = i + 1
    #     while j < len(nums) and j - i <= k:
    #         t1 = nums[i]
    #         t2 = nums[j]
    #         if abs(t1 - t2) <= t:
    #             return True
    #         j += 1
    # return False
    lenth = len(nums)
    a = set()  # set集合，是一个无序且不重复的元素集合。
    for i in range(lenth):
        if t == 0:
            if nums[i] in a:
                return True
        else:
            for atem in a:
                if abs(nums[i] - atem) <= t:
                    return True
        a.add(nums[i])
        if len(a) == k + 1:
            a.remove(nums[i - k])
    return False


def maximalSquare(matrix):
    """
    221. 最大正方形
    动态规划：dp[x][y] 代表以matrix[x][y]为右下角的正方形的最大面积
    最长边 = min(dp[x][y - 1], dp[x - 1][y], dp[x - 1][y - 1]) + 1
    :type matrix: List[List[str]]
    :rtype: int
    """
    # 解法 1
    # if not matrix:
    #     return 0
    # dp = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
    # res = 0
    # for x in range(len(matrix)):
    #     if matrix[x][0] == "1":
    #         res = 1
    #         dp[x][0] = 1
    # for y in range(len(matrix[0])):
    #     if matrix[0][y] == "1":
    #         res = 1
    #         dp[0][y] = 1
    # for x in range(1, len(matrix)):
    #     for y in range(1, len(matrix[0])):
    #         if matrix[x][y] == "1":
    #             # 正方形条件
    #             t = min(dp[x][y - 1], dp[x - 1][y], dp[x - 1][y - 1]) + 1
    #             if t > 1:
    #                 dp[x][y] = t
    #                 res = max(dp[x][y], res)
    #             else:
    #                 dp[x][y] = 1
    # return res ** 2
    # 解法 2
    if not matrix:
        return 0
    row = [0] * len(matrix[0])  # 竖着的边的长度
    min_bian = 0
    for i in range(len(matrix)):
        flag = 0  # 在每一行遇到 竖边大于最小正方形边长的时候，flag+=1如果 flag == min_bian + 1则证明遇到了一个更大的正方形
        for j in range(len(matrix[0])):
            row[j] = row[j] + 1 if matrix[i][j] == '1' else 0  # 求每列的中最长竖边
            flag = flag + 1 if row[j] > min_bian else 0  # 求遇到竖边大于 min_bian 的时候，横边有多长
            if flag == min_bian + 1:  # 遇到更大的正放形
                min_bian += 1
                flag = 0
    return min_bian * min_bian


if __name__ == '__main__':
    print(maximalSquare([["0", "1", "1", "0", "0"],
                         ["1", "1", "1", "0", "0"],
                         ["1", "1", "1", "1", "1"],
                         ["1", "0", "0", "1", "0"]]))
