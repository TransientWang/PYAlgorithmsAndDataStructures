# -*- coding: UTF-8 -*-

import copy
from heapq import *

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
    378	.有序矩阵中第K小的元素（review）
    思路：二分法，如果横向比较那么上一行的元素，不一定全比当前元素小，但是当前元素竖直方向上面的元素一定比当前元素小
    :param matrix:
    :param k:
    :return:
    '''
    # 解法一
    queue = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if len(queue) < k:
                heappush(queue, -matrix[i][j])
            elif -matrix[i][j] >= queue[0]:
                heappop(queue)
                heappush(queue, -matrix[i][j])

    return -heappop(queue)
    #解法二
    def counter(mid):
        i, j, count = len(matrix) - 1, 0, 0
        while i >= 0 and j < len(matrix[0]):
            if mid < matrix[i][j]:
                i -= 1
            else:
                count += i + 1
                j += 1
        return count


    lo, hi = matrix[0][0], matrix[-1][-1]
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        count = counter(mid)
        if count < k:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo




def getSkyline(buildings):
    from functools import cmp_to_key
    from heapq import heappush, heappop
    ''' 
    218.天际线问题
    线段树问题，去掉重合的线段，并且加入了高度这一维度
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
    events = sorted([(L, -H, R) for L, R, H in buildings] + list(set((R, 0, None) for _, R, _ in buildings)))
    # (R, 0, None)可以与  (L, -H, R) 区分出左右顶点
    res, hp = [[0, 0]], [(0, 2 ** 31)]  # res:结果集 hp：大顶堆，左顶点已经加入结果集，但是右顶点还没有处理的（高度，右顶点）
    for x, H, R in events:
        while x >= hp[0][1]:  # 如果当前左顶点大于大顶堆中最高的右顶点
            heappop(hp)  # 已经该建筑物处理完毕，将其高度排除
        if H:  # 如果是左顶点，则将左顶点加入大顶堆
            heappush(hp, (H, R))
        if res[-1][-1] + hp[0][0]:  # 前一个是左顶点时候同一个建筑物的右顶点不能加入，或者不同建筑物的高度不可以相同
            res.append([x, -hp[0][0]])
    return res[1:]

    # idx, n = 0, len(buildings) # TODO  没有完全理解
    # liveBuildings, skyLine = [], []
    # # liveBuildings：左上顶点已经加入结果集skyLine 但右上顶点还没有处理的building的右上顶点的集合
    # # skyLine : 结果集
    #
    # while idx < n or len(liveBuildings) > 0:  # 如果所有building没处理完，或者有右顶点没处理完
    #     if len(liveBuildings) == 0 or (
    #             idx < n and buildings[idx][0] <= - liveBuildings[0][1]):  # 如果没有右顶点需要处理或者当前building左顶点比前面的右顶点小
    #         start = buildings[idx][0]  # 将处理的开始顶点设置为当前左顶点
    #         while idx < n and buildings[idx][0] == start:  # while 考虑左右坐标相同但是height不同的building
    #             heappush(liveBuildings, [-buildings[idx][2], -buildings[idx][1]])  # 将当前顶点的右顶点加入liveBuilding
    #             idx += 1
    #     else:  # 如果之前的右顶点没处理完，并且当前左顶点 >没处理的最大右顶点
    #         start = - liveBuildings[0][1]  # 将最大没处理右顶点当做处理的起始点
    #         while len(liveBuildings) > 0 and - liveBuildings[0][1] <= start:  # 如果还有右顶点没处理完，并且最高右顶点的横坐标大于 处理起点
    #             heappop(liveBuildings)
    #     height = len(liveBuildings) and - liveBuildings[0][0]
    #     if len(skyLine) == 0 or skyLine[-1][1] != height:
    #         skyLine.append([start, height])
    # return skyLine


if __name__ == '__main__':
    print(getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
