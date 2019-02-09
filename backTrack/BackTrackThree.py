# -*- coding: UTF-8 -*-
from dataStructure import TreeNode


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


def findLadders(beginWord, endWord, wordList):
    """
    126. 单词接龙 II
    bfs
    先找出在遍历每个单词之前可以找到的相邻单词，然后回溯
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: List[List[str]]
    """
    if endWord not in wordList:
        return []
    wordList = set(wordList)
    lookup = set(wordList + [beginWord])
    res, cur, routine = [], set([beginWord]), {word: [] for word in lookup}
    while cur and endWord not in cur:
        next_queue = set()
        for i in cur:
            lookup.remove(i)
        for word in cur:
            for i in range(len(word)):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    tmp = word[:i] + j + word[i + 1:]
                    if tmp in lookup:
                        next_queue.add(tmp)
                        routine[tmp].append(word)
        cur = next_queue

    def bfs(path, word):
        if len(routine[word]) == 0:
            res.append([word] + path)
        else:
            for pre in routine[word]:
                bfs([word] + path, pre)

    if cur:
        bfs([], endWord)
    return res


def sumNumbers(root):
    """
    129. 求根到叶子节点数字之和
    dfs
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    res = [0]

    def find(root, tmp):
        if root.left:
            find(root.left, tmp + str(root.val))
        if root.right:
            find(root.right, tmp + str(root.val))
        if not root.left and not root.right:
            res[0] += int(tmp + str(root.val))

    find(root, "")

    return res[0]


def diffWaysToCompute(input):
    """
    241. 为运算表达式设计优先级
    :type input: str
    :rtype: List[int]
    """

    def helper(m, n, op):
        if op == "+":
            return m + n
        elif op == "-":
            return m - n
        else:
            return m * n

    if input.isdigit():
        return [int(input)]
    res = []
    for i in range(len(input)):
        if input[i] in "-+*":
            res1 = diffWaysToCompute(input[:i])
            res2 = diffWaysToCompute(input[i + 1:])
            res.extend(helper(j, k, input[i]) for j in res1 for k in res2)
    return res



if __name__ == '__main__':
    print(diffWaysToCompute("2*3-4*5"))

    # root = TreeNode.TreeNode(4)
    # # root.left = TreeNode.TreeNode(9)
    # # root.right = TreeNode.TreeNode(0)
    # # root.left.left = TreeNode.TreeNode(5)
    # # root.left.right = TreeNode.TreeNode(1)
    # # root.right.left = TreeNode.TreeNode(-2)
    # # root.right.right = TreeNode.TreeNode(6)
    # # root.left.left.left = TreeNode.TreeNode(-1)
    # print(sumNumbers(root))
