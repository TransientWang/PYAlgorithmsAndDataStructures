# -*- coding: UTF-8 -*-
def minFlipsMonoIncr(self, S):
    """
    926. 将字符串翻转到单调递增
    :type S: str
    :rtype: int
    """
    l0 = r0 = l1 = r1 = 0  # 左边0 的个数，右边0 的格式，左边1的个数，右边1 的个数
    for i in S:  # 首先计算所有的0 和 1 的个数
        if i == '0':
            r0 += 1
        else:
            r1 += 1
    res = r0
    for i in S:
        if i == '0':
            r0 -= 1
            l0 += 1
        else:
            r1 -= 1
            l1 += 1
        res = min(l1 + r0, res)  #左边的 1 全部变成 0，右边的 0 全部变成1
    return res
