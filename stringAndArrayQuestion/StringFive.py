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


def countRangeSum(nums, lower: int, upper: int) -> int:
    nums = nums
    dp = [[0] * len(nums) for i in range(len(nums))]
    res = 0

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i == j:
                dp[i][j] = nums[i]
            else:
                dp[i][j] = dp[i][j - 1] + nums[j]
            if dp[i][j] >= lower and dp[i][j] <= upper:
                res += 1

    return res
if __name__ == '__main__':
    print(countRangeSum([2147483647, -2147483648, -1, 0], -1, 0))
