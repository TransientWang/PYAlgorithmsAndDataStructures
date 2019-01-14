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
    优化：将剪枝函数的条件分别用list记录，空间换时间
    :type n: int
    :rtype: List[List[str]]
    """

    x = [-1 for i in range(n)]  # x[i] 代表第i行第x[i]列
    res = []

    def validate(t):
        for i in range(t):
            if x[i] != -1 and x[t] != -1 and x[i] == x[t] or fabs(t - i) == fabs(x[t] - x[i]):
                return False
        return True

    def backtrack(t=0):
        if t >= n:
            res.append(map(lambda d: "." * d + "Q" + "." * (n - d - 1), x))
            return
        for j in range(n):
            x[t] = j
            if validate(t):
                backtrack(t + 1)

    backtrack()
    return res


def totalNQueens(n):
    """
    52. N皇后 II
    :type n: int
    :rtype: int
    """
    count = [0]
    x = [-1 for i in range(n)]

    def validate(t):
        for i in range(t):
            if x[i] != -1 and x[t] != -1 and x[i] == x[t] or fabs(t - i) == fabs(x[t] - x[i]):
                return False
        return True

    def backtrack(t=0):
        if t >= n:
            count[0] += 1
            return
        for j in range(n):
            x[t] = j
            if validate(t):
                backtrack(t + 1)

    backtrack()
    return count[0]


def getPermutation(n, k):
    """
    60. 第k个排列
    直接用回溯法做的话需要在回溯到第k个排列时终止就不会超时了, 但是效率依旧感人
    可以用数学的方法来解, 因为数字都是从1开始的连续自然数, 排列出现的次序可以推
    算出来, 对于n=4, k=15 找到k=15排列的过程:

    1 + 对2,3,4的全排列 (3!个)
    2 + 对1,3,4的全排列 (3!个)         3, 1 + 对2,4的全排列(2!个)
    3 + 对1,2,4的全排列 (3!个)-------> 3, 2 + 对1,4的全排列(2!个)-------> 3, 2, 1 + 对4的全排列(1!个)-------> 3214
    4 + 对1,2,3的全排列 (3!个)         3, 4 + 对1,2的全排列(2!个)         3, 2, 4 + 对1的全排列(1!个)

    确定第一位:
        k = 14(从0开始计数)
        index = k / (n-1)! = 2, 说明第15个数的第一位是3
        更新k
        k = k - index*(n-1)! = 2
    确定第二位:
        k = 2
        index = k / (n-2)! = 1, 说明第15个数的第二位是2
        更新k
        k = k - index*(n-2)! = 0
    确定第三位:
        k = 0
        index = k / (n-3)! = 0, 说明第15个数的第三位是1
        更新k
        k = k - index*(n-3)! = 0
    确定第四位:
        k = 0
        index = k / (n-4)! = 0, 说明第15个数的第四位是4
    最终确定n=4时第15个数为3214

    :type n: int
    :type k: int
    :rtype: str
    """
    import math
    # u, k0 = [-1] * n, 0
    #
    # for i in range(n):
    #     for j in range(n):
    #         if j + 1 not in u:
    #             _k0 = k0 + math.factorial(n - i - 1)
    #             if _k0 >= k:
    #                 u[i] = j + 1
    #                 break
    #             else:
    #                 k0 = _k0
    # return ''.join([str(x) for x in u])

    #####
    seq, k, fact = '', k - 1, math.factorial(n - 1)
    perm = [i for i in range(1, n + 1)]
    for i in range(n)[::-1]:
        curr = perm[int(k // fact)]
        seq += str(curr)
        perm.remove(curr)
        if i > 0:
            k %= fact
            fact /= i
    return seq


if __name__ == '__main__':
    print(getPermutation(4, 15))
