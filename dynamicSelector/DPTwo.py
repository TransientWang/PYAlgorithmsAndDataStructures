# -*- coding: UTF-8 -*-

def longestValidParentheses(s):
    """
    32. 最长有效括号
    :type s: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    dp = [0 for i in range(len(s))]  # dp[i]表示以索引i结尾的串最长完成长度
    for i in range(1, len(s)):  # 第跳过一个肯定不成对，
        if s[i] == ")":  # 遇到 ） 的时候判断以i-1索引结尾的最长子串的左侧是否是 （，如果是则匹配 则dp[i] = dp[i-1]+2
            left = i - dp[i - 1] - 1
            if left >= 0 and s[left] == "(":
                dp[i] = dp[i - 1] + 2
                if left > 0:  # dp[left-1]左侧还有括号，则将其左侧最大值也加上
                    dp[i] += dp[left - 1]
    return max(dp)

if __name__ == '__main__':
    pass