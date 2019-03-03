# -*- coding: UTF-8 -*-
from functools import cmp_to_key


def maxEnvelopes(envelopes):
    """
    354. 俄罗斯套娃信封问题（review）
    动态规划
    二分
    把二维问题转化为一维问题
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


def minSteps(n, m):
    """
    最小步数（非LeetCode）
    输入两个整数 n,m，n可以乘2，减1，加1三种运算，求从 n 到 m 最少需要多少步。
    :param n:
    :param m:
    :return:
    """
    caluate = ["+", "-", "*"]
    dp = [0 for i in range(m - n + 1)]
    for i in range(1, len(dp)):
        p = []
        for j in caluate:
            if j == "*" and (i + n) % 2 == 0 and (i + n) // 2 >= n:
                p.append(dp[(i + n) // 2 - n] + 1)
            elif j == "+" and i + n - 1 >= n:
                p.append(dp[i - 1] + 1)
            elif j == "-" and i + n + 1 <= m:
                p.append(dp[i - 1] + 1)
        dp[i] = min(p)

    return dp[-1]


def longestSubstring(s, k):
    """
    395. 至少有K个重复字符的最长子串
    如果某一个字符在字符串中出现的次数少于 k,那么最长的子串一定在它两边
    :type s: str
    :type k: int
    :rtype: int
    """
    if len(s) < k:
        return 0
    for c in set(s):
        if s.count(c) < k:
            return max(longestSubstring(t, k) for t in s.split(c))
    return len(s)


def largestDivisibleSubset(nums):
    """
    368. 最大整除子集
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    res = []
    dp = [[]] * len(nums)  # 以nums[i] 结尾的符合要求的最长数组
    for i in range(len(nums)):
        tp = [nums[i]]
        for j in range(max(i - 1, 0), -1, -1):
            if not nums[i] % nums[j] and len(dp[j]) + 1 > len(tp):
                tp = dp[j] + [nums[i]]
        res = tp if len(tp) > len(res) else res
        dp[i] = tp
    return res


def palindromePairs(words):
    """
    336. 回文对
    :type words: List[str]
    :rtype: List[List[int]]
    """
    lookup = {word: i for i, word in enumerate(words)}
    res = []
    for i, word in enumerate(words):
        for j in range(len(word) + 1):
            pref, suff = word[:j], word[j:]
            # 去过后缀是回文，并且前缀在lookup里面而且前缀不等于当前单词，那么 pref[::-1]+suff + pref 是回文
            if suff == suff[::-1] and pref[::-1] in lookup and pref[::-1] != word:
                res.append([i, lookup[pref[::-1]]])
            # 如果前缀pref是回文且后缀suff的reverse也在words里面，那么suff[::-1]+(pref+suff)肯定是回文
            if pref == pref[::-1] and suff[::-1] in lookup and suff[::-1] != word:
                # 这是为了保证没有重复，例如：
                # 如果前面算了'abcd'+(''+'dcba')和'dcba'+(''+'abcd')的情况
                # 后面不能再算一遍('abcd'+'')+'dcba'和(‘dcba'+'')+'abcd'了
                if j != 0:
                    res.append([lookup[suff[::-1]], i])

    return res


if __name__ == '__main__':
    palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
