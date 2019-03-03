# -*- coding: UTF-8 -*-
import collections
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
    up,dw = 0,0
    n2 = collections.Counter(nums2)
    res = []
    while up < len(nums1):
        if nums1[up] in n2 and n2[nums1[up]] > 0:
            res.append(nums1[up])
            n2[nums1[up]] = 0
        up +=1
    return res