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


def AggressiveCows(nums, n):
    """
    愤怒的牛
    二分，极大化极小
    农夫约翰搭了一间有N间牛舍的小屋。牛舍排在一条直线上，第i号牛舍在xi的位置。
    但是他的M头牛对小屋很不满意，因此经常相互攻击。约翰为了防止牛之间相互伤害，
    因此决定把每头牛都放在离其他牛尽可能远的牛舍。也就是说要最大化最近的两头牛之间的距离
    :param nums:
    :param n:
    :return:
    """

    def clac(d):
        last = 0
        for i in range(1, n):
            crt = last + 1
            while crt < len(nums) and nums[crt] - nums[last] < d:
                crt += 1
            if crt == len(nums):
                return False
            last = crt
        return True

    left, right = 0, 2 ** 31
    nums.sort()
    while right - left > 1:
        mid = left // 2 + right // 2
        if clac(mid):
            left = mid
        else:
            right = mid
    return left


if __name__ == '__main__':
    print(AggressiveCows([1, 2, 8, 4, 9], 3))
