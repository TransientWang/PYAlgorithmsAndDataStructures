# -*- coding: UTF-8 -*-
"""0-1 背包问题"""


def bagSlution(c, w, v):
    """
    dp[ i ][ j ] 表示 在面对第 i 件物品，且背包容量为  j 时所能获得的最大价值
    :param c: 背包总重量
    :param w: 单个物品重量数组
    :param v: 单个物品价值
    :return:
    """
    dp = [[0] * (c + 1) for i in range(len(w) + 1)]
    res = 0
    for i in range(1, len(w) + 1):
        for j in range(w[i - 1], c + 1):
            dp[i][j] = max(dp[i - 1][j - w[i - 1]] + v[i - 1], dp[i - 1][j])
            res = max(dp[i - 1][j], res)
    for i in range(len(w) + 1):
        print(dp[i])
    print(res)


if __name__ == '__main__':
    bagSlution(12, [4, 6, 2, 2, 5, 1],
               [8, 10, 6, 3, 7, 2])
