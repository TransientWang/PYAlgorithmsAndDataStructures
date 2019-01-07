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


from heapq import *


def getSkyline(buildings):
    from functools import cmp_to_key
    ''' 
    218.天际线问题
    :param self:
    :param buildings:
    :return:
    开始，假设只有2个建筑物，拿出第一个buiding B1，我们先把它的左上顶点加进我们的output结果skyline中，
    然后继续拿下一个building B2，我们现在需要将B2的左上顶点对应的x coordinate与B1的右上顶点所对应的x coordinate做比较：

    如果前者小且B2的高度大于B1的高度，则我们将B2的左上顶点也加入skyline中去。
    如果前者小且B2的高度小于等于B1的高度，则忽略B2的左上顶点
    接下来考虑更多建筑物的情况，从左到右扫描，当我们遇到第一个楼的左边界时，把它push到一个heap中。
    如果后面扫描的楼的高度比heap中最高的楼还高，那么它的左上顶点一定会被加入到skyline中。
    当我们遇到一个building的右边界时,我们需要将其从heap中pop掉，如果heap中max height有变化，则push到结果中。
    '''
    # from collections import defaultdict
    # from heapq import heappush, heappop
    #
    # if not buildings:
    #     return buildings
    #
    # points = []
    # for l, r, h in buildings:
    #     points += [(l, -h), (r, h)]
    #
    # points.sort()
    #
    # result = []
    # heights = [0]
    # prev = heights[0]
    #
    # ignored = defaultdict(int)
    #
    # for x, h in points:
    #     if h < 0:
    #         heappush(heights, h)
    #     else:
    #         ignored[-h] += 1
    #
    #     while ignored[heights[0]] > 0:
    #         ignored[heights[0]] -= 1
    #         heappop(heights)
    #
    #     cur = heights[0]
    #     if cur != prev:
    #         result.append((x, -cur))
    #         prev = cur
    #
    # return result

    idx, n = 0, len(buildings) # TODO  没有完全理解
    liveBuildings, skyLine = [], []
    # liveBuildings：左上顶点已经加入结果集skyLine 但右上顶点还没有处理的building的右上顶点的集合
    # skyLine : 结果集

    while idx < n or len(liveBuildings) > 0:  # 如果所有building没处理完，或者有右顶点没处理完
        if len(liveBuildings) == 0 or (
                idx < n and buildings[idx][0] <= - liveBuildings[0][1]):  # 如果没有右顶点需要处理或者当前building左顶点比前面的右顶点小
            start = buildings[idx][0]  # 将处理的开始顶点设置为当前左顶点
            while idx < n and buildings[idx][0] == start:  # while 考虑左右坐标相同但是height不同的building
                heappush(liveBuildings, [-buildings[idx][2], -buildings[idx][1]])  # 将当前顶点的右顶点加入liveBuilding
                idx += 1
        else:  # 如果之前的右顶点没处理完，并且当前左顶点 >没处理的最大右顶点
            start = - liveBuildings[0][1]  # 将最大没处理右顶点当做处理的起始点
            while len(liveBuildings) > 0 and - liveBuildings[0][1] <= start:  # 如果还有右顶点没处理完，并且最高右顶点的横坐标大于 处理起点
                heappop(liveBuildings)
        height = len(liveBuildings) and - liveBuildings[0][0]
        if len(skyLine) == 0 or skyLine[-1][1] != height:
            skyLine.append([start, height])
    return skyLine


if __name__ == '__main__':
    print(getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
