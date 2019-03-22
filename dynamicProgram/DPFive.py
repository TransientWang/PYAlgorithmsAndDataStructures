# -*- coding: UTF-8 -*-
import collections
from typing import List


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


def numExchange(line, n):
    """
    数字交换
    区间DP
    字符串S由小写字母构成，长度为n。定义一种操作，每次都可以挑选字符串中任意的两个相邻字母进行交换。
    询问在至多交换m次之后，字符串中最多有多少个连续的位置上的字母相同？
    :param line: abcdaa
    :param n: 2
    :return: 2
    """
    mp = collections.defaultdict(list)
    for i, val in enumerate(line):
        mp[val].append(i)
    count = 1
    for k, v in mp.items():
        if len(v) <= 1:
            continue
        dp = [[0] * len(v) for i in range(len(v))]
        for lens in range(2, len(v) + 1):
            for begin in range(len(v) - lens + 1):
                end = begin + lens - 1
                dp[begin][end] = dp[begin + 1][end - 1] + (v[end] - v[begin]) - lens + 1

                if dp[begin][end] < int(n):
                    count = max(count, lens)


def isMatch(s, p):
    """
    10. 正则表达式匹配(review)
    1, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];
    2, If p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1];
    3, If p.charAt(j) == '*':
    here are two sub conditions:
               1   if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
               2   if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == '.':
                              dp[i][44j] = dp[i-1][j]    //in this case, a* counts as multiple a
                           or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
                           or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty
    :type s: str
    :type p: str
    :rtype: bool
    """
    dp = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
    dp[0][0] = True
    for i in range(len(p)):
        if p[i] == "*" and dp[0][i - 1]:
            dp[0][i + 1] = True

    for i in range(len(s)):
        for j in range(len(p)):
            if p[j] == "." or s[i] == p[j]:
                dp[i + 1][j + 1] = dp[i][j]
            if p[j] == "*":
                if p[j - 1] != s[i] and p[j - 1] != ".":
                    dp[i + 1][j + 1] = dp[i + 1][j - 1]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1] or dp[i + 1][j - 1]
    return dp[-1][-1]


def isMatchTwo(s, p):
    """
    44. 通配符匹配(review)
    :type s: str
    :type p: str
    :rtype: bool
    """
    dp = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
    dp[0][0] = True
    for i in range(len(p)):
        if p[i] == "*":
            dp[0][i + 1] = dp[0][i]

    for i in range(len(s)):
        for j in range(len(p)):
            if (s[i] == p[j] or p[j] == "?") and dp[i][j]:
                dp[i + 1][j + 1] = dp[i][j]
            if p[j] == "*":
                dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1]

    return dp[-1][-1]


def getMoneyAmount(n: int) -> int:
    # 375. 猜数字大小 II
    # 区间dp
    cache = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for lo in range(n - 1, 0, -1):
        for hi in range(lo + 1, n + 1):
            cache[lo][hi] = float('inf')
            for pivot in range(lo, hi):
                cache[lo][hi] = min(cache[lo][hi], pivot + max(cache[lo][pivot - 1], cache[pivot + 1][hi]))
                # 每次猜完后有三种回答，大了，小了，等于（这种情况不用付钱）。取前两种情况的最大值
    return cache[1][n]


def checkSubarraySum(nums, k):
    """
    523. 连续的子数组和
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    # sums = sum(nums)
    # if ((sums == 0 and k ==0) and len(nums) >1) or (k!=0 and sums % k ==0 and len(nums) >1):
    #     return True
    # for start in range(len(nums)):
    #     sum_ = nums[start]
    #     for end in range(start +1,len(nums)):
    #         sum_ += nums[end]
    #         if (k == 0 and sum_ ==0) or (k != 0 and sum_ % k ==0):
    #             return True
    # return False
    # 解法二

    lookup = {0: -1}
    summing = 0
    n = len(nums)
    if n < 2: return False
    for i in range(0, n):
        summing += nums[i]
        if k != 0:
            summing = summing % k
        pre = lookup.get(summing, None)
        if pre != None and i - pre > 1:
            return True
        elif pre == None:
            lookup[summing] = i
    return False

def combinationSum4(nums: List[int], target: int) -> int:
    #377. 组合总和 Ⅳ
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(target+1):
        for j in nums:
            if i + j <= target:
                dp[i + j] += dp[i]
        print(dp)
    return dp[-1]
if __name__ == '__main__':
    print(combinationSum4([1, 2, 3], 4))
