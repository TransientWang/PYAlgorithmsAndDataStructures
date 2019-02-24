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
    516. 最长回文子序列（review）
    回文子串可以不连续，相当于删除掉某些值
    回文串倒过来是一样的
    :type s: str
    :rtype: int
    """
    # 解 一
    # def find(s1, s2):
    #     m, n = len(s1), len(s2)
    #     dp = [[0] * (n + 1) for i in range(m + 1)]
    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             if s1[i - 1] == s2[j - 1]:
    #                 dp[i][j] = dp[i - 1][j - 1] + 1
    #             else:
    #                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    #     return dp[-1][-1]
    #
    # if s == s[::-1]:
    #     return len(s)
    # return find(s, s[::-1])

    # 解 二
    size = len(s)
    if s == s[::-1]: return size
    dp = [[0] * size for _ in range(size)]
    for i in range(size - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, size):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][-1]
    # 解 二优化
    # n = len(s)
    # dp = [0 for j in range(n)]
    # dp[n - 1] = 1
    #
    # for i in range(n - 1, -1, -1):  # can actually start with n-2...
    #     newdp = dp[:]
    #     newdp[i] = 1
    #     for j in range(i + 1, n):
    #         if s[i] == s[j]:
    #             newdp[j] = 2 + dp[j - 1]
    #         else:
    #             newdp[j] = max(dp[j], newdp[j - 1])
    #     dp = newdp
    #
    # return dp[n - 1]

    # 解 三
    dp = [[0] * len(s) for i in range(len(s))]
    for i in range(1, len(s)):
        dp[i][i] = 1
    for lens in range(1, len(s)):
        for i in range(len(s)):
            j = i + lens
            if j >= len(s):
                break
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][len(s) - 1]


def reversePairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    def merge_count(lo, hi):

        if lo == hi:
            return 0
        mid = (lo + hi) // 2
        count = merge_count(lo, mid) + merge_count(mid + 1, hi)
        j = mid + 1
        i = lo
        while i <= mid and j <= hi:

            if nums[i] > nums[j] * 2:

                count += mid - i+1
                j += 1
            else:
                i += 1

        nums[lo:hi + 1] = sorted(nums[lo:hi + 1])
        return count

    return merge_count(0, len(nums) - 1)


if __name__ == '__main__':
    print(reversePairs([1,3,2,3,1]))
