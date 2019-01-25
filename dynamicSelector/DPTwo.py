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


def isInterleave(s1, s2, s3):
    """
    97. 交错字符串
    思路：dp[i][j] 代表 s1[i] 和 s2[j] 之后的子串是否可以组成 s3[i+j]之后的子串
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    if len(s1) + len(s2) != len(s3):
        return False
    dp = [[False for i in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    dp[-1][-1] = True
    for i in range(len(s1), -1, -1):
        for j in range(len(s2), -1, -1):
            if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:  #如果s1[i]满足条件并且 s2[i+j+1] 之前的子串可满足
                dp[i][j] = True
            elif j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                dp[i][j] = True
    return dp[0][0]

def numDistinct(s, t):
    """
    115. 不同的子序列
    dp[i][j]代表 s[:i] 与 t[:j],有多少个子序列相同
    :type s: str
    :type t: str
    :rtype: int
    """
    m, n = len(s), len(t)
    if m < n:
        return 0
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] != t[j - 1]:  # 如果当前字符不相等，那么去掉t中当前字符也一样
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]  # t 去掉当前字符 + s、t 都去掉当前字符
    return dp[-1][-1]

    # if len(s) < len(t) or len(t) == 0 or len(s) == 0:
    #     return 0
    # m = {}
    # for i, c in enumerate(t):
    #     m[c] = [i] + m.get(c, [])  # 找到t中各字符的索引，同样的字符的索引在一个list里面，通过m找到这个list
    # dp = [0] * len(t)
    # for c in s:  # 把s中的值找出其在t中的索引列表，遍历放到t[j]里面，放进去之后，到t[j]这个字符的路就相应要增加，
    #     # 增加个数为从开始到其之前一个字符的路，而从开始到之前一个字符的路的个数已经存在dp[j-1]里面了，所以dp[j]就相应增加一个dp[j-1],
    #     # 如果把一个字符放在了还没能到其前值的地方，那它自然不能到达，把它放在那里就完全没有意义，所以到它的路数肯定增加0。
    #     # (不会出现s中后面的值的路程数目被加到前面来的情况，例如'acbacbcb'与'abc'中的dp[1]不会把s[2]加到dp[1]中因为s[2]前面没有b。
    #     # 某个地方的值增加后暂时不会影响最后的值，只有它之后每个都在s的后面再出现时，才会更新到dp[-1]），dp中存的是s[i]之前所有可能下，
    #     # 开始到每个点的路径数量
    #     for j in m.get(c, []):
    #         if j == 0:
    #             dp[0] += 1
    #         else:
    #             dp[j] += dp[j - 1]
    # return dp[-1]

if __name__ == '__main__':
    print(isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
