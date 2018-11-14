# -*- coding: UTF-8 -*-


def sortCount(nums, min, max):
    '''
    计数排序：
    思想：首先需要知道这个数组中的最大值和最小值分别是多少
    然后维护一个 max-min+1的数组 用于保存 索引位置数-min 在待排序数组里的每一个数字数组出现的此时
    辅助数组索引就是待排序数组每个数字按大小顺序排列出现的次数了
    然后通过辅助数组来重新构建
    数组的索引加上最小值就是原数组的数字
    :param nums: 待排序数组
    :param min: 数组中的最小值
    :param max: 数组中的最大值
    :return:
    '''
    tmp = [0 for i in range(max - min + 1)]
    for i in nums:
        tmp[i - min] += 1
    q = 0
    for i in range(len(tmp)):
        while tmp[i] > 0:
            nums[q] = i
            q += 1
            tmp[i] -= 1

    print(nums)


if __name__ == '__main__':
    sortCount([2, 0, 2, 1, 1, 0], 0, 2)
