# -*- coding: UTF-8 -*-
import math


def slove(nums, k):
    """
    二分，假定一个解并判断是否可行
    有N 条绳子，他们的长度为 nums[i],如果从他们中切割出K条长度相同的绳子的话，这K条绳子
    最长有多长？
    :param nums:
    :param k:
    :return:
    """

    def clac(x):
        num = 0
        for i in nums:
            num += i // x
        return num >= k

    lb, ub = float(0), float(10000)

    for i in range(1000):
        mid = (lb + ub) / 2
        if clac(mid):
            lb = mid
        else:
            ub = mid
    return math.floor(ub * 100000) / 100000


if __name__ == '__main__':
    print(slove([8.02, 7.43, 4.57, 5.39], 11))
