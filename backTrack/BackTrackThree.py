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





if __name__ == '__main__':
   pass
