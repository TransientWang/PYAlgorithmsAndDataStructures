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


if __name__ == '__main__':
    print(maxProfit(2, [3, 2, 6, 5, 0, 3]))
