# -*- coding: UTF-8 -*-
from heapq import heappushpop, heappush, nsmallest
from math import hypot
import doctest


def kClosest(points, K):
    """
    973. 最接近原点的 K 个点
    >>> print(1111)
    :type points: List[List[int]]
    :type K: int
    :rtype: List[List[int]]
    """
    # return nsmallest(K, points, lambda p: hypot(p))
    heap = []
    for t1, t2 in points:
        if len(heap) < K:
            heappush(heap, (-hypot(t1, t2), (t1, t2)))
        else:
            heappushpop(heap, (-hypot(t1, t2), (t1, t2)))

    return [p[1] for p in heap]


def slove(nums, S):
    """
    尺取法
    给定长度为n的数列整数 nums,与最大值S。求总和不小于S的连续子序列长度的最小值。
    :param nums:
    :param S:
    :return:
    """
    res = len(nums) + 1
    left = sums = 0
    for right, val in enumerate(nums):
        if sums < S:
            sums += val
        while sums >= S:
            sums -= nums[left]
            res = min(res, right - left + 1)
            left += 1
    return res


if __name__ == '__main__':
    print(slove([1, 2, 3, 4, 5], 11))
    # doctest.testmod()
