# -*- coding: UTF-8 -*-


def coinChange(coins, amount):
    '''
    零钱兑换
    给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
    如果没有任何一种硬币组合能组成总金额，返回 -1。
    我们需要尽可能少的硬币个数，所以从11的总金额中取出任意一枚硬币，剩下的金额所需最少硬币个数再加上1就是所需硬币个数，
    即所需硬币个数为：dp[10]+1、dp[9]+1、dp[6]+1，再从中取最小值，即可求解。以此类推，dp[10]=min(dp[9]+1,dp[8]+1,dp[5]+1)
    所以可以看出，通过求出所有dp[1]、dp[2]、...、dp[10]的值，最终就能得到dp[11]的值。
    '''
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
用一个辅助数组来保存从0当前节点的最优值
'''


def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0
    dp = []
    max_res = 1
    for i in range(len(nums)):
        dp.append(1)
        for j in range(i):  # 计算的子序列是从0开始，到i结束
            if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
            if dp[i] > max_res:
                max_res = dp[i]
    # for j in range(l):
    #     print(dp[j], end=" ")
    # print("\n")
    return max_res


def maxArea(height):
    '''
    盛最多水的容器
    给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

    说明：你不能倾斜容器，且 n 的值至少为 2。
    思路：典型的动态规划，但是 时间复杂度要求在o(n²)以下，次问题只遍历一遍，让左右索引向中间移动就可以了
    :param height:
    :return:
    '''
    res = 0
    i, j = 0, len(height) - 1
    while i < j:
        res = max(min(height[i], height[j]) * (j - i), res)
        if height[i] <= height[j]:
            i += 1
        else:
            j -= 1
    return res


def maxProduct(nums):
    '''
     乘积最大子序列
     关键点在，如果整个序列的符号个数是偶数，那么就 只关心 出现0的情况
     遇到负号的情况,如果整个序列的符号个数是奇数，那么还需要记录最小值
     这样这个最小值在遇到下一个辅助的时候就变成了正值

    :param nums:
    :return:
    '''
    maxVal = nums[0]
    minVal = nums[0]
    dp = nums[0]
    for i in range(1, len(nums)):
        tmp = maxVal
        maxVal = max(maxVal * nums[i], minVal * nums[i], nums[i])  # 如果序列都是大于0的数，那么唯一关心的数字就是0
        minVal = min(tmp * nums[i], minVal * nums[i], nums[i])  # 如果序列出现了小于0的数字，那么需要把这个小于0的数字记录下来
        # 当在此出现小于0的数字时，便于比较
        dp = max(maxVal, dp)
    return dp


def wordBreak(s, wordDict):
    '''
    单词拆分
    给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

    说明：

    拆分时可以重复使用字典中的单词。
    你可以假设字典中没有重复的单词。
    :param s:
    :param wordDict:
    :return:
    '''
    dp = [False for i in range(len(s) + 1)]  # dp[i]表示s[0:i]可以拆分成单词
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(len(wordDict)):
            if i < len(wordDict[j]):
                continue
            if dp[i - len(wordDict[j])] and s[i - len(wordDict[j]):i] == wordDict[j]:
                dp[i] = True
    return dp[-1]


if __name__ == '__main__':
    print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
# [1,3,6,7,9,4,10,5,6]
