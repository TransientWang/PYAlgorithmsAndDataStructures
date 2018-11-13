# -*- coding: UTF-8 -*-
'''
给定两个数组，编写一个函数来计算它们的交集。
'''
import math


def singleNumber(nums):
    tmp = nums[0]
    index = 0
    left = 0
    right = 0

    while index < len(nums):
        if tmp == nums[index]:
            right = index
        elif right - left == 0:
            return nums[left]
        else:
            tmp = nums[index]
            left = index
            right = index
        index += 1
    return tmp


def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    i = 0
    j = 0
    res = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] != nums2[j]:
            if nums1[i] < nums2[j] and i < len(nums1):
                i += 1
            elif nums1[i] > nums2[j] and j < len(nums2):
                j += 1
        else:
            if i > j:
                res.append(nums1[i])
            else:
                res.append(nums2[j])
            i += 1
            j += 1
    return res


'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
'''


def moveZeroes(nums):
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


'''
矩阵逆置
'''


def rotate(matrix):
    lens = len(matrix[0]) - 1
    for i in range(int(math.ceil(float(len(matrix[0])) / 2))):
        for j in range(i,lens -i):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[lens -j][i]
            matrix[lens - j][i] = matrix[lens - i][lens -j]
            matrix[lens - i][lens - j] = matrix[j][lens -i]
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

'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。

'''
def lengthOfLISGreedy(nums):
    if len(nums) == 0:
        return 0
    r = [nums[0]] #维护维护一个递增序列
    res = 0
    for i in range(1, len(nums)):
        if nums[i] > r[res]:      #当前元素大于递增序列的右端 直接加上
            r.append(nums[i])
            res += 1
        else: #找到第一个比 nums[i]大的替换
            left = 0
            right = res
            while left < right:
                mid = int((left + (right-1)) /2)
                if nums[i] == r[mid]:
                    left = mid
                    break
                elif r[mid] >= nums[i]:
                    right = mid
                else:
                    left = mid + 1
            r[left] = nums[i]
    return res+1
if __name__ == '__main__':
    print((rotate([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ], )))

