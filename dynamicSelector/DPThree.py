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


if __name__ == '__main__':
    print(minCut("abbab"))
