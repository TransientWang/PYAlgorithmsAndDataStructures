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
    :param matrix:
    :return:
    '''
    map = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x = 0
    y = 0
    k = 4
    h = 0
    t1 = len(matrix[0]) - 1
    t2 = len(matrix) - 1
    t = t1
    for i in range(len(matrix) * len(matrix[0])):
        print(matrix[x][y], end=" ")
        h += 1

        x += map[k % 4][0]
        y += map[k % 4][1]
        if h == t:
            if t == t1:
                t = t2
            else:
                t = t1
            h = 0
            k += 1


if __name__ == '__main__':
    print(spiralOrder([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]))
