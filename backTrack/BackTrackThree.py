# -*- coding: UTF-8 -*-
def isScramble(s1, s2):
    """
    87. 扰乱字符串
    思路：如果s1和s2是 isScramble的，一定有s1的两个子串，s11,s12和s2的两个子串 s21和s22 ，并且s11和s21，s12和s22 ,s12和s21，s11，和s22
    这四个组合中必定有一对组合也是 isScramble的
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    if len(s1) != len(s2) or sorted(s1) != sorted(s2):
        return False
    if len(s1) < 4 or s1 == s2:  # len(s1) < 4 是一个过滤条件
        return True
    return any(
        isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:]) or
        isScramble(s1[:i], s2[-i:]) and isScramble(s1[i:], s2[:-i])
        for i in range(1, len(s1)))


def subsetsWithDup(nums):
    """
    90. 子集 II
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # nums.sort()
    # res = []
    #
    # def dfs(nums, lists):
    #
    #     if lists not in res:
    #         res.append(lists)
    #     for i in range(len(nums)):
    #         sub = dfs(nums[i + 1:], lists + [nums[i]])
    #
    # dfs(nums, [])
    #
    # return res
    res = [[]]

    nums.sort()

    def dfs(index, lists):
        if index == len(nums):
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue

            res.append(lists + [nums[i]])
            dfs(i + 1, lists + [nums[i]])

    dfs(0, [])
    return res


def restoreIpAddresses(s):
    """
    93. 复原IP地址
    思路：DFS + 剪枝条件
    剪枝条件 ：
    当 remain[:i] > 255 或者remain[:i] 长度 > 1 但是 remain[:i][0] == "0"  并且剩余字符串长度  > 合法长度
    :type s: str
    :rtype: List[str]
    """
    res = []

    def find(remain, num, tmp):
        """
        :param remain: 剩余字符串
        :param num: 还剩几节没遍历
        :param tmp: 临时字符串
        :return:
        """
        if num == 1 and ((len(remain) > 1 and remain[0] != "0") or len(remain) == 1) and int(remain) <= 255:
            res.append(tmp + remain)
            return
        for i in range(1, len(remain)):

            if int(remain[:i]) > 255:
                return
            if len(remain[i:]) <= (num - 1) * 3 and (
                    (len(remain[:i]) > 1 and remain[:i][0] != "0") or len(remain[:i]) == 1):
                tmp = remain[:i] + "." if tmp == "" else tmp + remain[:i] + "."
                find(remain[i:], num - 1, tmp)
                tmp = tmp[:-i - 1]

    find(s, 4, "")
    return res


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
    print(numDistinct("rabbbit", "rabbit"))
