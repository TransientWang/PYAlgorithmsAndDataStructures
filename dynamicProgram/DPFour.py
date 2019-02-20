# -*- coding: UTF-8 -*-
from functools import cmp_to_key


def maxEnvelopes(envelopes):
    """
    354. 俄罗斯套娃信封问题
    动态规划
    二分
    :type envelopes: List[List[int]]
    :rtype: int
    """
    if not envelopes:
        return 0
    envelopes = list(map(lambda a: a[1], sorted(envelopes, key=lambda a: (a[0], -a[1]))))
    # 基本dp
    dp = [1] * len(envelopes)
    for i in range(1, len(envelopes)):
        for j in range(i):
            if envelopes[i] > envelopes[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
    # 优化
    # p = [1] * len(envelopes)
    # for i in range(1, len(envelopes)):
    #     for j in range(i):
    #         if envelopes[i] > b[j]
    # for i in range(len(b)):
    #     if envelopes[i] > p[-1]:
    #         p.append(b[i])
    #     else: #排序
    #         for j in range(len(p) - 1, -1, -1):
    #             if envelopes[i] > p[j]:
    #                 if j == len(p) - 2:
    #                     p[-1] = envelopes[i]
    #                 else:
    #                     p[j + 1] = envelopes[i]
    #                 break
    # return len(p) - 1

    # 优化二分法
    # for i in range(len(envelopes)):
    #     if envelopes[i] > p[-1]:
    #         p.append(envelopes[i])
    #     else:
    #         left, right = 0, len(p)
    #         while left < right:
    #             mid = (left + right) // 2
    #             if envelopes[i] <= p[mid]:
    #                 right = mid
    #             else:
    #                 left = mid + 1
    #         p[right] = envelopes[i]
    # return len(p) - 1


def longestPalindromeSubseq(s):
    """
    516. 最长回文子序列
    回文串倒过来是一样的
    :type s: str
    :rtype: int
    """

    def find(s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

    if s == s[::-1]:
        return len(s)
    return find(s, s[::-1])


if __name__ == '__main__':
    print(longestPalindromeSubseq("bbbab"))
