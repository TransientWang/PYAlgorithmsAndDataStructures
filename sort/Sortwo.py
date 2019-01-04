# -*- coding: UTF-8 -*-

import copy


def wiggleSort(nums):
    '''
    324.摆动排序 II
    :param nums:
    :return:
    '''
    t = nums[:]
    t.sort()
    i = 1
    while i < len(nums):
        nums[i] = t.pop()
        i += 2
    i = 0
    while i < len(nums):
        nums[i] = t.pop()
        i += 2


def wiggleSortOne(nums):
    '''
    324.摆动排序 II
    nums[::2]最后一个2是每隔两个提出来
    摆动排序
    :param nums:
    :return:
    '''
    print(nums[::-1])
    nums.sort()
    half = len(nums[::2]) - 1
    nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]


def findMedianSortedArrays(nums1, nums2):
    '''
    4.寻找两个有序数组的中位数
    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

    你可以假设 nums1 和 nums2 不会同时为空。
    思路：要求时间复杂度为log
    多半都会有分治，二分。堆。出现
    本题采用归并的方法，找出知道能求出中为数的数字即可
    :param nums1:
    :param nums2:
    :return:
    '''
    # lenOne = len(nums1)
    # lenTwo = len(nums2)
    # flag = True
    # mid = 0
    # if (lenOne + lenTwo) % 2 == 0:
    #     flag = False
    # mid = (lenOne + lenTwo) // 2
    # tmp = []
    # i, j = 0, 0
    # while i < lenOne and j < lenTwo and mid >= 0:
    #     if nums1[i] <= nums2[j]:
    #         tmp.append(nums1[i])
    #         i += 1
    #     else:
    #         tmp.append(nums2[j])
    #         j += 1
    #     mid -= 1
    # while mid >= 0 and i < lenOne:
    #     tmp.append(nums1[i])
    #     i += 1
    #     mid -= 1
    # while mid >= 0 and j < lenTwo:
    #     tmp.append(nums2[j])
    #     j += 1
    #     mid -= 1
    # print(tmp)
    # t = tmp[-1] if flag else (tmp[-1] + tmp[-2]) / 2
    # return t

    num = nums1 + nums2
    num.sort()
    mid = (len(num) - 1) // 2
    if len(num) & 0x1:
        return num[mid]
    else:
        return (num[mid] + num[mid + 1]) / 2


def kthSmallest(matrix, k):
    '''
    378	.有序矩阵中第K小的元素
    思路：二分法，如果横向比较那么上一行的元素，不一定全比当前元素小，但是当前元素数值方向上面的元素一定比当前元素小
    :param matrix:
    :param k:
    :return:
    '''

    def getMid(mid):
        """
        二分法，从左下角开始
        只在向右移动时候计数数值方向上的元素个数
        :param mid:
        :return:
        """
        n = len(matrix)
        res = 0
        i = n - 1
        j = 0
        while i >= 0 and j < n:
            if matrix[i][j] > mid:
                i -= 1
            else:
                res += i + 1  # 每次向右移动一位，该值竖直方向向上（包括该值）的i+1位都一定小于预期值
                j += 1
        return res

    n = len(matrix)
    low = matrix[0][0]
    high = matrix[n - 1][n - 1]
    while low < high:
        mid = low + (high - low) // 2
        count = getMid(mid)
        if count < k:
            low = mid + 1
        else:
            high = mid - 1
    return low


def getMid(matrix, mid):
    n = len(matrix)
    res = 0
    i = n - 1
    j = 0
    while i >= 0 and j < n:
        if matrix[i][j] > mid:
            i -= 1
        else:
            res += i + 1
            j += 1
    return res


if __name__ == '__main__':
    print(findMedianSortedArrays([1, 2], [3, 4]))
