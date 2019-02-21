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
    回文子串可以不连续，相当于删除掉某些值
    回文串倒过来是一样的
    :type s: str
    :rtype: int
    """
    #
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


def countRangeSum(nums, lower, upper):
    """
    327. 区间和的个数
    :param nums:
    :param lower:
    :param upper:
    :return:
    """
    # 动态规划 TLE
    # nums.sort()
    # dp = [[0] * len(nums) for i in range(len(nums))]
    # sum = 0
    # for i in range(len(nums)):
    #     for j in range(i, len(nums)):
    #         dp[i][j] = nums[j] + dp[i][j - 1]
    #         if dp[i][j] >= lower and dp[i][j] <= upper:
    #             sum += 1
    # return sum

    # 分治法，通过分治法将范围不断缩小，由递归函数处理每一块较小的范围
    sums = [0]
    for i in nums:
        sums.append(sums[-1] + i)

    def sort(lo, hi):
        if hi - lo <= 1:  # 如果数组只有一个数，那么下面的算法将不能比较出来，还会将数组长度退化成1，在下面的 sort 会栈溢出
            return 0

        mid = (lo + hi) // 2
        count = sort(lo, mid) + sort(mid, hi)
        i = j = mid  # 放在for 循环的外面，已经计算过的就不再重复，减少计算量
        for left in sums[lo:mid]:  # 对于 lo:mid 和 mid:hi 的所有情况已经在递归中全部计算过了，现在只有右边减去左边的可能没有出现过
            while i < hi and sums[i] - left < lower: i += 1
            while j < hi and sums[j] - left <= upper: j += 1
            count += j - i
        sums[lo:hi] = sorted(sums[lo:hi])  # 如果不排序，就会出现前面较大的数sums[h] (h >=mid)
        # 在索引低位的数 left计算失败后，left后移，而后面较小的数 sums[h+1] 计算不到 left 的情况的情况
        return count

    return sort(0, len(sums))


if __name__ == '__main__':
    print(countRangeSum([-2, 5, -1],
                        -2,
                        2))
