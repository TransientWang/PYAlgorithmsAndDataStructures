# -*- coding: UTF-8 -*-

import math


def singleNumber(nums):
    '''
    136. 只出现一次的数字
    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
    考察点:异或运算符 ^相同为0，不同为1。两个相同的数字^以后为0这样遍历一遍之后的值就是单个值
    '''
    # tmp = nums[0]
    # index = 0
    # left = 0
    # right = 0
    #
    # while index < len(nums):
    #     if tmp == nums[index]:
    #         right = index
    #     elif right - left == 0:
    #         return nums[left]
    #     else:
    #         tmp = nums[index]
    #         left = index
    #         right = index
    #     index += 1
    # return tmp
    res = 0
    for i in nums:
        res ^= i
    return res


def intersect(nums1, nums2):
    '''
    350. 两个数组的交集 II（review）
    :param nums1:
    :param nums2:
    :return:
    '''
    dic = dict()
    res = []
    for i in nums1:
        dic[i] = dic[i] + 1 if i in dic else 1
    for i in nums2:
        if i in dic and dic[i] >= 1:
            res.append(i)
            dic[i] -= 1
    return res


def moveZeroes(nums):
    '''
    给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
    '''

    index = 1
    count = 0
    while index < len(nums):
        tmp = index
        while nums[tmp - 1] == 0:
            count += 0
            nums[tmp - 1] = nums[tmp]
            nums[tmp] = 0
            tmp -= 1
            if tmp == 0:
                break

        index += 1

    print(nums)


def rotate(matrix):
    '''
    矩阵逆置
    '''

    lens = len(matrix[0]) - 1
    for i in range(int(math.ceil(float(len(matrix[0])) / 2))):
        for j in range(i, lens - i):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[lens - j][i]
            matrix[lens - j][i] = matrix[lens - i][lens - j]
            matrix[lens - i][lens - j] = matrix[j][lens - i]
            matrix[j][lens - i] = tmp

    for x in range(len(matrix)):
        for y in range(len(matrix)):
            print((matrix[x][y]), end=' ')
        print("\n")


def reverseString(s):
    i = 0
    j = len(s) - 1
    ss = list(s)

    while i < j:
        tmp = ss[i]
        ss[i] = ss[j]
        ss[j] = tmp
        i += 1
        j -= 1

    return "".join(ss)


def intToRoman(num):
    """
    12. 整数转罗马数字
    思路：贪心选择,首先列出所有表达式的字典，然后从大到小遍历字段。当num>k的时候，由于k是当前最大值，所以将k参与计算
    当num < k 的时候，说明前面到现在已经么有比K更合适的了，只能继续遍历后面更小的值
    :param self:
    :param num:
    :return:
    """

    hlist = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
             (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))
    roman = ""
    for k, v in hlist:
        while num >= k:
            roman += v
            num -= k
    return roman


def nextPermutation(nums):
    """
    31. 下一个排列
    思路：每一个序列和比他更大的序列都有一个公共前缀
    前缀并不需要处理，只考虑不同的后缀
    如果排列都是降序那么就没有比他更大的值了
    如果某一位置比他前面的数更大，那么就需要从此处处理排列，
    从此处向后面找到第一个比它大的数然后交换，
    交换过后该索引的值变大了，需要注意的是索引后面的值应该变得最小才能得到下一个比较大的值，所以需要逆置
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if len(nums) < 1:
        return
    idx = 0
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] > nums[i - 1]:
            idx = i
            break
    if idx != 0:
        for i in range(len(nums) - 1, idx - 1, -1):
            if nums[i] > nums[idx - 1]:
                nums[i], nums[idx - 1] = nums[idx - 1], nums[i]
                break
    nums[idx:] = nums[idx:][::-1]


if __name__ == '__main__':
    print(lengthOfLISGreedy([10, 9, 2, 5, 3, 7, 101, 18]))
