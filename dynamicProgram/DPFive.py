# -*- coding: UTF-8 -*-
def minFlipsMonoIncr(self, S):
    """
    926. 将字符串翻转到单调递增
    :type S: str
    :rtype: int
    """
    l0 = r0 = l1 = r1 = 0
    for i in S:
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
        res = min(l1 + r0, res)
    return res