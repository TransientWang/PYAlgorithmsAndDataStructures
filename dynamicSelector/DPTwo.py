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


def numDecodings(s):
    """
    91. 解码方法
    斐波那契数列的加强版
    :type s: str
    :rtype: int
    """
    if len(s) == 0 or s[0] == "0":
        return 0
    dp = [0 for i in range(len(s) + 1)]
    dp[0] = 1

    for i in range(1, len(dp)):
        if s[i - 1] == "0":  # 计算 i-1
            dp[i] = 0
        else:
            dp[i] = dp[i - 1]

        if i > 1 and (s[i - 2] == "1" or (s[i - 2] == "2" and s[i - 1] <= "6")):  # 计算 i-2
            dp[i] += dp[i - 2]
    return dp[-1]


def numTrees(n):
    """
    96. 不同的二叉搜索树
    思路：1到n都可以作为二叉搜索树的根节点，当k是根节点时，它的左边有k-1个不等的数，它的右边有n-k个不等的数。
    以k为根节点的二叉搜索树的种类就是左右可能的种类的乘积。用递推式表示就是
    h(n) = h(0)*h(n-1) + h(1)*h(n-2) + ... + h(n-1)h(0) (其中n>=2) ，其中h(0)=h(1)=1
    因为0个或者1个数能组成的形状都只有一个。从1到n依次算出h(x)的值即可。此外这其实就是一个卡特兰数
    :type n: int
    :rtype: int
    """
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        for k in range(i):
            dp[i] += dp[k] * dp[i - k - 1]
    return dp[-1]


if __name__ == '__main__':
    print(numDecodings("17"))
