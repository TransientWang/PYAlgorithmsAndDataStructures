# -*- coding: UTF-8 -*-
def productExceptSelf(nums):
    '''
    给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
    其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
    :param nums:
    :return:
    '''
    r = [1 for i in range(len(nums))]
    r1 = [1 for i in range(len(nums))]
    res = [1 for i in range(len(nums))]

    for i in range(len(nums) - 1):
        r[i + 1] = nums[i] * r[i] if i >= 0 else nums[i]

    for i in range(1, len(nums)):
        r1[i] = nums[-i] * r1[i - 1] if i >= 0 else nums[-i]

    r1.reverse()

    for i in range(len(nums)):
        res[i] = r[i] * r1[i]
    return res


def spiralOrder(matrix):
    '''
    给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
    思路：这个问题 需要考虑的方面有两个，一个是遍历的方向，另一个是每一方向遍历的步数，
    方向可以有四个，步数每一方向走完，下次在走这个方向的时候就会减少一
    :param matrix:
    :return:
    '''
    row = len(matrix) - 1
    if row == -1 or row == 0:
        return matrix
    if row == 0:
        return matrix[0]
    column = len(matrix[0])
    map = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 记录方向
    vector = 0  # 标记方向
    x = 0
    y = -1
    res = []
    while row >= 0 and column > 0:  # 将横向和走向放在一起走，注意横向步数条件是 >0
        for i in range(column):  # 走横向
            x += map[vector % 4][0]
            y += map[vector % 4][1]
            res.append(matrix[x][y])
        vector += 1
        for j in range(row):  # 走纵向
            x += map[vector % 4][0]
            y += map[vector % 4][1]
            res.append(matrix[x][y])
        vector += 1
        row -= 1
        column -= 1
    return res


def firstMissingPositive(nums):
    '''
    丢失的第一个正整数
    将找到的元素放到正确的位置，如果发现某个元素一直没找到，则该元素即为所求

    循环不变式：如果某命题初始为真，且每次改变后仍保持该命题为真，则若干次改变后该命题为真
    只允许时间复杂度O(n)的算法，并且只能使用常数级别的空间。

    分析：把当前数放到该放的位置即可，如1应该放到第0个位置，2应该放到第1个位置。
        :param nums:
    :return:
    '''
    i = 0
    while i < len(nums):
        if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
            tmp = nums[i]
            nums[i] = nums[tmp - 1]
            nums[tmp - 1] = tmp
        else:
            i += 1
    print(nums)
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1


if __name__ == '__main__':
    print(firstMissingPositive([3, 4, -1, 1]))
