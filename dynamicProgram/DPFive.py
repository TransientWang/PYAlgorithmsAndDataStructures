# -*- coding: UTF-8 -*-
def minFlipsMonoIncr(S):
    """
    926. 将字符串翻转到单调递增
    :type S: str
    :rtype: int
    """
    # l0 = r0 = l1 = r1 = 0  # 左边0 的个数，右边0 的格式，左边1的个数，右边1 的个数
    # for i in S:  # 首先计算所有的0 和 1 的个数
    #     if i == '0':
    #         r0 += 1
    #     else:
    #         r1 += 1
    # res = r0
    # for i in S:
    #     if i == '0':
    #         r0 -= 1
    #         l0 += 1
    #     else:
    #         r1 -= 1
    #         l1 += 1
    #     res = min(l1 + r0, res)  #左边的 1 全部变成 0，右边的 0 全部变成1
    # return res

    if not S or len(S) <= 1:
        return 0
    count_0, count_1 = [0] * (len(S) + 1), [0] * (len(S) + 1)
    for i, v in enumerate(S):
        if v == '0':
            count_0[i + 1] = count_0[i] + 1
            count_1[i + 1] = count_1[i]
        else:
            count_0[i + 1] = count_0[i]
            count_1[i + 1] = count_1[i] + 1
    res = 2000
    for i in range(len(S) + 1):  # 代表S前面i个字符全都是'0'
        res = min(res, count_1[i] + (count_0[-1] - count_0[i]))
    return res

if __name__ == '__main__':
    minFlipsMonoIncr("00011000")