# -*- coding: UTF-8 -*-
import collections
from typing import List


def reverseString(s):
    """
    344. 反转字符串(review)
    :param s:
    :return:
    """
    i = 0
    j = len(s) - 1
    while i < j:
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp
        i += 1
        j -= 1


def intersection(nums1, nums2):
    """
    349. 两个数组的交集
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    up, dw = 0, 0
    n2 = collections.Counter(nums2)
    res = []
    while up < len(nums1):
        if nums1[up] in n2 and n2[nums1[up]] > 0:
            res.append(nums1[up])
            n2[nums1[up]] = 0
        up += 1
    return res


def isLongPressedName(name, typed):
    """
    925
    :type name: str
    :type typed: str
    :rtype: bool
    """
    if len(set(name)) != len(set(typed)):
        return False

    idx = 0
    tdx = 0
    while idx < len(name) and tdx < len(typed):
        if name[idx] == typed[tdx]:
            idx += 1
            tdx += 1
        elif tdx > 0 and typed[tdx] == typed[tdx - 1]:
            tdx += 1
        else:
            return False

    return True if name[-1] == typed[-1] else False


def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    #713. 乘积小于K的子数组
    #尺取法
    if k <= 1:
        return 0
    left = res = 0
    pre = 1
    for right, val in enumerate(nums):
        pre *= val
        while pre >= k:
            pre /= nums[left]
            left += 1
        res += right - left + 1
    return res


if __name__ == '__main__':
    pass
