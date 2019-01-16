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


def minDistance(word1, word2):
    """
    72. 编辑距离
    思路：动态规划
    可以对字符串进行三种操作
    dp[i][j] 代表 word1[i] 转换到word2[j] 所需要的操作次数
    插入dp[i][j-1] +1 = dp[i][j] 代表word2[i]，可以由 word1[:j-1] 添加一个字符得到
    删除 dp[i-1][j] + 1 = dp[i][j]  代表 word2[j] 可以 由 word1[i-1]删除一位字符得到
    替换：dp[i-1[j-1] + t = dp[i][j] 代表 Word2 与word1的长度相等，则可以通过一次替换最后一个字符得到
    如果最后一个字符相同，则不用替换 所以 t 为 1/0
    :type word1: str
    :type word2: str
    :rtype: int
    """
    if len(word2) == 0 or len(word1) == 0:
        return max(len(word2), len(word1))
    dp = [[i + j for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
    # dp = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
    # dp[0] = [i for i in range(len(word2) + 1)]
    for i in range(len(word1) + 1):
        dp[i][0] = i
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            tmp = 0 if word1[i - 1] == word2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j - 1] + tmp, dp[i][j - 1] + 1, dp[i - 1][j] + 1)

    return dp[-1][-1]


if __name__ == '__main__':
    print(minDistance(word1="horse", word2="ros"))
