# -*- coding: UTF-8 -*-
def minCut(s):
    """
    132. 分割回文串 II
    dp[i] 记录 从 0 到 i 需要切几刀才能使 全部子串为回文
    这样就需要遍历所有子序列，取每段子序列 [j:i] 和 [:j-1]+1 的最小值
    :type s: str
    :rtype: int
    """
    # if not s:
    #     return 0
    #
    # s_len = len(s)
    # mem = [i for i in range(-1, s_len)]
    # for i in range(1, s_len + 1):
    #     for j in range(i):
    #         if s[j:i] == s[j:i][::-1]:
    #             mem[i] = min(mem[i], mem[j] + 1)
    # return mem[-1]
    if s == s[::-1]: return 0
    for i in range(1, len(s)):
        if s[i:] == s[:i - 1:-1] and s[:i] == s[i - 1::-1]: return 1
    # 切分 0次 和 1次的过滤一下
    dp = [i for i in range(len(s))]  # 0到dp[i]需要切分几次
    vald = [[False for i in range(len(s))] for i in range(len(s))]  # 从s[i][j]是否是回文串
    for i in range(len(s)):
        for j in range(i + 1):  # 遍历所有子序列
            if s[i] == s[j] and (i - j <= 1 or vald[j + 1][i - 1]):
                dp[i] = min(dp[i], dp[j - 1] + 1) if j != 0 else 0  # j == 0 的时候不用切分，j !=0 的时候需要进行比较
                vald[j][i] = True
    return dp[-1]


def calculateMinimumHP(dungeon):
    """
    174. 地下城游戏
    动态规划反推
    :type dungeon: List[List[int]]
    :rtype: int
    """
    m = len(dungeon)
    n = len(dungeon[0])
    dp = [[0] * n] * m  # 代表从dp[i][j] 出发所需要的最少血量

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j == n - 1:
                dp[i][j] = max(1, 1 - dungeon[i][j])
            elif i == m - 1:
                print(dp[i][j + 1] - dungeon[i][j])
                dp[i][j] = max(1, dp[i][j + 1] - dungeon[i][j])

            elif j == n - 1:
                dp[i][j] = max(1, dp[i + 1][j] - dungeon[i][j])

            else:  # 从dp[i][j] 出发需要的最少血量，为从它的后一步（往右，往下），到它之间需要的最少血量
                dp[i][j] = max(1, min(dp[i + 1][j] - dungeon[i][j], dp[i][j + 1] - dungeon[i][j]))
    return dp[0][0]


def maxProfit(k, prices):
    """
    188. 买卖股票的最佳时机 IV
    dp[k][i] 代表第 i 天完成 k 次交易的最大收益
    dp[k][i] = max(dp[k][i-1],dp[k-1][i-1] + prices[i] - prices[j]) (0<j<i )
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    if not prices or len(prices) == 0:
        return 0
    if k >= len(prices) // 2:
        return sum([max(prices[i] - prices[i - 1], 0) for i in range(1, len(prices))])

    # dp = [[0] * len(prices)] * (k + 1)
    # mdp = [prices[0]] * (k + 1)
    # for i in range(1, len(prices)):
    #     for j in range(1, k + 1):
    #         mdp[j] = min(mdp[j], prices[i] - dp[j - 1][i - 1]) # prices[i] - dp[j - 1][i - 1] 第 i 天的金额减去 i-1 天之前的收益
    #         dp[j][i] = max(dp[j][i - 1], prices[i] - mdp[j]) #当前值 - 之前的总付出= 当前收益
    # return dp[-1][-1]

    # 优化空间
    dp = [0] * (k + 1)
    mdp = [prices[0]] * (k + 1)
    for i in range(1, len(prices)):
        for j in range(1, min(k + 1, i // 2 + 2)):  # min(k + 1, i // 2 + 2) 计算优化 + 2 是因为进度问题 +1 范围会不准确
            mdp[j] = min(mdp[j], prices[i] - dp[j - 1])
            dp[j] = max(dp[j], prices[i] - mdp[j])
    return dp[-1]


def change(amount, coins):
    """
    518. 零钱兑换 II
    动态规划
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    dp = [0 for i in range(amount + 1)]  # 兑换 i 元的方案数
    dp[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], amount + 1):
            # 使用前 i 中钱币，兑换 j的方案数 = 使用前 i 中钱币表示兑换 j + 使用前 i 中钱币表示兑换 j-coins[i]
            dp[j] = dp[j] + dp[j - coins[i]]
            # 兑换 j 的方案数 可以分为两部分，一部分是算上coins[i]的方案数 为 dp[j]
            # 另一部分是去除 coins[i] 的方案数，因为 coins[i]+每种组成 j - coins[i] 的方案 都会得到 j
            # 所以为dp[j-coins[i]]
    return dp[-1]


def longestCommonSubstring(m, n):
    """
    最长公共连续子串
    给出两个字符串（可能包含空格）,找出其中最长的公共连续子串,输出其长度。

    输入描述:
    输入为两行字符串（可能包含空格），长度均小于等于50.

    :param m:
    :param n:
    :return:最长公共连续子串的长度。
    """
    dp = [[0 for i in range(len(n) + 1)] for i in range(len(m) + 1)]  # m[:i] 与 n[:j] 的最长公共子序列
    res = 0
    for i in range(1, len(m) + 1):
        for j in range(1, len(n) + 1):
            if m[i - 1] == n[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                res = max(res, dp[i][j])
    return res


def countBits(num):
    """
    338. 比特位计数
    动态规划
    思路：将数字转换成二进制
    最多需要1 的个数为，0 、2 ** 0（1）,2**1（2-3）、2**2（4-7）、2**3（8-15）
    每个数二进制中1的个数= 1+ （该数字 - 该数字所在区间大小所在数字的 1的位数））
    :type num: int
    :rtype: List[int]
    """
    # dp = [0]
    # k = 0
    # for i in range(1,num + 1):
    #     dp.append(dp[i - 2 ** k] + 1)
    #     if i == 2 ** k:
    #         k += 1
    # return dp

    list1 = [0]
    while len(list1) < num + 1:
        list1 += [i + 1 for i in list1]

    return list1[:num + 1]


if __name__ == '__main__':
    print(countBits(10))
