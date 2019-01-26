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

    dp = [i for i in range(len(s))]
    vald = [[False for i in range(len(s))] for i in range(len(s))]
    for i in range(len(s)):
        for j in range(i + 1):  # 遍历所有子序列
            if s[i] == s[j] and (i - j <= 1 or vald[j + 1][i - 1]):
                dp[i] = min(dp[i], dp[j - 1] + 1) if j != 0 else 0  # j == 0 的时候不用切分，j !=0 的时候需要进行比较
                vald[j][i] = True

    return dp[-1]


if __name__ == '__main__':
    print(minCut("abbab"))
