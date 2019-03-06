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
    518. 零钱兑换 II(review)
    动态规划，组合
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    dp = [0 for _ in range(amount + 1)]  # 兑换 i 元的方案数
    dp[0] = 1
    coins.sort()
    for i in coins:
        for j in range(i, amount + 1):
            # 使用前 i 中钱币，兑换 j的方案数 = 使用前 i 中钱币表示兑换 j + 使用前 i 中钱币表示兑换 j-coins[i]
            dp[j] = dp[j] + dp[j - i]
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
    338. 比特位计数(reciew)
    动态规划
    思路：将数字转换成二进制
    最多需要1 的个数为，0 、2 ** 0（1）,2**1（2-3）、2**2（4-7）、2**3（8-15）
    每个数二进制中1的个数 = 1+ （该数字 - 该数字所在区间大小所在数字的 1的位数））
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


def integerBreak(n):
    """
    343. 整数拆分(review)
    将 7-10进行拆分得到规律
    从 7 开始往后 如果 数字 n -4 得到的值 能整除3 则结果为 4 * (3 ** ((n - 4) // 3))
    否则 计算n //3 的值three，再计算 n- three*3 =lift 结果为(3 ** three) * lift
    :type n: int
    :rtype: int
    """
    dp = [1, 2]
    if n < 4:
        return dp[n - 2]
    if (n - 4) % 3 != 0:
        three = n // 3
        lift = n - three * 3
        if lift == 0: lift = 1
        return (3 ** three) * lift
    else:
        return 4 * (3 ** ((n - 4) // 3))


def maxNumber(nums1, nums2, k):
    """
    321. 拼接最大数（review）
    贪心选择，动态规划
    一共k位digit，我们可以先确定从nums1里面取i位，那么从nums2肯定就是取k-i位
    然后我们确定了从nums1里面取i位的话，就可以算出所能取得的长度为i的最大子序列lis1，相应的也可以算出从nums2取得的长度为k-i的最大子序列lis2
    然后我们用双指针依次从lis1和lis2中取较大的那个数就可以了，不停更新res
    Note：

    i至少需要k - len(nums2)，否则digit不够, 但是如果k - len(nums2)小于0的话，i还是要从0开始取
    i最多取到k，但是因为num1也有长度限制，所以如果k > len(nums1)的时候，i最多取len(nums1)
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[int]
    """

    def getList(num, k):
        """
        求最大子序列
        贪心选择、栈
        :param num:
        :param k:
        :return:
        """
        res, n = [], len(num)
        for i in range(n):
            while res and len(res) + (n - i) > k and res[-1] < num[i]:  # len(res) + (n - i) > k 贪心性质保证有足够数量的元素
                res.pop()
            if len(res) < k:
                res.append(num[i])
        return res

    res = [0] * k
    for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
        # max(0, k - len(nums2))当 nums2 长度较短的时候，min(k, len(nums1))：当nums1 长度过长的时候
        list1 = getList(nums1, i)
        list2 = getList(nums2, k - i)
        res = max(res, [max(list1, list2).pop(0) for _ in range(k)])
    return res


if __name__ == '__main__':
    print(2 & 1)
    print(countBits(4))
    print(max([2, 2, 3], [2, 3, 4]))
