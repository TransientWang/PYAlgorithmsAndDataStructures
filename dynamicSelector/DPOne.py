# -*- coding: UTF-8 -*-

'''
零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。
我们需要尽可能少的硬币个数，所以从11的总金额中取出任意一枚硬币，剩下的金额所需最少硬币个数再加上1就是所需硬币个数，
即所需硬币个数为：dp[10]+1、dp[9]+1、dp[6]+1，再从中取最小值，即可求解。以此类推，dp[10]=min(dp[9]+1,dp[8]+1,dp[5]+1)
所以可以看出，通过求出所有dp[1]、dp[2]、...、dp[10]的值，最终就能得到dp[11]的值。
'''


def coinChange(coins, amount):
    dp = [0]  # dp[i]代表在有多少钱的的时候，最少能找零的硬币数量
    l = amount + 1
    for i in range(1, l):
        dp.append(l)
        for j in coins:
            if i >= j:
                dp[i] = min(dp[i], dp[i - j] + 1)
    print(dp)
    if dp[amount] == amount + 1:
        return -1
    else:
        return dp[amount]


'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。
这道题不适合贪心算法
'''


def lengthOfLIS(nums):
    if len(nums)== 0:
        return 1
    l = len(nums)
    dp = [[1 for i in range(l)] for i in range(l)]

    max_res = 0
    for i in range(l):
        for j in range(l):
            if i < j:
                if nums[j] > max(nums[i:j]):
                    dp[i][j] = dp[i][j - 1] + 1
                else:
                    dp[i][j] = dp[i][j - 1]
                max_res = dp[i][j] if dp[i][j] > max_res else max_res


    for i in range(l):
        for j in range(l):
            print(dp[i][j], end=" ")
        print("\n")
    return max_res


if __name__ == '__main__':
    print(lengthOfLIS([10,9,2,5,3,4]))
# [1,3,6,7,9,4,10,5,6]
